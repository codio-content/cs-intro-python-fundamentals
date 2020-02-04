import os
import subprocess
import sys

path = "code/fundamentals"
file = "exercise4.py"
student_code = os.path.join(path, file)

def check_variable(file):
  correct_var = False
  with open(file, "r") as code_to_check:
    for line in code_to_check.readlines():
      if line.find("my_float") != -1:
        correct_var = True
    
  return correct_var

def check_output(file):
  student_output = subprocess.check_output(["python3", file]).rstrip()
  if student_output.decode("utf-8") == "3.0":
    return True
  else:
    return False

def print_var(file):
  print_variable = False
  with open(file, "r") as code_to_check:
    for line in code_to_check.readlines():
      if "print(my_float)" in line:
        print_variable = True
  return print_variable
  
if not check_variable(student_code):
  print("<h2>Test did not pass</h2>")
  print("Program did not use the variable 'my_float'.")
  
if not check_output(student_code):
  print("<h2>Test did not pass</h2>")
  print("Program did not print '3.0'.")

if not print_var(student_code):
  print("<h2>Test did not pass</h2>")
  print("Program did not use 'my_float' with the 'print' statement.")

if check_variable(student_code) and check_output(student_code) and print_var(student_code):
  print("<h2>Test passed!</h2>")
  sys.exit(0)
else:
  sys.exit(1)