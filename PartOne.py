var = str(input("What would you like rewrote in snake case?"))
list(var)

for i in var:
    if i.isupper():
        var += "_" + i.lower()
    else:
        var += i

print(var)

