class Student:
    def __init__(self,name):
        self.student_name=name
    
    @property
    def student_name(self): #self.student_nae fucntion field name tu pay ya ml
        """Getter method"""
        return self._student_name+ " of GCA"
    
    @student_name.setter
    def student_name(self,name):
        """Setter Method"""
        if not name:
            raise ValueError("Missing Name")
        self._student_name=name
    
    def study(self):
        print(f"{self.student_name} is studying Python Course")

#student1=Student('') #Raise Value Error
student1=Student('John')
student1.student_name=""
print(student1.student_age)