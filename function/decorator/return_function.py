def hello():
    def greet():
        return ("This is greet inside hello")
    def welcome():
        return "This is welcome inside hello"
    return greet,welcome

my_func=hello
print(my_func())
print(type(my_func()))
print(my_func()[0]())
print(my_func()[1]())