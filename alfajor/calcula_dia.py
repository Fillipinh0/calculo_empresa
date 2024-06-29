#calcula manualmente o pix do dia
def cal_pix_dia(): 
    dia = 0

    while True:
        compra = input("Digite o numero ou 'n' para sair: ")
        if compra == "n":
            print(dia)
            break
        else:
            compra = float(compra)
            if compra > -100:
                dia += compra
