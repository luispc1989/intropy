# Montante inicial que o utilizador da máquina deve pagar
due = 50

# Aplicação de loop infinito para continuar a pedir moedas até que o montante seja pago ou haja troco
while True:
    # Exibe o montante restante que o utilizador ainda deve
    print("Amount Due:", due)

    # Solicita ao utilizador que insira uma moeda e converte para integer
    money = int(input("Insert Coin: "))

    # Verifica se a moeda inserida é válida (ou seja, 25, 10 ou 5 cêntimos)
    if money == 25 or money == 10 or money == 5:
        # Se o valor da moeda inserida for maior ou igual ao montante devido, calcula o troco
        if money >= due:
            # Exibe o troco, que é a diferença entre o valor inserido e o montante devido
            print("Change Owed:", money - due)
            # Sai do loop, pois a transação está concluída
            break
        # Se o valor inserido for menor que o devido, subtrai o valor da moeda do montante devido
        due -= money
    else:
        # Se a moeda for inválida, o loop continua e o utilizador é solicitado a inserir outra moeda
        continue

