print("Hi!")

mainigais = "Hello!"

print(mainigais)

cits = 5
print(cits)
cits = cits +  6 

print(mainigais,cits)

# ievade = int( input("Ievadiet Skaitli! : ") )
# print(ievade)
# lielaks = ievade + 1 
# print("One bigger:", lielaks)

print(6==3)

number = int(input("Give me a number!: "))

if(number>10):
    print ("Big")
elif(number<5):
    print("Small")
elif(number>10 and number<20):
    print("Medium")
else:
    print("Normal")

def calculate(num1, num2):
    reiz = num1*num2
    if (reiz<=10):
        return reiz 
    return num1+num2


print( calculate(50,4))
print( calculate(60,4))
print( calculate(5,4))
print( calculate(50,1))
print( calculate(5,2))

print("--------------------")

for i in range(-2,5,2): # range (begining, end (without), step)
    print(calculate(3,i))

print("--------------------")

answ = "y"
while(answ == "y"):
    sk1 = int(input("pirmais: "))
    sk2 = int(input("otrais: "))
    print(calculate(sk1,sk2))
    answ = input("Vai velaties turnipat? (ievadiet 'y'): ")
    