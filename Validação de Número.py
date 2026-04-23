# Validando entrada de numero inteiro
numero = None

while numero is None:
    try:
        numero = int(input("Digite um numero inteiro: "))
    except ValueError:
        print("Erro! Voce deve digitar um numero inteiro. Tente novamente.")

print(f"Numero digitado: {numero}")