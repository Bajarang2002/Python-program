
class Employee:
    def __init__(self,emp_id,emp_name,salary,age ):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.salary = salary
        self.age = age

e1 = Employee(101,"Aditya",50000,25)
print(e1.emp_id,e1.emp_name,e1.salary,e1.age)
e2 = Employee(102,"Ashu",70000,26)
print(e2.emp_id,e2.emp_name,e2.salary,e2.age)


# Delecting object and object properties


del e1.emp_id
del e1




# Private Member

class Student:
    def __init__(self,id,name,class1,password):
        self.id = id
        self.name = name
        self.class1 = class1
        self.__Stu_password = password

    def show_password(self):
         print(self.__Stu_password)

    def __hello(self):
        print("Hello Friends")

    def welcome(self):
         self.__hello()


s1 = Student(1,'Pavan',"Fourth",'ABC@emal')
print(s1.id,s1.name,s1.class1)
print(s1.show_password())
print(s1.welcome())









