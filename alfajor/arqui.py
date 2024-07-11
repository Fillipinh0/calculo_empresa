### Calcula o que compras para efetuar o pagamaneto para Lu
def compras():
    comprou = input("Vocês compraram algo esta semana?? \n-Digite 'S' ou 'N' \nDigite: ").upper()
    if comprou == "S":
        #Preciso aprender a mecher com banco de dados para passar o valor da semana para realemente saber quanto pagar... ate entao vou fazer semi manual
        lu_val = float(input("Escreva o valor total da semana: ")) / 2
        while True:
            repet = input("-Se voce comprou tecle '0' \n-se a Lu comprou tecle '1' \n-passar para etapa 2 tecle '2' \nDigite:")
            match repet:
                case '0':
                    compras = float(input("Valor da compra:"))
                    lu_val = lu_val - (compras / 2)
                case '1':
                    compras = float(input("Valor da compra:"))
                    lu_val = lu_val + (compras / 2)
                case '2':
                    valor_dinheiro = float(input("Digite total em dinheiro fisico:"))
                    pagar_lu = (lu_val - valor_dinheiro)
                    print("Voce precisa pagar a Lu: ", pagar_lu, 'total dela',lu_val)
                    break
    else:
        lu_val = float(input("Escreva o valor total da semana: ")) / 2
        print("Voce precisa pagar a Lu: ", pagar_lu, 'total dela',lu_val)

compras()
