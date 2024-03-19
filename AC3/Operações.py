def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Dividir por zero não é válido."

def calcular():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (Soma, Subtração, Multiplicação, Divisão): ")

    if operacao == 'soma':
        resultado = soma(num1, num2)
    elif operacao == 'subtração':
        resultado = subtracao(num1, num2)
    elif operacao == 'multiplicação':
        resultado = multiplicacao(num1, num2)
    elif operacao == 'divisão':
        resultado = divisao(num1, num2)
    else:
        resultado = "Operação inválida."

    print("Resultado:", resultado)