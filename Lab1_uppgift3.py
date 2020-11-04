list_1 = list(range(1,21))
odd = []
even = []

for i in list_1:
    if i%2 == 0:
        print(i, "is even.")
        even.append(i)
    else:
        print(i, "is odd.")
        odd.append(i)

print("Odd:",odd)
print("Even:",even)      