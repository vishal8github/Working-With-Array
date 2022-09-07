ls = input("enter some numbers ").split()

arr = [eval(x) for x in ls]

print(ls, "\n", type(ls))

print(arr, "\n", type(arr))