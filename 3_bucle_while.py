numero = 1

while numero < 100:
    print(numero)
    numero *= 2

print("---------------------------")

comando = ""

while comando.lower() != "salir":
    comando = input("$ ")
    print(comando)

print("-----------------")

while True:
    comando = input("$ ")
    print(comando)
    if comando.lower() == "salir":
        break
