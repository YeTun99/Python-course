#positional argument def function_name(num1,num2) function_name(1,2)
#keyword argument def function_name(num2,num1) functon_name(num1=2,num2=3)
#arbitary argument def function_name(*args) function_name(1,2,3,4) postintion nae thone
#function_name(**args) function_name(num2=4,num5=6,num3=10) keyword nae thone star na lone

#positional argument
def main():
    hello_world()

def hello_world():
    print("Hello World")
main()

#keyword Arguments
def greet(name,message):
    print("Hello,"+name+"."+message)
greet(message="How are you today?",name="GCA")

#variable length
def greet(*args):
    print(args)
greet(1,2,3,4)
def greet(**args):
    for key,value in args.items():
        print("Key:"+key+"Value"+value)
greet(name="GCA",message="How are you")

def cube(num):
    return num*num*num
print(cube(2))

#lambda arguments: expresson
add= lambda num1,num2:num1+num2
print(add(2,3))

print((lambda num1,num2,num3:(num1+num2)*num3)(2,3,4))


name= lambda name,message:name+message
print(name(message="how r u",name="gca"))