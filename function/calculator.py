def calc(*args,init_value,op,**kwargs):
    result=init_value
    for arg in args:
        if type(arg) in (int,float):
            result=op(result,arg)
    for value in kwargs.values():
        if type(value) in (int,float):
            result=op(result,value)
    return result
# def add(x,y):
#     return x+y
# def mul(x,y):
#     return x*y

import operator
print(calc(1,2,3,init_value=0,op=operator.add,a=1,b=2,c=5))
print(calc(1,2,3,init_value=1,op=lambda x,y:(x*y),a=3,y=5))
print(calc(2,3,4,init_value=2,op=lambda x,y:x+y,x=1,y=2,z=5,v=1))

def square(x):
    return x**2

def splicer(my_string):
    if len(my_string)%2==0:
        return True
    else: return False

my_list=[1,2,3,4,5,6]
my_str=["John","Honey","Mia"]

print(list(map(square,my_list)))
print(list(filter(splicer,my_str)))

def mul(x,y):
    return x*y
my_list1=[1,2,3,4,5]
my_list2=[6,7,8,9,10]
print(list(map(mul,my_list1,my_list2)))