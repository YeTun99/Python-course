class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __lt__(self,other):
        return self.age < other.age
    
people=[
    Person("John",20), #class ko pyan call
    Person("KOKO",30),
    Person("Aries",40)

]

sorted_people=sorted(people)
for person in sorted_people:
    print(person.name,person.age)