"""funtion without name (Lambda expression)"""
# s=lambda a,b : a+b
# x=s(10,20)
# print(x)

# r=(lambda a,b:a+b)(10,30)
# print("sum is:",r)

"""Create a lamda expression to find greater between two numbers"""

# r=(lambda a,b: a if a>b else b)(10,15)
# print("greater is:",r)

"""Recursion in lambda expression"""
# s=(lambda a:1 if a==0 else a*s(a-1))
# r=s(5)
#
# print('factorial is:',r)

# def fact(a):
#     if a==0:
#         return 1
#     return a*fact(a-1)
#
# r=fact(5)
# print('factorail is:',r)

"""Function decorators """
"""if someone mark is greater than 80 than display congratulations message using decorators"""
# def decor_result(result):
#     def congratulations(marks):
#         for m in marks:
#             if m>=80:
#                 print('congratulations')
#             else:
#                 result(marks)
#     return congratulations
#
# @decor_result
# def result(marks):
#     for m in marks:
#         if m>=33:
#             pass
#         else:
#             print('fail')
#             break
#     else:
#         print('pass')
#
# result([50,60,70,80,65])


# def is_called():
#     def is_returned():
#         print("Hello")
#     return is_returned
#
#
# new = is_called()
#
# new()

"""Classes"""

# class Myclass:
#     x=5
#
# p1=Myclass()
# print(p1.x)


# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#
# p1=Person('suprit',24)
# p2=Person('shipu',18)
# print(p1.name)
# print(p1.age)
# print(p2.name)
# print(p2.age)


# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age=age
#
#     def myfunc(self):
#         print("Hello my name is "+self.name)
#
# p1=Person('suprit',24)
# p1.myfunc()

"""The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:"""

# class Person:
#   def __init__(mysillyobject, name, age):
#     mysillyobject.name = name
#     mysillyobject.age = age
#
#   def myfunc(abc):
#     print("Hello my name is " + abc.name)
#
# p1 = Person("John", 36)
# p1.myfunc()

"""Modify object properties"""
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#   def myfunc(self):
#     print("Hello my name is " + self.name)
#
# p1 = Person("John", 36)
# p1.age = 40
# print(p1.age)

"""Delete object properties"""
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#   def myfunc(self):
#     print("Hello my name is " + self.name)
#
# p1 = Person("John", 36)
# del p1.age
# print(p1.age)

"""Delete object by keyword"""
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#   def myfunc(self):
#     print("Hello my name is " + self.name)
#
# p1 = Person("John", 36)
# del p1
# print(p1)


"""class defination can't be empty, but if you for some reason have a class defination with no content,put the pass statement to avoid getting error"""


class Person:
    pass


# having an empty class definition like this, would raise an error without the pass statement


# class Account:
#     def __init__(self,a,b):
#         self.accn=a
#         self.blnc=b
#     def f1(self,a,b):
#         self.accn=a
#         self.blnc=b
#
# p1=Account('xxxx568',5000)
# p1.f1('xxx254',9000)
# print(p1.accn)
# print(p1.blnc)
# print(p1.__dict__)



# class Test:
#     a=10            #static variable
#     def __init__(self):
#         self.x=1    #Instance variable and self refering current object
#         Test.b=20   #static varibale
#
#     def f1(self):   #Instance member function
#         self.x=2    #Instance variable
#         Test.c=30   #static varibale
#
#     @staticmethod   # @ is annotation and @ declaration is compulsory before defining static method
#     def f2():       #static method or static member function
#         Test.d=40   #static varibale
#
#     @classmethod
#     def f3(cls):
#         cls         #cls is a class object
#         cls.e=50    #static varibale
#         cls.f=100   #static varibale
#
#         Test.g=50   #static variable
#
# print(Test.__dict__)



# y=10
# def f1():
#     y=5 #local variable
#     print('local variable inside function-->',y)
#     print('global variable inside function--->',globals()['y'])
#
# f1()
# print('outside the function-->',y)


# What is inheritance
"""Defining a new class with the help of old class is called inheritance"""
# synatax of inheritance


# Parent class and child class function and argument matches means overhiding
# function match but argument did not match means hiding

"""Create a class named Person, with firstname and lastname properties, and a printname method:
Create a class named Student, which will inherit the properties and methods from the Person class:"""


# class Person:
#     def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lasttname=lname
#
#     def printname(self):
#         print(self.firstname)
#         print(self.lasttname)
#
# class Student(Person):
#     pass
#
# p1=Student('Tarun','Tirkey')
# p1.printname()


