from student import Student 

student1 = Student("Jim", 3)
student2 = Student("Felix", 2)
student3 = Student("Jim", 1)

print(student1 > student2)
print(student1 < student2)
print(student1 == student2)
print(student1 == student3)
print(student1 >= student3)
print(student1 <= student2)
