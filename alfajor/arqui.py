### Calcula o que compras para efetuar o pagamaneto para Lu
def compras():
    comprou = input("Vocês compraram algo esta semana?? S ou N")
    if comprou == "S":
        #lu = divid     <--- Para terminar o projeto preciso fazer o calculo da semana para ter o divid da semana e o banco de dados ainda  
        quem_comprou = input("Ce voce comprou algo digite: s")
        match quem_comprou:
            case "s":
                lu_val = 0
                while True:
                    repet = input("Digite 0 para continuar ou 1 se a Lu comprou!")
                    if repet == "0":
                        compras = input("Valor da compra:")
                        lu_val = lu_val - (compras / 2)
                    elif  repet == "1":
                        compras = input("Valor da compra:")
                        lu_val = lu_val + (compras / 2)
                    else:
                            print("Voce precisa pagar a Lu: ", lu_val)
    else:
         pass