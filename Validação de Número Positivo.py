
numero = -1

while numero < 0:
    numero = int(input("Digite um numero positivo: "))
    if numero < 0:
        print("Numero invalido! Digite um numero positivo.")

print(f"Numero cadastrado: {numero}")