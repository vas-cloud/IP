lst = [10,20,[300,400,[5000,6000],500],30,40]

for i in lst[2]:
    if i == 6000:
        ind = lst.index(i)
        print(ind)
        lst.insert(ind+1,"7000")
print(lst)