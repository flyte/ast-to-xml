# ast-to-xml

Converts a Python abstract source tree (AST) to an XML representation. Uses lxml to enable full XPath searching.

## Installation

```bash
pip install ast-to-xml
```

## Usage

Given the following code as `code.py`:

```python
SOME_CONSTANT = "some constant"

def a_function(arg1, arg2, kwarg1=None):
    def a_subfunction(arg1, kwarg1=None):
        print("Hello, World!")

class SomeClass:
    def __init__(self, arg1):
        self.arg1 = arg1

    def a_method(self, arg1, kwarg1=None):
        pass
```

Parse the code and convert to XML:

```python
import ast

from ast_to_xml import visit_node


with open("code.py") as code_file:
    ast_tree = ast.parse(code_file.read())

xml_tree = visit_node(ast_tree)
```

<details>
  <summary>Click to expand rendered XML</summary>

```xml
<Module>
  <body>
    <Assign lineno="3" col_offset="0" end_lineno="3" end_col_offset="31">
      <targets>
        <Name id="SOME_CONSTANT" lineno="3" col_offset="0" end_lineno="3" end_col_offset="13">
          <ctx>
            <Store/>
          </ctx>
        </Name>
      </targets>
      <value>
        <Constant lineno="3" col_offset="16" end_lineno="3" end_col_offset="31">
          <value type="str">some constant</value>
          <kind type="NoneType">None</kind>
        </Constant>
      </value>
      <type_comment type="NoneType">None</type_comment>
    </Assign>
    <FunctionDef name="a_function" lineno="5" col_offset="0" end_lineno="7" end_col_offset="30">
      <args>
        <arguments>
          <posonlyargs/>
          <args>
            <arg lineno="5" col_offset="15" end_lineno="5" end_col_offset="19">
              <arg type="str">arg1</arg>
              <annotation type="NoneType">None</annotation>
              <type_comment type="NoneType">None</type_comment>
            </arg>
            <arg lineno="5" col_offset="21" end_lineno="5" end_col_offset="25">
              <arg type="str">arg2</arg>
              <annotation type="NoneType">None</annotation>
              <type_comment type="NoneType">None</type_comment>
            </arg>
            <arg lineno="5" col_offset="27" end_lineno="5" end_col_offset="33">
              <arg type="str">kwarg1</arg>
              <annotation type="NoneType">None</annotation>
              <type_comment type="NoneType">None</type_comment>
            </arg>
          </args>
          <vararg type="NoneType">None</vararg>
          <kwonlyargs/>
          <kw_defaults/>
          <kwarg type="NoneType">None</kwarg>
          <defaults>
            <Constant lineno="5" col_offset="34" end_lineno="5" end_col_offset="38">
              <value type="NoneType">None</value>
              <kind type="NoneType">None</kind>
            </Constant>
          </defaults>
        </arguments>
      </args>
      <body>
        <FunctionDef name="a_subfunction" lineno="6" col_offset="4" end_lineno="7" end_col_offset="30">
          <args>
            <arguments>
              <posonlyargs/>
              <args>
                <arg lineno="6" col_offset="22" end_lineno="6" end_col_offset="26">
                  <arg type="str">arg1</arg>
                  <annotation type="NoneType">None</annotation>
                  <type_comment type="NoneType">None</type_comment>
                </arg>
                <arg lineno="6" col_offset="28" end_lineno="6" end_col_offset="34">
                  <arg type="str">kwarg1</arg>
                  <annotation type="NoneType">None</annotation>
                  <type_comment type="NoneType">None</type_comment>
                </arg>
              </args>
              <vararg type="NoneType">None</vararg>
              <kwonlyargs/>
              <kw_defaults/>
              <kwarg type="NoneType">None</kwarg>
              <defaults>
                <Constant lineno="6" col_offset="35" end_lineno="6" end_col_offset="39">
                  <value type="NoneType">None</value>
                  <kind type="NoneType">None</kind>
                </Constant>
              </defaults>
            </arguments>
          </args>
          <body>
            <Expr lineno="7" col_offset="8" end_lineno="7" end_col_offset="30">
              <value>
                <Call lineno="7" col_offset="8" end_lineno="7" end_col_offset="30">
                  <func>
                    <Name id="print" lineno="7" col_offset="8" end_lineno="7" end_col_offset="13">
                      <ctx>
                        <Load/>
                      </ctx>
                    </Name>
                  </func>
                  <args>
                    <Constant lineno="7" col_offset="14" end_lineno="7" end_col_offset="29">
                      <value type="str">Hello, World!</value>
                      <kind type="NoneType">None</kind>
                    </Constant>
                  </args>
                  <keywords/>
                </Call>
              </value>
            </Expr>
          </body>
          <decorator_list/>
          <returns type="NoneType">None</returns>
          <type_comment type="NoneType">None</type_comment>
        </FunctionDef>
      </body>
      <decorator_list/>
      <returns type="NoneType">None</returns>
      <type_comment type="NoneType">None</type_comment>
    </FunctionDef>
    <ClassDef name="SomeClass" lineno="9" col_offset="0" end_lineno="14" end_col_offset="12">
      <bases/>
      <keywords/>
      <body>
        <FunctionDef name="__init__" lineno="10" col_offset="4" end_lineno="11" end_col_offset="24">
          <args>
            <arguments>
              <posonlyargs/>
              <args>
                <arg lineno="10" col_offset="17" end_lineno="10" end_col_offset="21">
                  <arg type="str">self</arg>
                  <annotation type="NoneType">None</annotation>
                  <type_comment type="NoneType">None</type_comment>
                </arg>
                <arg lineno="10" col_offset="23" end_lineno="10" end_col_offset="27">
                  <arg type="str">arg1</arg>
                  <annotation type="NoneType">None</annotation>
                  <type_comment type="NoneType">None</type_comment>
                </arg>
              </args>
              <vararg type="NoneType">None</vararg>
              <kwonlyargs/>
              <kw_defaults/>
              <kwarg type="NoneType">None</kwarg>
              <defaults/>
            </arguments>
          </args>
          <body>
            <Assign lineno="11" col_offset="8" end_lineno="11" end_col_offset="24">
              <targets>
                <Attribute lineno="11" col_offset="8" end_lineno="11" end_col_offset="17">
                  <value>
                    <Name id="self" lineno="11" col_offset="8" end_lineno="11" end_col_offset="12">
                      <ctx>
                        <Load/>
                      </ctx>
                    </Name>
                  </value>
                  <attr type="str">arg1</attr>
                  <ctx>
                    <Store/>
                  </ctx>
                </Attribute>
              </targets>
              <value>
                <Name id="arg1" lineno="11" col_offset="20" end_lineno="11" end_col_offset="24">
                  <ctx>
                    <Load/>
                  </ctx>
                </Name>
              </value>
              <type_comment type="NoneType">None</type_comment>
            </Assign>
          </body>
          <decorator_list/>
          <returns type="NoneType">None</returns>
          <type_comment type="NoneType">None</type_comment>
        </FunctionDef>
        <FunctionDef name="a_method" lineno="13" col_offset="4" end_lineno="14" end_col_offset="12">
          <args>
            <arguments>
              <posonlyargs/>
              <args>
                <arg lineno="13" col_offset="17" end_lineno="13" end_col_offset="21">
                  <arg type="str">self</arg>
                  <annotation type="NoneType">None</annotation>
                  <type_comment type="NoneType">None</type_comment>
                </arg>
                <arg lineno="13" col_offset="23" end_lineno="13" end_col_offset="27">
                  <arg type="str">arg1</arg>
                  <annotation type="NoneType">None</annotation>
                  <type_comment type="NoneType">None</type_comment>
                </arg>
                <arg lineno="13" col_offset="29" end_lineno="13" end_col_offset="35">
                  <arg type="str">kwarg1</arg>
                  <annotation type="NoneType">None</annotation>
                  <type_comment type="NoneType">None</type_comment>
                </arg>
              </args>
              <vararg type="NoneType">None</vararg>
              <kwonlyargs/>
              <kw_defaults/>
              <kwarg type="NoneType">None</kwarg>
              <defaults>
                <Constant lineno="13" col_offset="36" end_lineno="13" end_col_offset="40">
                  <value type="NoneType">None</value>
                  <kind type="NoneType">None</kind>
                </Constant>
              </defaults>
            </arguments>
          </args>
          <body>
            <Pass lineno="14" col_offset="8" end_lineno="14" end_col_offset="12"/>
          </body>
          <decorator_list/>
          <returns type="NoneType">None</returns>
          <type_comment type="NoneType">None</type_comment>
        </FunctionDef>
      </body>
      <decorator_list/>
    </ClassDef>
  </body>
  <type_ignores/>
</Module>
```
</details>

