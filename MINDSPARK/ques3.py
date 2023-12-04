str_ = input("Enter A String: ")
v_str = "aeiouAEIOU"

for i in str_:
    if i not in v_str:
        print("Not Accepted ")
        break

    else:
        print("Accepted")
        break