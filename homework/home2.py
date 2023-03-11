item1={x:x**3 for x in range(1,6)}
print(item1)
item2=list(lambda x:x%2==1,range(1,10))
print(item2)