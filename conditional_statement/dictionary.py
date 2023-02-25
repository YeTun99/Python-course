#{key:value,key:value}
#student={"name","John","Phone":"09_2321412423}

# monthConversions={
#     "Jan":"January",
#     "Feb":"Febuary",
#     "M":"March"
# }

# print(monthConversions["Jan"])
# print(monthConversions["M"])

# print(monthConversions.get("M"))
# # print(monthConversions["febb"]) #error
# print(monthConversions.get("jasn"))#noerror
# print(monthConversions.get("jan","Invalid key"))

person ={"name":"John","age":20,'weight':60,'office':'GCA'}
print('name' in person,'tel' in person)
person['tel']="12344355"
person['signature']='My Signature'
print(person)

students={
    1001:{'name':'Aung Khant','sex':'Male','age':21,'place':'Southokalapa'},
    1002:{'name':'Ye Tun','sex':'Male','age':21,'place':'Southokalapa'},
    1003:{'name':'Chan Win','sex':'Male','age':21,'place':'Southokalapa'},
    1004:{'name':'Min Zaw Hein','sex':'Male','age':21,'place':'Southokalapa'}
}
print(students.keys())
print(students.values())

for key,value in students.items():
    print(key,'----->',value)

stu1 = students.pop(1002)
print(stu1)
print(students)

print(len(students))
#stu2=students.po(1005) #keyerror:1005
stu2=students.pop(1005,{})
print(stu2)

result= students.setdefault(1002,{'name':'Ye Tun','sex':'Male','age':21,'place':'Southokalapa'})#1002  သာ list ထဲမှာရှိခဲ့ရင်  input မလုပ်ပဲ return ပြန်ပေး
print(result)
print( students)

other={
    1005:{'name':'Aung Khant','sex':'Male','age':21,'place':'Southokalapa'},
    1006:{'name':'Aung Khant','sex':'Male','age':21,'place':'Southokalapa'}
}

students.update(other)
print(students)