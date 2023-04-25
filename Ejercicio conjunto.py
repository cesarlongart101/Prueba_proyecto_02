#Debemos hacer un ejercicio donde Vanessa va a hacer
# las operaciones matematicas y Cesar va a hacer los mensajes printcipas y los input


#Zona Cesar

print("---------------------------------")
print("Bienvenido al programa de cálculo")
print("---------------------------------")

operacion = input("¿Qué operación quieres hacer? Suma, Resta, Multiplicación o División: ")

if operacion == "Suma":
    num_1 = int(input("Dime un número: "))
    num_2 = int(input("Dime otro número: "))

#Zona de Vane

    Suma = num_1 + num_2
    print("La suma de", num_1, "y", num_2, "es igual a", Suma)

if operacion == "Resta":
    num_1 = int(input("Dime un número: "))
    num_2 = int(input("Dime otro número: "))

    Resta = num_1 - num_2
    print("La resta de", num_1, "y", num_2, "es igual a", Resta)

if operacion == "Multiplicacion":
    num_1 = int(input("Dime un número: "))
    num_2 = int(input("Dime otro número: "))

    Multiplicacion = num_1 * num_2
    print("La multiplicación de", num_1, "y", num_2, "es igual a", Multiplicacion)

if operacion == "Division":
    num_1 = int(input("Dime un número: "))
    num_2 = int(input("Dime otro número: "))

    Division = num_1 / num_2
    print("La division de", num_1, "y", num_2, "es igual a", Division)







