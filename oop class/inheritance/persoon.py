class Person:
    def __init__(self,name,age):
        self.name=name
        self.age= age
    
    def eat(self):
        print(f"{self.name} is eating")
    
class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def study(self,course_name):
        print(f"{self.name} is studying {course_name}")
    
class Teacher(Person):
    def __init__(self, name, age,title):
        super().__init__(name, age)
        self.title=title

    def teach(self,course):
        print(f"{self.name}{self.title} is teaching {course}")

stu1=Student("John",30)
stu1.study("Python")

teacher1=Teacher("Nathen",50,"Professor")
teacher1.teach("Python")