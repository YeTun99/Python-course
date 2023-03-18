import uuid
import os
import json

uuid_obj=uuid.uuid1()
print(uuid_obj)
path='/home/yetun/gca/Python-course/standard_library/uuid_module.py'
print(os.path.getatime(path))
print(os.path.getsize(path))
if os.path.exists(path):
    print(f'the file {path} exists.')
else:
    print(f'the file {path} does not exist')

#Json is universal data exhange
#API
#Serialization => transmit or save data structure over network

my_dict={
    "name":'John',
    'age':30,
    'is employed':True
}
print(json.dumps(my_dict))

#Serialization

with open('data.json','w') as file:
    json.dump(my_dict,file)

#Deserialization
with open('data.json','r') as file:
    my_dict=json.load(file)
    print(my_dict)

""" 
Python               JSon
Dict                 object
list/tuple           array
str                  string
int/float            number
Bool(True/False)     boolean(true/false)
None                 null"""