lst = []
nums = [1,2,3,4,5]
for i in range(1,6):
    num = int(input("Enter The Number: "))
    lst.append(num)

for i in nums:
    if i not in lst:
        print(f"{i} - missing number")

