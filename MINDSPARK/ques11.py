lst = []
for i in range(1,4):
    num = int(input("Enter The Numbers: "))
    lst.append(num)


if lst[0]+lst[1]>=10 or lst[1]+lst[2]>=10 or lst[2]+lst[0]>=10:
    print("Yes")
else:
    print("No")


