class student:
    # constructor
    def __init__ (self,student_name,student_id):
        self.student_age= student_name
        self.student_id= student_id
    def study(self):
        print(f"Student P{self.student_age}{self.student_id}")

student1=student()
student2=student("002","maung maung")
print(student1.student_age)
student1.study()
student2.study()
print(student1)
