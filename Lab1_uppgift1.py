answer = ""

while True:
    answer = input("Gillar du Python?\nSvar: ")
    if answer.upper() != "JA":
        print("FEL SVAR! FÖRSÖK IGEN!")
    else:
        break
    
print("HELT RÄTT! JAG OCKSÅ!")