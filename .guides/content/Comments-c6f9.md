----------------

## Comments

You may have wondered why a couple of lines of code are a different color (in the below example, light brown, but it depends on the Theme you have picked):

![.guides/img/comments](.guides/images/comments.png)

In Python, to write notes in code without effecting it's function we can use `#` to make a **comment**.

{Try it}(python3 code/fundamentals/comments.py 1)

Comments can also be used to help you fix your code. You can "comment out" lines of code that are not working or you suspect are causing problems.

|||challenge
## What happens if you:
* Change `print("Red")` to `prnt("Red")`?
* Comment out the line of code with the typo?

|||

{Try it}(python3 code/fundamentals/comments.py 2)

## Comment Blocks

To make a multi-line comment you can either combine the single line characters `#` or wrap the set of lines in triple quotes (`'''`). 

```python
'''
This is a multi-line comment
You can then easily end the comment with a triple quote (see below)
'''

#You can also do a multi-line comment
#like this!
    
print("Notice code that runs is not the same color as single-line comments");
print("This feature is called syntax highlighting");
print("It is a common feature of IDEs");
```

{Try it}(python3 code/fundamentals/comments.py 3)

The syntax highlighting is different for comments with `#`and comments with `'''`. That is because the triple quotation marks are also used for multi-line strings (see the Strings lesson). When a multi-line string is by itself (no `print` statement), then Python treats it as multiline comment.

<details><summary>**What is an IDE?**</summary> <blockquote cite="https://simple.wikipedia.org/wiki/Integrated_development_environment">An integrated development environment, or IDE, is a computer program that makes it easier to write other computer programs. They are used by computer programmers to edit source code, and can be easier to use than other text editors for new programmers. They can have compilers so programmers don't have to open other programs to compile the source code. They also often have syntax highlighting. ... It also may have predictive coding that can finish lines with syntax such as brackets or semicolons and can suggest variables to be used. It also may have debuggers that can step through lines, take breaks and inspect variables. <br> <br> <b>Source: Simple Wikipedia </b></blockquote></details>