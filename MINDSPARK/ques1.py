
def pop(string,i):
    before = string[:i]
    after = string[i+1:]

    return before+after


string = input("Enter A string: ")
n = int(input("Enteer A The Indexing NumberTo Remove: "))
print(pop(string,n))