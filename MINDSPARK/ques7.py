lst = [5,10,15,20,25,50,20]

n = int(input("Enter THE Number: "))

for i in lst:
    if i == n:
        print("Element Found")
        ind = lst.index(i)
        lst[ind] = 200
        break

print(lst)