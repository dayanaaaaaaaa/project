def  calcularIMC(p, a):
    return p / (a * a)

def NivelDePeso(IMC):
    if IMC < 18.5:
        return "Bajo peso"
    elif 18.5 <= IMC and IMC <= 24.9:
        return "Normal" 
    elif 25 <= IMC <= 29.9:
        return "Sobrepeso"
    elif 30 <= IMC and IMC <= 34.9:
        return "Obesidad 1"
    elif 35 <= IMC <= 39.9:
        return "Obesidad 2"
    elif 40 <= IMC <= 49.9:
        return "Obesidad 3"
    elif IMC >= 50:
        return "Obesidad 4"
    

answ = "y"
while answ == "y":
    weight_peso = float(input("Ingrese el peso (Kg): "))
    height_altura = float(input("Ingrese su altura (m): "))

    print("Su nivel de peso es:", NivelDePeso(calcularIMC(weight_peso, height_altura)))

    answ = input ("Do you want to continue? (write 'y') :")
