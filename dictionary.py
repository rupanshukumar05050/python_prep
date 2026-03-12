students = {}

no_of_students = int(input("Enter the Number of student: "))

for i in range(no_of_students):
  roll_no = int(input("Enter your Roll no: ")
  name_ = input("Enter your Name: ")
  age = int(input("Enter your Age: ")
  course = input("Enter your Course: ")

       students[roll_no] = {
         "Name" : name_,
         "Age" : age,
         "Course" : course
       }
print("\nStudent Records:")
for l in students:
  print(l, "i", student[l])
