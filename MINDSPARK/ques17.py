import statistics
lst =[]
for i in range(4):
    num = int(input("Enter: "))
    lst.append(num)

print(statistics.mode(lst))