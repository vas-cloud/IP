# Write a program that check for presence of a value inside
# a dictionary and prints its key.

dic = {}

n = int(input("Enter The Number Of Students: "))

for i in range(1,n+1):
    name = input("Enter The Name Of Student: ")
    wins = int(input("Enter The Number Of Wins: "))

    dic[name] = wins


key = input("Enter The Name Of Student: ")

if dic.get(key) is not None:
    print(dic[key])
else:
    print(f"{key} Not Found :(")
