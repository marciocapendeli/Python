
# Refaturando com função modo profissional
#-----------------------------------------
def calculaMedia(valor1, valor2):
    return (valor1 + valor2)/2

def calcularConceito(valor):
    if valor >=9:
        return "O"
    elif valor > 7 and valor <= 8.9:
        return"B"
    elif valor > 5 and valor <= 6.9:
        return "S"
    else:
        return "I"
def main():
 # Solicita as notas A e B ao usuário
    valor1 = float(input("Digite a nota A: "))
    valor2 = float(input("Digite a nota B: "))
#calcular a media
    media = calculaMedia (valor1 + valor2)

#verificar conceitos
    print(calcularConceito(media))

main()
"""""
# modo iniciante

 # Solicita as notas A e B ao usuário
notaA = float(input("Digite a nota A: "))
notaB = float(input("Digite a nota B: "))

# Calcula a média das notas A e B

media = (notaA + notaB) / 2



#verificar conceito
if media >= 9:
    print("Conceito: Nota O")
elif media >= 7 and media <= 9:
    print("Conceito: Nota B")
elif media >= 7 and media < 8:
    print("Conceito: Nota C")
elif media >= 6 and media < 7:
    print("Conceito: Nota D")
else:
    print("Conceito: Nota I")

"""

