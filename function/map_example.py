def square(x):
    x**=2
    return x
    

numbers=[1,2,3,4,5,6]
squared_numbers=[square(n) for n in numbers]
# squared_numbers=list(map(square,numbers))

print(squared_numbers)