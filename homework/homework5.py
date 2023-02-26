# num=int(input("Enter Number for dice:"))
# count1=0
# count2=0
# count3=0
# count4=0
# count5=0
# count6=0
# for number in range(num):
#     import random
#     dice=random.randint(1,6)
#     print(dice)
 
#     if dice==1:
#         count1+=1
 
#     elif dice==2:
#         count2+=1
    
#     elif dice==3:
#         count3+=1
   
#     elif dice==4:
#         count4+=1
    
#     elif dice==5:
#         count5+=1
    
#     elif dice==6:
#         count6+=1
# print(f" one:{count1}\n two:{count2}\n three:{count3} \n four:{count4}:\n five:{count5} \n six:{count6}")

import random
counters =[0]*6
for _ in range(5000):
    face=random.randint(1,6)
    counters[face-1]+=1
for face in range(1,7):
    print(f"No.{face} dice{counters[face-1]}times")