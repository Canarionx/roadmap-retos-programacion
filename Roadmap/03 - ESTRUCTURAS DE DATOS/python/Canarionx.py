#Listas 
my_list = ["Aday","Adan","Feluco","Brais"]
print(my_list)
my_list.append("Castor")  #Insercion
print(my_list)
my_list.remove("Brais")   #Eliminacion
print(my_list)
print(my_list[1])   #Acceso
my_list[1] = "Cono"      #Actualizacion
print(my_list)
my_list.sort()   # Ordenacion
print(type(my_list))

# Tuplas
my_tuple: tuple = ("Adan", "Feluco", "18")
print(my_tuple[1])  # Acceso
print(my_tuple[2])
my_tuple = tuple(sorted(my_tuple)) # Ordenacion
print(my_tuple)
print(type(my_tuple))

# Sets
my_set = {"Adan", "Feluco", "18"}
print(my_set)
my_set.add("adan@gmail.com")  # Insercion
print(my_set)
my_set.remove("Adan")  # Eliminacion
print(my_set)
my_set = set(sorted(my_set))  # No se puedeordenar
print(my_set)
print(type(my_set))

# Diccionario 
my_dict: dict = {
    "name":"Adan", 
    "alias":"Feluco", 
    "ag":"18"
}
my_dict["email"] = "adan@gmail.com" # Insercion
print(my_dict)
del my_dict["alias"] #Eliminacion
print(my_dict)
print(my_dict["name"])  # Acceso
my_dict["age"] = "18" # Actualizacion
print(my_dict)
my_dict = dict(sorted(my_dict.items()))  #Ordenacion
print(my_dict)
print(type(my_dict))

"""
Dificultad Extra
"""

def my_agenda():
   
   agenda = {}


   while True:

    print("")
    print("1. Buscar contacto")
    print("2. Insertar contacto")
    print("3. Actualizar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")

    option = input("\nSelecciona una opcio:")

    match option:
        case "1":
            name = input("Introduce el nombre del contacto a buscar:")
            if name in agenda:
                print(
                    f"El numero de telefono de {name} es {agenda[name]}.")
            else:
               print(f"El contacto {name} no existe.")
        case "2":
            name = input("Introduce el nombre del contacto:")
            phone = input("Introduce el telefono del contacto:")
            if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
                agenda[name] = phone
            else:
               print(
                  "Debes introducir un numero de telefono con maximo de 12 digitos.")
        case "3":
            name = input("Introduce el nombre del contacto a actualizar:")
            if name in agenda:
               phone = input("Introduce el telefono del contacto")
               if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
                  agenda[name] = phone
               else:
                    print(
                    "Debes introducir un numero de telefono un maximo de 11 digitos.")
            else:
                print(f"El conctato {name} no existe.")
        case "4":
            name = input("Introduce el nombre del contacto a eliminar:")
            if name in agenda:
               del agenda[name]
            else:
               print(f"El contacto {name} no existo")
        case "5":
            print("Saliendo de la aguenda")
            break
        case _:
            print("Opcion no valida.Elige una opcion del 1 al 5.")



my_agenda()
