num = int(input("Enter The Number: "))
sums = 0
prod = 1
for i in range(1,num+1):
    sums+=i
    prod+=i
    
if prod%sums == 0:
    print("Yes")
else:
    print("no")
    