# if both classes have __init__function is called data-overhiding

# class Person:
#     def __init__(self,n,a):
#         self.name=n
#         self.age=a
#
#     def showname(self):
#         print('name: ',self.name)
#     def showage(self):
#         print('age: ',self.age)
#
# class Student(Person):
#     def __init__(self,r,n,a):
#         super().__init__(n,a)
#         self.rollno=r
#
#     def printroll(self):
#         print('roll no: ',self.rollno)
#
# s1=Student(100,'Amit',15)
# s1.printroll()
# s1.showname()
# s1.showage()


# Static member variable name conflict

# class Base:
#     x=11
#     def __init__(self):
#         self.a=10
#         Base.x=13
#     def showcase(self):
#         print('base a: ',self.a)
#
# class Derived:
#     x=12
#     def __init__(self):
#         super().__init__()
#         self.a=20
#     def show(self):
#         print(Base.x,Derived.x)
#     def showderived(self):
#         print('Derived a:',self.a)
#
# obj=Derived()
# print(Derived.x)
# obj.show()


# Name conflict between static and instance members
# How to access instance and static variable


# class Base:
#     x=10
#     def __init__(self):
#         self.x=20
# class Derived(Base):
#     def __init__(self):
#         super().__init__()
#
# obj=Derived()
# print(obj.x)
# print(Derived.x)


# How to access base class members in derived class

# Instance member variable of base class in derived class

# class Base:
#     def __init__(self):
#         self.a=10
# class Derived(Base):
#     def __init__(self):
#         super().__init__()
#     def f1(self):
#         print(self.a)
#
# obj=Derived()
# obj.f1()

# Static member variables of base class in derived class

# class Base:
#     x=1     #static member variable
#     def __init__(self):
#         self.a=10
#
# class Derived(Base):
#     def __init__(self):
#         super().__init__()
#     @staticmethod
#     def f1():
#         print(Derived.x)
#
# Derived.f1()


# Instance member function of base class in derived class

# class Base:
#     def __init__(self):
#         self.a=10
#     def basefunction(self):
#         print('Base instance funtion a: ',self.a)
# class Derived(Base):
#     def __init__(self):
#         super().__init__()
#     def f1(self):
#         super().basefunction()
#
# obj=Derived()
# obj.f1()


# Static member funtion of base class in derived class
# class Base:
#     x=11
#     def __init__(self):
#         self.a=10
#     @staticmethod
#     def basefuntion():
#         print('Base static funtion x: ',Base.x)
#
# class Derived:
#     def __init__(self):
#         super().__init__()
#     @staticmethod
#     def f1():
#         Base.basefuntion()
#
# obj=Derived()
# obj.f1()

# Multiple Inheritance
# If a class derived from more than one class it is known as multiple inheritance

# class Person:
#     def __init__(self,n,a):
#         self.name=n
#         self.age=a
# class Student(Person):
#     def __init__(self,n,a,r):
#         self.rollno=r
#         Person.__init__(self,n,a)
#
# class Teacher(Person):
#     def __init__(self,n,a,s,sub):
#         self.salary=s
#         self.subject=sub
#         Person.__init__(self, n, a)
# class BrightStudent(Student,Teacher):
#     def __init__(self,n,a,r,s,sub,p):
#         self.points=p
#         Student.__init__(self,n,a,r)
#         Teacher.__init__(self,n,a,s,sub)
#
# obj=BrightStudent('Suprit',24,101,14500,'computer',7)
# print(obj.__dict__)


# How to make a generator to produce N prime numbers ?
# def isPrime(num):
#     for i in range(2,num):
#         if num%i==0:
#             return False
#     return True
#
# def primeGenerator(n):
#     num=2
#     while n:    #Loop will run till n value will be 0
#         if isPrime(num):
#             yield   num        #we use yield in generotor , It pause the function so function will resume after this line if function call again
#             n=n-1
#         num+=1
#     return
#
# it=primeGenerator(10)

# for e in it:             #Here generator is returning iterate elements so we have use for loop here
#     print(e,end=' ')

# How to implement variable length arguments in Python function ?

# def average(*t):
#   avg=sum(t)/len(t)
#   print('Average is ',avg)
# average(10,15,18)
# average(10,15,18,22,25,56,44)
# average(10,20)



f = lambda n: 1 if n==0 else n*f(n-1)
print(f(5))
