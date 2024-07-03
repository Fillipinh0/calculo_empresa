### Calcula o que compras para efetuar o pagamaneto para Lu
def compras():
<<<<<<< HEAD
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
=======
    comprou = input("Vocês compraram algo esta semana?? S ou N ").upper()
    if comprou == "S":
        #Preciso aprender a mecher com banco de dados para passar o valor da semana para realemente saber quanto pagar... ate entao vou fazer semi manual
        lu_val = float(input("Escreva o valor total da semana: ")) / 2
        while True:
            repet = input("Digite 0 para continuar ou 1 se a Lu comprou!")
            if repet == "0":
                compras = float(input("Valor da compra:"))
                lu_val = lu_val - (compras / 2)
            elif  repet == "1":
                compras = float(input("Valor da compra:"))
                lu_val = lu_val + (compras / 2)
            else:
                print("Voce precisa pagar a Lu: ", lu_val)
                break
    else:
         pass
    semana = input('Escreva o tal da semana: ')
compras()
>>>>>>> 8197b75 (Mudei algumas cisas depois que usei ele...)
