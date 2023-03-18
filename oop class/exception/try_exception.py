# try:
#     number=int(input("Enter Number"))
# except:
#     print("Invalid input number")
#if ka condition and exception ka error

try:
    value=3/int(input("Enter number1 :"))
    number=int(input("Enter number2 :"))
except ZeroDivisionError:
    print("Division by zero error")
except ValueError:
    print("Invalid Input Number")
finally:
    print("Program Completed")
