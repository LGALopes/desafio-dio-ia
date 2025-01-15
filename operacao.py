num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

operacao = input("Digite a operação que deseja realizar (+, -, *, /): ")

if operacao == "+":
    resultado = num1 + num2
    print(f"O resultado de {num1} + {num2} é {resultado}.")
elif operacao == "-":
    resultado = num1 - num2
    print(f"O resultado de {num1} - {num2} é {resultado}.")
elif operacao == "*":
    resultado = num1 * num2
    print(f"O resultado de {num1} * {num2} é {resultado}.")
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"O resultado de {num1} / {num2} é {resultado}.")
    else:
        print("Divisão por zero não é permitida.")
else:
    print("Operação inválida. Por favor, escolha entre +, -, * ou /.")
