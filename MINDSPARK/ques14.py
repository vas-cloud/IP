str_ = input("Enter A String: ")
lst = ""
for i in str_:
    if i not in lst:
        lst+=i

print((lst))