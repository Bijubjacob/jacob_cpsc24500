from datetime import datetime

name = input("Enter your name: ")
age = 25
gpa = 3.5
is_student = True

print("***********************")
print(f" Welcome, {name}! ")
print("***********************")

now = datetime.now()
print(f"Current date and time: {now}")

print(f"Age: {age}, GPA: {gpa}, Student: {is_student}")