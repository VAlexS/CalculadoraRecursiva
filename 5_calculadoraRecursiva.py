def suma(op1, op2):
    return int(op1) + int(op2)


def resta(op1, op2):
    return int(op1) - int(op2)


def mult(op1, op2):
    return int(op1) * int(op2)


def div(op1, op2):
    return int(op1) / int(op2)


def show_resultado(str):
    print(str)


print("La operaciones son suma, resta, mult o div")
num = input("Ingrese numero: ")
resultado = 0

while True:

    operacion = input("Ingrese operación, o salir en caso de que no desees continuar: ")
    if operacion.lower() != "salir":
        if operacion.lower() == "suma":
            num2 = input("Ingrese el siguiente numero: ")
            resultado = suma(num, num2)
            show_resultado(resultado)
            num = resultado
        elif operacion.lower() == "resta":
            num2 = input("Ingrese el siguiente numero: ")
            resultado = resta(num, num2)
            show_resultado(resultado)
            num = resultado
        elif operacion.lower() == "mult":
            num2 = input("Ingrese el siguiente numero: ")
            resultado = mult(num, num2)
            show_resultado(resultado)
            num = resultado
        elif operacion.lower() == "div":
            num2 = input("Ingrese el siguiente numero: ")
            resultado = div(num, num2)
            show_resultado(resultado)
            num = resultado
    else:
        break
