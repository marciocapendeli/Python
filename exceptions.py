#exeptions
#
#try  para lidar com situações em que erro
#except identifica o erro de digitação

while True:
    try:
        x = int(input("digite um valor para x "))
        print (f"x é {x:f}") 
    except ValueError:
        print("x nao é um valor")
    else:
        break