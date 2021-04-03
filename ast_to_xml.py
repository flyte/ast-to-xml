import ast

from lxml import etree as ET

ATTRS = ("id", "name", "lineno", "col_offset", "end_lineno", "end_col_offset")


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
