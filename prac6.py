# Write a program to create a dictionary containing names
# of competition winner students as keys and number of
# their wins as values.

dic = {}

n = int(input("Enter The Number Of Students: "))

for i in range(1,n+1):
    name = input("Enter The Name Of Student: ")
    wins = int(input("Enter The Number Of Wins: "))

    dic[name] = wins


print(dic)





