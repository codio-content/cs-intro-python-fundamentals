----------

## Variable Names
Variables are used to store a value, and these values have a data type. Data types describe the kind of information that is being stored. Numbers are different than text, and integers are different from numbers with decimals. Variable declaration is when you create a variable and assign it a value. Enter the name of the variable you want to create, a `=` (called the assignment operator), and the value you want to store in the variable. You do not have to indicate the data type when declaring a variable. Use the `print` statement to see the value of the variable.

```python
my_variable = "Hello world"
print(my_variable)
```

{try it}(python3 code/fundamentals/playground-variables1.py 1)

Do not use quotation marks when printing a variable. Using quotation marks will print the variable name, not its value.

```python
my_variable = "Hello world"
print(my_variable)
print("my_variable")
```

{try it}(python3 code/fundamentals/playground-variables1.py 2)

## Variable Naming Rules
Here are the rules for declaring a variable.

|Rule|Correct|Incorrect|
|----|-------|---------|
|Start with a letter or underscore|`variable`, `_variable`|`1variable`|
|Remainder of variable name is letters, numbers, or underscores|`var_i_able`, `var1able`|`var-i-able`, `var!able`|
|Cannot use a Python keyword|`my_class`|`class`|
|Variables are case sensitive|`variable`, `Variable`, and `VARIABLE` are all different variables|

<details><summary><b>What are the Python key words?</b></summary><table><tr><th></th><th></th><th></th><th></th></tr><tr><td>and</td><td>as</td><td>assert</td><td>break</td></tr><tr><td>class</td><td>continue</td><td>def</td><td>del</td></tr><tr><td>elif</td><td>else</td><td>except</td><td>FALSE</td></tr><tr><td>finally</td><td>for</td><td>from</td><td>global</td></tr><tr><td>if</td><td>import</td><td>in</td><td>is</td></tr><tr><td>lamda</td><td>None</td><td>nonlocal</td><td>nont</td></tr><tr><td>or</td><td>pass</td><td>raise</td><td>return</td></tr><tr><td>TRUE</td><td>try</td><td>while</td><td>with</td></tr><tr><td>yield</td></tr></table></details>

{Check It!|assessment}(multiple-choice-928839981)
