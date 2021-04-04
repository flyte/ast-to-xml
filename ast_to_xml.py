import ast
import textwrap
from importlib import import_module
from types import ModuleType

from lxml import etree as ET

ATTRS = ("lineno", "col_offset", "end_lineno", "end_col_offset")


def ast_node_attrs(ast_node):
    attrs = {}
    for key in ATTRS:
        try:
            attrs[key] = str(getattr(ast_node, key))
        except AttributeError:
            continue
    return attrs


def visit_node(ast_node, parent_xml_node=None):
    xml_node_name = ast_node.__class__.__name__

    if parent_xml_node is None:
        xml_node = ET.Element(xml_node_name)
    else:
        xml_node = ET.SubElement(parent_xml_node, xml_node_name)

    xml_node.attrib.update(ast_node_attrs(ast_node))

    for key, value in ast_node.__dict__.items():
        if key.startswith("_") or key in ATTRS:
            continue
        if isinstance(value, ast.AST):
            sub_node = ET.SubElement(xml_node, key)
            visit_node(value, sub_node)
        elif isinstance(value, list):
            if all(isinstance(x, ast.AST) for x in value):
                sub_node = ET.SubElement(xml_node, key)
                for node in value:
                    visit_node(node, sub_node)
        else:
            node = ET.SubElement(xml_node, key)
            node.attrib["type"] = type(value).__name__
            node.text = str(value)

    return xml_node


def xml(src):
    ast_tree = ast.parse(src)
    return visit_node(ast_tree)


def file_xml(src_path):
    with open(src_path) as src_file:
        src = src_file.read()
    return xml(src)


def module_xml(module_or_path):
    if isinstance(module_or_path, ModuleType):
        module = module_or_path
    else:
        module = import_module(module_or_path)
    return file_xml(module.__file__)


def source(src, xpath, until_xpath=None, dedent=True):
    xml_tree = xml(src)

    src_lines = src.split("\n")
    sources = []
    until_lineno = None
    if until_xpath is not None:
        until = xml_tree.xpath(until_xpath)
        assert len(until) == 1, "until_xpath must return only one result"
        until_lineno = int(until[0].attrib["lineno"]) - 1
    for node in xml_tree.xpath(xpath):
        try:
            start_lineno = int(node.attrib["lineno"]) - 1
            if until_lineno is not None:
                if until_lineno < start_lineno:
                    raise ValueError(
                        f"until_lineno ({until_lineno}) must not be lower than "
                        f"start_lineno ({start_lineno})"
                    )
                end_lineno = until_lineno
            else:
                end_lineno = int(node.attrib["end_lineno"])

            src = "\n".join(src_lines[start_lineno:end_lineno])
        except AttributeError:
            continue
        if dedent:
            src = textwrap.dedent(src)
        sources.append((src, node.attrib))

    return sources


def file_source(src_path, *args, **kwargs):
    with open(src_path) as src_file:
        src = src_file.read()
    return source(src, *args, **kwargs)


def module_source(module_or_path, *args, **kwargs):
    if isinstance(module_or_path, ModuleType):
        module = module_or_path
    else:
        module = import_module(module_or_path)
    return file_source(module.__file__, *args, **kwargs)
