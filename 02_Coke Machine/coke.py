def main():
    # Montante inicial que o utilizador deve pagar
    amount_due = 50

    #Solicitar montante até que o devido seja > 0
    while amount_due > 0:
        print(f"Amount Due: {amount_due}")

        # Solicita que ao utilizador a inserção de uma moeda
        coin = int(input("Insert Coin: "))

        # Verifica se a moeda é válida -> 25, 10 ou 5 cêntimos
        if coin in [25, 10, 5]:
            # Subtrai o valor da moeda ao montante devido
            amount_due -= coin
        else:
            # Se moeda inválida, o programa continua a pedir moedas válidas
            continue

    # Programa efetua o cálculo do troco, caso exista
    change_owed = abs(amount_due)

    #Exibição do troco, caso este exista
    print(f"Change owed: {change_owed}")

if __name__ == "__main__":
    main()
