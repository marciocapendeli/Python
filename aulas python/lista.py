'''
personagens = ["frodo", "sam", "legolas", "gandalf", "ginly", "smeagol", "bilbo"]

print(personagens)

print("lista fixa")
for i in range(4):
    print("nome: ",personagens[i])

print("lista dinamica")
for personagem in personagens:
    print("nome: ", personagem)
   

#exercicio
personagens = ["frodo", "sam", "legolas", "gandalf", "ginly", "smeagol", "bilbo"]
especies = ["hobbit", "hobbit", "elfo", "mago", "anao", "hobbit", "hobbit"]

print("\nClassificação por Espécie: \n")
for personagem, especie in zip(personagens, especies):
    print("personagem: {} Especie: {} ".format(personagem, especie))

#resolução
'''

personagens = ["frodo", "sam", "legolas", "gandalf", "ginly", "smeagol", "bilbo"]
especies = ["hobbit", "hobbit", "elfo", "mago", "anao", "hobbit", "hobbit"]

for i in range(7):
    print("personagem: {} Especie: {} ".format(personagens[i], especies[i]))
   # print("nome:" , personagens[i], "especies:", especies[i])

for i in range(5):
    print(i)
