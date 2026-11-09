class Employee:
    def do(self):
        print("Employee works")
  
class Student:
    def do(self):
        print("Student studies")
  
  
# class WorkingStudent(Student,Employee):
class WorkingStudent(Employee, Student):
    pass
 
tom = WorkingStudent()
tom.do()     # ?

# При необходимости мы можем программным образом посмотреть очередность применения функционала базовых классов.
# Для этого применяется атрибут __mro__, либо метод mro()

print(WorkingStudent.__mro__)
print(WorkingStudent.mro())