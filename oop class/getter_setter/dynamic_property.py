class Student:
    __slots__=('name','age')
    def __init__(self,name):
        self.name=name

student_obj=Student('John')
student_obj.age=22 #slots property htae ma htar yin let khan lox maya
print(student_obj.age)