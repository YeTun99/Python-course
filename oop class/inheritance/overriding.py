class Parent:
    def print_self(self):
        print("Parent")
    
class Child(Parent):
    def print_self(self):
        print("Child")
    
child_instance=Child()
child_instance.print_self()

#parent class ko overide lote pee pyan yayyy