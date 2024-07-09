
personagens = [
    {
    "nome":"frodo","especie":"hobbit", "local":"condato"
    },
    {
    "nome":"Sam", "especie":"hobbit","local":"condato",
    },
    {
    "nome":"Legolas", "especie":"Elfo", "local":"Valfenda",
    }
    ] 
for personagem in personagens:
   print(personagem["nome"], personagem["local"])

    #print("personagens: {} especie: {} local: {}".format(personagem ["nome"], personagem["especie"],personagem ["local"]))


'''
personagens = {"frodo":"hobbit",
               "sam":"hobbit",
               "legolas":"elfo",
               "gandalf":"mago",
               "ginly":"anao", 
               "smeagol": "hobbit",
                "bilbo":"hobbit"}
for personagem in personagens:
    print(personagem, personagens[personagem])

    #print("a lista{} é personagens {}".format(personagens,personagem))
   
'''

