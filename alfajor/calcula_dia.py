#calcula manualmente o pix do dia
def cal_pix_dia(): 
    dia = 0

    while True:
        compra = input("Voce pode:\n-Digitar um numero para somar\n-Digitar'n' para sair\n-Escrever 'delet' para deletar\n Digite: ")
        if compra == "n":
            print(dia)
            break
        elif compra == 'delet':
            certe = input("Voce realmente quer deletar?")
            if certe == 'deletar':
                dia = 0
        else:
            compra = float(compra)
            if compra > -100:
                dia += compra
    return(dia)
valor_semana = []
valor_dia = cal_pix_dia()
print(valor_dia)
valor_semana.push(valor_dia)
print(valor_semana)
