# def common_word(list_1,list_2):
#     result= [i for i in list_1 if i in list_2]
#     return result

# list_1=[]
# list_2=[]

# i=0
# while i<6:
#     x = int(input("Enter Number for list 1:"))
#     list_1.append(x)
#     i+=1
# print(list_1)
# a=0
# while a<6:
#     x = int(input("Enter Number for list2:"))
#     list_2.append(x)
#     a+=1
# print(list_2)
# print(f"Commom elements are: {common_word(list_1,list_2)}")

def find_common_words(*list):
    result=[]
    for word in list[0]:
        if all (word in lst for lst in list[1:]):
            result.append(word)
    return result  
   
       

list1=[1,2,3,4,5,6,"orange"]
list2=[3,"apple","orange"]
list3=[3,8,9,4]

print(find_common_words(list1,list2,list3))


# def common_words(*lists):
#     common = []
#     for word in lists[0]:
#         print(lists[1])
#         if all(word in lst for lst in lists[1:]):
#             common.append(word)
#     return common

# # Example usage:

# list1 = [1,2,3,"apple", "banana", "orange", "peach"]
# list2 = [3,5,6,"orange", "peach", "grape", "pear"]
# list3 = [3,"peach", "pear", "cherry", "mango"]
# common_words = common_words(list1, list2, list3)
# print("Common words:", common_words)