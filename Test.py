#!/usr/bin/env python3

from student import Student

Student1 = Student('John','013454900')

print(Student1.name)
print(Student1.number)
print(Student1.courses)
Student1.displayStudent()

student2 = Student('Jessica', '023384103')

print(student2.name)
print(student2.number)
print(student2.courses)
student2.displayStudent()

Student1.addGrade('uli101',4.0)
Student1.addGrade('ops245', 3.5)
Student1.addGrade('ops445', 3.0)

student2.addGrade('ipc144', 4.0)
student2.addGrade('cpp244', 4.0)

print(Student1.name)
print(Student1.courses)
print(student2.name)
print(student2.courses)
 

print(Student1.name)
Student1.name = 'Jack'
print(Student1.name)
print(len(Student1.name))
