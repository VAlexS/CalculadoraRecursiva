for numero in range(5):
    print(numero) #imprime de 0 a 4

#for else

print("---------------------")

numero_a_buscar = 3

for numero in range(5):
    if numero == numero_a_buscar:
        print("encontrado", numero_a_buscar)
        break
    else:
        print("No encontré el número buscado")

print("--------------------------------")

for char in "Ultimate Python":
    print(char)


