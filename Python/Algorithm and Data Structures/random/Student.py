import Person 

class Student(Person):
    
    def __init__(self,name,age,year):
        super().__init__(name,age)
        self.graduation = year

    def welcome(self):
        print("Welcome", self.name, self.age, "to the class of", self.graduation)

student1 = Student("Ram",17,2019)


student1.welcome()