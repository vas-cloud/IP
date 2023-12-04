lst = lst = [5,10,15,20,25,20,50,20]

u_lst = []

for i in lst:
    if i not in u_lst:
        u_lst.append(i)
        for i in u_lst:
            if i == 20:
                u_lst.remove(i)



print(u_lst)