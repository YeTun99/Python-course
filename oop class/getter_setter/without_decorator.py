#private,protected,public private ka only protected ka choose htar tae luu thone
class Student:
    def __init__(self,name):
        if not name:
            raise ValueError("Missing Name")
        self.name=name
    
    def study(self):
        print(f"{self.name} is studying Python Course")
    
#student_obj= Student('')
student_obj=Student("John")
student_obj.name=""
print(student_obj.study())