base=int(input("Enter base:"))
power=int(input("Enter power:"))

result=1
for num in range(power):
    result=base*result
    
print(result)
    
