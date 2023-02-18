year=int(input("Enter year: "))
leapyear=year%4==0 or year%400==0 and year%100!=0

print(leapyear)