string=(input("Enter A String: "))
num = "1234567890"
str2 = ""
for i in string:
    if i not in num:
        str2+=i

print(str2)