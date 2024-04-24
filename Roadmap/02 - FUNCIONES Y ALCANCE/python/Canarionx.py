"""
Funciones definidas por el mundo 
"""

# Funciones Simples 


from itertools import count


def greet():
     print("Hola, Feluco!!")

greet() # La instruccion greet te lo repite el texto

# Funciones con retorno

def return_greet():
     return "Hola, Feluco!"

print(return_greet())

# Funciones con un argumento 

def arg_greet(name):
     print(f"Hola,{name}!")

arg_greet("Canarionx")

# Funciones con argumentos

def arg_greet(greet,name):
     print(f"{greet},{name}!")

arg_greet("Eyy","Canarionx")

# Funciones con un argumento predeterminado

def defult_arg_greet(name="Python"):
     print(f"Hola, {name}!")

defult_arg_greet("Canarionx")
defult_arg_greet()

# Funciones con argumentos y retorno

def return_arg_greet(greet,name):
     return(f"{greet},{name}!")

print(return_arg_greet("Eyy","Canarionx"))

 # Con retorno varios valores 
def multiple_return_greet():
    return "Hola", "Canarionx"

greet, name = multiple_return_greet()
print(greet)
print(name)

# Funciones con un numero variable de argumentos

def variable_arg_greet(*names):
     for name in names:
          print(f"Holaa, {name}!")

variable_arg_greet("Python", "Canarionx","Feluco","Chavales")

#Funcion con un numero variable de argumentos con palabra clave

def variable_key_arg_greet(**names):
     for key,value in names.items():
          print(f"Hola, {value} ({key})!")

variable_key_arg_greet(
     language="Python", 
     name= "Canarionx",
     alias="Feluco",
     age="18"
)

"""
Funciones dentro de funciones 
"""
def outer_function():
    def inner_function():
         print("Funcion interna: Hola Chavales !")
    inner_function()

outer_function()

"""
Funciones del lenguaje (built-in) 
"""
print(len("Hola Chavales"))# Cuenta cuantos carcteres hay
print(type(18))
print("Chavales".upper())

"""
Variables locales y globales
"""

global_var = "Python"

def hello_python():
     locals_var = "Hola"
     print(f"{locals_var},{global_var}!")

print(global_var)
# print (local_var) No se puede acceder desde fuera de la funcion

hello_python()

"""
Difucultad Extra
"""

def print_numbers(text_1, text_2) -> int:
     count = 0
     for number in range(1,101):
        if number % 3 == 0 and number % 5 == 0:
            print(text_1 + text_2)
        elif number % 3 == 0:
            print(text_1)
        elif number % 5 == 0:
            print(text_2)
        else: 
            print(number)
            count += 1
     return count

print(print_numbers("Fizz","Buzz"))
