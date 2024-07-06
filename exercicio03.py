
""""
nome = input("digite o personagem ")

if nome == "frodo":
    print("hobbit")
elif nome == "sam":
    print("hobbit")
elif nome == "aragon":
    print("homem")
elif nome == "gandalf":
    print ("mago")

    """
nome = input("digite o personagem ")
match nome:
    case "frodo" | "sam":
        print ("hobbit")
    case "aragorn":
        print ("homem")
    case "gandalf":
        print ("mago")
    case _: 
        print ("quem???")
