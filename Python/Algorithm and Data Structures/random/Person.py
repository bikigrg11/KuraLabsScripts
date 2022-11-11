'''
Learning how to use classes and Objects
'''

class Person:
    def __init__(self,name ,age):
        self.name = name
        self.age = age
    
    def getName(self):
        print(self.name)
    
    def getAge(self):
        print(self.age)
    

# father = Person("John",25)
# father.getAge()

class Student(Person):
    def __init__(self,name,age,year):
        super().__init__(name,age)
        self.graduation = year

    def welcome(self):
        print("Welcome", self.name, self.age, "to the class of", self.graduation)

student1 = Student("Ram",17,2019)


student1.welcome()