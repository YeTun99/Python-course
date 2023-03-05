stock={
    'Apple':200,
    'Google':25,
    'Microsoft':400,
    'Twitter':50,
    'facebook':100
}

new_stock={}

for key,value in stock.items():
    if value>100:
        new_stock[key] = value
        # new_stock.append({ key:value})
        # print("Hello")
    
    
print(new_stock)
