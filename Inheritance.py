 ## Inheritance
 
 # Single Inheritance

class Car():
    def Car_Start(self):
        print("Car is starting")

    def Car_Stop(self):
        print("Car is stoping")

class Toyota(Car):
    def __init__(self,acc,cluth,break1):
        self.acc= acc
        self.cluth= cluth
        self.break1 = break1

    def automated(self):
        print("Automating car")


t1 = Toyota(50,"Press_cluth","Press_break")
print(t1.acc,t1.cluth,t1.break1)
print(t1.automated())
print(t1.Car_Start())
print(t1.Car_Stop())


# Multilevel Inheritance

class Animal():
    def animal(self):
        print("Animal live in Forest")
    def Run(self):
        print("Some animal is running fast")

class cat(Animal):
    def Meow(self):
        print("Cat is meowing")

    def Dangerous(self):
        print("Cat is dangerous for mouse")

class Dog(cat):
    def Bark(self):
        print("Dog is barking")

    def Protect(self):
        print("Dog is Protecing Home")

d1 = Dog()
print(d1.Bark())
print(d1.Protect())
print(d1.animal())
print(d1.Run())
print(d1.Meow())


# Multiple Inheritance


class A:
    varA = "This is A method"
    
class B:
    varB ="This is B method"

class C(A,B):
    varC = "This is C method"




c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)

    





class Car():
    def Car_Start(self):
        print("Car is starting")

    def Car_Stop(self):
        print("Car is stoping")


# Super 

class Toyota(Car):
    def __init__(self,acc,cluth,break1):
        self.acc= acc
        self.cluth= cluth
        self.break1 = break1

    def automated(self):
        print("Automating car")

class Dragon(Toyota):
    def __init__(self,acc,cluth,break1,Loca_shower,Weather_Pre):
        self.Loca_shower = Loca_shower
        self.Weather_Pre = Weather_Pre
        super().__init__(acc,cluth,break1)
        #super().automated()



    def fully_ventilated(self):
        print("Dragon car is fully ventilated")


d1 = Dragon(50,"Press_cluth","Press_break","Kolhapur","Rainy")
print(d1.acc,d1.cluth,d1.break1,d1.Loca_shower,d1.Weather_Pre)  
print(d1.fully_ventilated()) 
print(d1.automated())
print(d1.Car_Start())
print(d1.Car_Stop())




# Decorators
# static method(No argument),class method(cls), instance method(self) '

class Car:
    def __init__(self,type1):
        self.type1 = type1
    
    @staticmethod                          # Static method
    def Start():
        print("Car start")
    @staticmethod
    def Stop():
        print("Car Stop")
    def Run(self):
        print("Car is running")            # Instance Method
class Toyota(Car):
    def __init__(self,name,type1):
        self.name =name
        super().__init__(type1)

t1 = Toyota("Fortuner","Petrol")
print(t1.name,t1.type1)
print(t1.Start())
print(t1.Stop())
print(t1.Run()) 


#@ property

class Student:
    def __init__(self,phy,che,math):
     self.phy =phy
     self.che =che
     self.math = math 
     #self.percentage = str((phy+che+math)/3)+"%"

    #def show_Pecentage(self):
       # self.percentage = str((self.phy+self.che+self.math)/3)+"%"
       # print(self.percentage)
    
    @property                                        #decorator
    def cal_percentage(self):
        return str((self.phy+self.che+self.math)/3) + "%"

    
         
        

s1 = Student(96,92,90)
print(s1.phy,s1.che,s1.math)
#print(s1.percentage)
#print(s1.show_Pecentage())


s1.phy = 70
print(s1.phy,s1.che,s1.math)
#print(s1.show_Pecentage())
s1.che = 80
print(s1.phy,s1.che,s1.math)
#print(s1.show_Pecentage())
print(s1.cal_percentage)



s1.math =78
print(s1.cal_percentage)


class Person:
     name = 'anonymous'
     @classmethod
     def changeName(cls,name):
            cls.name =name

p1 =Person()
print(p1.name)
print(p1.changeName("Pavan Jadhav"))
print(p1.name)



# Operator Overloading


class Complex_No:
    def __init__(self,real,img):
        self.real =real
        self.img =img

    def show_Number(self):
        print(self.real,"i+",self.img,"j")

    def __add__(num1,num2):
        newReal = num1.real+num2.real
        newImg = num1.img+num2.img
        return Complex_No(newReal,newImg)
        



c1 = Complex_No(5,3)
print(c1.show_Number())

c2 =Complex_No(6,3)
print(c2.show_Number())

#num3 = c1.add(c2)
#print(num3.show_Number())

num3 = c1 +c2
print(num3.show_Number())




'''Define a circle class to create a circle with radius r using the construtor ,Define an Area() method of the class which calculate area of the class 
define perimeter() method of the class which allow you to calculate perimeter of the circle'''



class Circle:
    def __init__(self,radius):
        self.radius= radius

    def Area(self):
        area = 3.14 *( self.radius**2)
        print(area)

    def Perimeter(self):
        p_area = 2*3.14*(self.radius**2)
        print(p_area)

c1 = Circle(6)
print(c1.Area())

print(c1.Perimeter())   
