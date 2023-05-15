#Debemos hacer un ejercicio donde Vanessa va a hacer
# las operaciones matematicas y Cesar va a hacer los mensajes principales y los input




#Este codigo que puse va a mostrar un menú, está hecho con una función. (Lo edite aquí mismo en Github, no lo corrí - Pruebalo tú)
#Para definir una funcion se usa la palabra def seguido del nombre de la funcion, parentesis () y dos puntos:
def menu():
  salir = False
  while not (salir):
      print()
      print("__________________")
      print("------ MENU ------")
      print("__________________")
      print()
      print("1. Suma \n"
            "2. Resta \n"
            "3. Multiplicación \n"
            "4. División \n"
            "5. Salir \n     ")

      op = input("Seleccione una opción: ")

      if op == "1":
        num_1 = int(input("Dime un número: "))
        num_2 = int(input("Dime otro número: "))
        Suma = num_1 + num_2
        print("La suma de", num_1, "y", num_2, "es igual a", Suma)
      elif op == "2":
        num_1 = int(input("Dime un número: "))
        num_2 = int(input("Dime otro número: "))
        Resta = num_1 - num_2
        print("La resta de", num_1, "y", num_2, "es igual a", Resta)
      elif op == "3":
        num_1 = int(input("Dime un número: "))
        num_2 = int(input("Dime otro número: "))
        Multiplicacion = num_1 * num_2
        print("La multiplicación de", num_1, "y", num_2, "es igual a", Multiplicacion)
      elif op == "4":
        num_1 = int(input("Dime un número: "))
        num_2 = int(input("Dime otro número: "))
        Division = num_1 / num_2
        print("La division de", num_1, "y", num_2, "es igual a", Division)
      elif op == "5":
        break
      else:
          print()
          print("Debe seleccionar una opción de 1 a 6")
          print()

menu()




