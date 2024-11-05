# Função para soma
def soma(x, y):
    return x + y


#Função para multiplicação
def multiplicação(x, y):
    return x * y


#Função para divisão
def divisão(x, y):
    return x / y


#Função pra subtração
def subtração(x, y):
    return x - y


def mostrar_historico(lista_contas):
    if not lista_contas:
        print("Nenhuma operação realizada ainda.")
    else:
        print("Histórico de operações:")
        for operacao in lista_contas:
            print(operacao)


def limpar_historico(lista_contas):
    lista_contas.clear()

    print("Histórico limpo.")


# Função principal
def calculadora():
    lista_contas = [ ]
    while True:

        operador = input("Digite a operação:")
        if operador != "hist":
            num1 = int(input("Digite o primeiro número: "))
            num2 = int(input("Digite o segundo número:  "))

        result1 = soma(num1, num2)
        result2 = divisão(num1, num2)
        result3 = subtração(num1, num2)
        result4 = multiplicação(num1, num2)

        if operador == "soma":
            print("Resultado da soma:" + str(result1))
            conta= str(num1) + "+" + str(num2) + "=" + str(result1)
            lista_contas.append(conta)
            print(conta)
        elif operador == "divisão":
            print("Resultado da divisão:" + str(result2))
            conta = str(num1) + "/"  + str(num2) + "=" + str(result1)
            lista_contas.append(conta)
            print(conta)
        elif operador == "subtração":
            print("Resultado da subtração:" + str(result3))
            conta = str(num1) + "-" + str(num2) + "=" + str(result1)
            lista_contas.append(conta)
            print(conta)
        elif operador == "multiplicação":
            print("Resultado da multiplicação" + str(result4))
            conta = str(num1) + "*" + str(num2) + "=" + str(result1)
            lista_contas.append(conta)
            print(conta)
        elif operador == "hist":
            mostrar_historico(lista_contas)

calculadora()