You may now query `xml_tree` with xpath to get details of various sections of the Python source code:

```python
>>> # All function definitions
>>> xml_tree.xpath("//FunctionDef")
[<Element FunctionDef at 0x7f89780e41c0>, <Element FunctionDef at 0x7f89780e42c0>, <Element FunctionDef at 0x7f89780e4280>, <Element FunctionDef at 0x7f89780e4100>]

>>> # Get the line numbers of the `s_subfunction` function
>>> xml_tree.xpath("./body/FunctionDef[@name='a_function']/body/FunctionDef[@name='a_subfunction']")[0].attrib
{'name': 'a_subfunction', 'lineno': '6', 'col_offset': '4', 'end_lineno': '7', 'end_col_offset': '30'}

>>> # The above can be made simpler, since there's only one function called `a_subfunction`:
>>> xml_tree.xpath("//FunctionDef[@name='a_subfunction']")[0].attrib
{'name': 'a_subfunction', 'lineno': '6', 'col_offset': '4', 'end_lineno': '7', 'end_col_offset': '30'}

>>> # Get all of the methods within `SomeClass`:
>>> xml_tree.xpath("./body/ClassDef[@name='SomeClass']//FunctionDef")
[<Element FunctionDef at 0x7f89785fcd80>, <Element FunctionDef at 0x7f89780e4200>]
```
