
""""
#codigo iniciante
def verificarParImpar(numero):
    if numero %2 == 0:
        return "par"
    else:
        return "ímpar"


numero = int(input("Digite um número inteiro: "))
resultado = verificarParImpar(numero)
print(f"O número {numero} é {resultado}.")

"""

#codigo melhorado abaixo

def isPar(numero):
    return numero % 2 == 0

def main():
    #ler um numero
    valor = int(input("Digite um numero"))

    # verificar se é par ou impar
    if isPar(valor):
        print("par")
    else:
        print("impar")

main()