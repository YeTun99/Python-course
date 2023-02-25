my_numbers=[1,2,3,4,5,0.33]
print([number*2 for number in my_numbers])

my_list=[]
for number in my_numbers:
    if number %2==0:
        my_list.append("even")
    else :
        my_list.append("odd")
print(my_list)

even_numbers=[number for number in my_numbers if number%2==0]
print(even_numbers)

result=["even" if number%2==0 else "odd" for number in my_numbers]
print(result)

print(["even" if number%2==0 else "odd" if number%2==1 else "unknown" for number in my_numbers])