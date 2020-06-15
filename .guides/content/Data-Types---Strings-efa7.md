----------

## Strings
A string is a collection of text, numbers, or symbols. Strings are always surrounded by quotation marks.

```python
string_variable = "This is a string"
second_string = 'This is a string also'
print(string_variable)
print(second_string)
```

{try it}(python3 code/fundamentals/playground-types-string.py 1)

|||challenge
## What happens if you:
* Mix single (`'`) and double (`"`) quotation marks?
<details><summary>**What happened?**</summary>This causes an error because Python requires that you be consistent with quotation marks. If you start with a single quote (`'`) you must end with a single quote. The same is true for double quotes (`"`). You may use either style of quotation marks, just be consistent.</details>
* Forget one of the quotation marks?
<details><summary>**What happened?**</summary>This causes an error because Python requires that quotation marks be used in pairs.</details>
* Forget both quotation marks?
<details><summary>**What happened?**</summary>This causes an error because to Python a string without quotes appears to be a series of variables that have not been defined.</details>

|||

{try it}(python3 code/fundamentals/playground-types-string.py 2)

Notice that when you print a string, the quotation marks are not printed.

{Check It!|assessment}(fill-in-the-blanks-3755866164)
