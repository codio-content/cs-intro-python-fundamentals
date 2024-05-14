---

## Assigning Value
The value stored in a variable can change. Use the assignment operator to give a variable a new value.

![The image shows two lines of code both starting with the variable "my_variable" and the assignment operator. The first line is "my_variable = 'Hello world'" with the red comment that here we declare the variable and assign a value. The second line is "my_variable = 'Goodbye world'" with the blue comment that now we overwrite the old value and assign a new value.](.guides/images/variable-assignment.png)

The image above is **not** declaring two variables called `my_variable`. The first line declares the variable because this is the first instance. The second line overwrites `Hello world` with `Goodbye world`. Enter the code below and see the results of the `print` commands. Use the code visualizer to see how the value of `my_variable` changes.

```python
my_variable = "Hello world"
print(my_variable)
my_variable = "Goodbye world"
print(my_variable)
```

[Code Visualizer](open_tutor code/fundamentals/playground-assign-value.py)
{try it}(python3 code/fundamentals/playground-assign-value.py 1)

{Check It!|assessment}(parsons-puzzle-2757362999)
