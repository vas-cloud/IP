string = input("Enter A Line: ")

uc = 0
lc = 0
dig = 0
space = 0
sym = 0

for i in string:
    if i.islower():
        lc+=1
    elif i.isupper():
        uc+=1
    elif i.isdigit():
        dig+=1
    elif i == " ":
        space+=1
    else:
        sym+=1

print(f"UpperCase : {uc}  lowercase : {lc}  digit : {dig}  Spaces : {space}  Symbols : {sym}")