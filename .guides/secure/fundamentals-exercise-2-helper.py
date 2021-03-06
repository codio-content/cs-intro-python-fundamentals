import os
import subprocess
import sys

path = "code/fundamentals"
file = "exercise2.py"
student_code = os.path.join(path, file)

def check_variable(file):
  correct_var = False
  with open(file, "r") as code_to_check:
    for line in code_to_check.readlines():
      if "my_int" in line and "=" in line and "#" not in line and "'''" not in line and '"""' not in line:
        correct_var = True
  return correct_var

def check_output(file):
  student_output = subprocess.check_output(["python3", file]).rstrip()
  if student_output.decode("utf-8") == "3":
    return True
  else:
    return False

def print_var(file):
  print_variable = False
  with open(file, "r") as code_to_check:
    for line in code_to_check.readlines():
      if "print" in line and "my_int" in line and "#" not in line and "'''" not in line and '"""' not in line:
        print_variable = True
  return print_variable
  
if not check_variable(student_code):
  print("<h2>Test did not pass</h2>")
  print("Program did not declare the variable 'my_int'.")
  
if not check_output(student_code):
  print("<h2>Test did not pass</h2>")
  print("Program did not print '3'.")

if not print_var(student_code):
  print("<h2>Test did not pass</h2>")
  print("Program did not use 'my_int' with the 'print' statement.")

if check_variable(student_code) and check_output(student_code) and print_var(student_code):
  print("<h2>Test passed!</h2>")
  sys.exit(0)
else:
  sys.exit(1)