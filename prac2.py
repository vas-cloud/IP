# Write a program that inputs an integer range 0–999 and then prints if the integer entered is a 1/2/3 digit number.\


num = int(input("Enter The Number: "))

if 0<num<10:
    print("The Number Is Single Digit Number")
elif 11<num<99:
    print("The Number Is Two Digit Number")
else:
    print("Three Digit Number")

