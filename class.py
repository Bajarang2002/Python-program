
# Class

class Student:
        name = "Ram"
        age = 25
        class_1 = "Final_Year"
        department="CSE"

s1 = Student()   #Object
print(s1.name)
print(s1.age)
print(s1.class_1)
print(s1.department)



# Construtor

class Employee:
    name = "Pavan"            # Class attribute
    def __init__(self,e_name,age,salary,department):
        self.e_name = e_name               # Instance Attribute
        self.age = age
        self.salary = salary
        self.department = department

e1 = Employee("Bajarang",25,56000,"IT")
print(e1.name)
print(e1.e_name,e1.age,e1.salary,e1.department)


# Method


class Employee:       
    def __init__(self,e_name,age,salary,department):
        self.e_name = e_name              
        self.age = age
        self.salary = salary
        self.department = department

    def Hello(self):
        print("Hello Friends")

    def Welcome(self):
        print("Welcome to our project")

e1 = Employee("Bajarang",25,56000,"IT")
print(e1.e_name,e1.age,e1.salary,e1.department)
print( e1.Hello())
print(e1.Welcome())


# Static Method


class Student:
    @staticmethod
    def College():
        print("ABC College")

s1 = Student()
print(s1.College())


# Create student class and takes names And marks of 3 subject as argument in construtor .Then Create a method to
#to print average

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum=0
        for i in self.marks:
            sum +=i
        avg = sum/3
        print("Hi",self.name,"Your average score is",avg)


s1 = Student("Sid",[96,85,88])
print(s1.get_avg())


# Create Acccount class with 2 attribute - balace & account no. Create methods for debit,credit & printing the balance


class Account:
    def __init__(self,account_no,balance):
        self.account_no =account_no 
        self.balance=balance

    def Debit(self,amount):
        self.balance -=amount
        print("Your account has been debited",amount,"Rs")
        print("Total balance is:",self.get_balance())

    def Credit(self,amount):
        self.balance+=amount
        print("Your account has been credited",amount,"Rs")
        print("Total balance is:",self.get_balance())

    def get_balance(self):
        return self.balance



a1 = Account(101,50000)
print(a1.Debit(5000))
print(a1.Credit(2000))

print(a1.Credit(70000))







