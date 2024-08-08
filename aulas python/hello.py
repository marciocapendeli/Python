#le o nome deo usuario
nome = input("Qual é seu nome? ")
nome = nome.strip() #retira espaços em branco
nome = nome.capitalize()#coloca a pimeira Letra em Maiusculo
#unificando ordens de funções nome.strip().capitalize()

#imprime uma mensagem na tela
#print("Ola,"+ nome)     

#imprimindo com parametro end
#print("ola,", end="")
#print(nome)

#usando aspas para destacar
#print('Ola, "Amigo" ') 

#coloca o nome e sobre com inicios em maiuscula .strip().title()

#função split separa nome de sobre nome
primeiro, sobrenome = nome.split("")
nome = nome.strip().title()

#usando sem concatenização mas com chaves e f (magic simbols)
print(f"Ola, {nome}") 
print(sobrenome)

