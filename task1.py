students = {

    'Alice' :85,
    'mark':43,
    'jack':88
}

userinput =input("enter the student name :")

if userinput in students:
  print(f"{userinput} marks :",students[userinput])
else:
    print(" student not found.")