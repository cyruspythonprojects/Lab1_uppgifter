lista_tal = []

while len(lista_tal) != 5:
    lista_tal.append(int(input("Skriv in ett tal: ")))
    
print("Genomsnittet är: ", sum(lista_tal)/5)