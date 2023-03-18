class Student:
    def __init__(self,name):
        self.__name=name
    def study(self,course):
        print(f"{self.__name}{course}")

student_obj=Student("John")
#print(student_obj.__name) #error
print(student_obj._Student__name)
student_obj.study("Python Programming")