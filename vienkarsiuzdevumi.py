def pirmais(skaitlis1, skaitlis2):
    reiz = skaitlis1*skaitlis2
    if reiz <= 1000:
        return reiz 
    return skaitlis1+skaitlis2

# print(pirmais(150,28))

def otrais(gals):
    ieprieksejais = 0 
    for esosais in range (gals+1):
        print(f"Esošais skaitlis - {esosais}, Iepriekšējais skaitlis - {ieprieksejais}, to summa = {esosais+ieprieksejais}")
        ieprieksejais = esosais
    return

# otrais(10)

def tresais():
    teksts = input("Lūdzu ievadi tekstu! : ")
    for i in range(0, len(teksts),2):
        print(teksts[i])

# tresais()

# teksts = "Sveiki!"

#  print(len(teksts))

def ceturtais():
    teksts = input("Lūdzu ievadi tekstu! : ")
    skaits = int(input("Cik pirmos burtus jāpazaudē? : "))
    print(teksts[skaits:])
    return

# ceturtais()

def piektais():
    saraksts = []
    ievade = input("Ievadi sarakstu, elementus atdalot ar atstarpēm! : ")
    saraksts = [elements for elements in ievade.split()]
    if saraksts[0] == saraksts[-1]:
        print("Pirmais un pēdējais ir vienādi!")
    else:
        print("Pirmais un pēdējais nav vienādi!")

    return

# piektais()

def sestais():
    saraksts = []
    ievade = input("Ievadi sarakstu, elementus atdalot ar atstarpēm! : ")
    saraksts = [int(elements) for elements in ievade.split()]
    for skaitlis in saraksts:
        if skaitlis % 5 == 0:
            print(skaitlis)
    return

# sestais()

def devitais(skaits):
    for cipars in range(1,skaits+1):
        for i in range(cipars):
            print(f"{cipars} ", end="")
        print("")
    return

devitais(10)
