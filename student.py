class Student:
    def printInfo(self):
        print(f"Fullname {self.name}")
st1 =Student()
st1.name="Duyet"
st1.printInfo()
del st1.name
del st1

class Dog:
    def __init__(self,name="",age=0):
        self.name=name
        self.age=age
    def say(self):
        print(f"GO GO{self.name}")
mydog= Dog()
mydog.say()
mydog.name="DOGGO"
mydog.say()

class Car:
    def __init__(self,year,make,model):
        self.year=year
        self.make=make
        self.model=model
    def old(self):
        return 2022-self.year
mycar =Car(2021,"Mazda","Mazda -2 sport")
print("My car is {}years old ".format(mycar.old()))

class Person:
    def __init__(self,lname,fname):
        self.lastname=lname
        self.firstname =fname
    def printname(self):
        print(self.firstname,self.lastname)
class Student(Person):
    def printage(self):
        print(self.age)
st=Student("Bui","Duyet")
st.printname()
st.age=20
st.printage()
