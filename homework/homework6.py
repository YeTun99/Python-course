def common_word(list_1,list_2):
    result= [i for i in list_1 if i in list_2]
    return result

list_1=[]
list_2=[]

i=0
while i<6:
    x = int(input("Enter Number for list 1:"))
    list_1.append(x)
    i+=1
print(list_1)
a=0
while a<6:
    x = int(input("Enter Number for list2:"))
    list_2.append(x)
    a+=1
print(list_2)
print(f"Commom elements are: {common_word(list_1,list_2)}")