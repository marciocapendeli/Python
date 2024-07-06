
# nao esquecer de usa (:) no final da function

def exibirMensagem():
    print("Sou uma function")

def exibirSaudação(nome,total):
    print("ola,",nome)
    print("o total da soma é", total)

def somar(valor1,Valor2):
    total = valor1+Valor2
    return total
  
def main():
    soma = somar (6,9)
    exibirMensagem()
    print (soma)
    exibirSaudação("Marcio Silva", soma)
    

main()