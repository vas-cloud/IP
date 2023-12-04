str = input("Enter A String: ")
lst = []

rev = str.split()[::-1]
print(rev)
for i in rev:
    lst.append(i)
print(lst)
print(" ".join(lst))
