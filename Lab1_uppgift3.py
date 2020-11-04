list_1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
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