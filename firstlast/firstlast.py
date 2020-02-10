posl = input("enter numbers:")
list = posl.split()
for i in range(len(list)):
    list[i] = int(list[i])
print(list[0], list[-1])