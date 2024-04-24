"""
Operadores
"""

# Operadores arimetricos (Suma,Resa,Multiplicar,
# dividir,Modulo,Exponente y Division con numero entero)
print(f"Suma: 30 + 3 = {30 + 3}")
print(f"Reesta: 30 - 3 = {30 - 3}")
print(f"Multiplicacion: 30 * 3 = {30 * 3}")
print(f"Division: 30 / 3 = {30 / 3}")
print(f"Modulo: 30 % 3 = {30 % 3}")
print(f"Exponente: 30 ** 3 = {30 ** 3}")
print(f"Division entera: 30 // 3 = {30 // 3}")

#Operadores de Comparecion
print(f"Igualdad: 30 == 3 es {30 == 3}")# Si no es igual marcara Falso
print(f"Igualdad: 3 == 3 es {3 == 3}")# Si es igual marcara True
print(f"Desigualdad: 30 != 3 es {30 != 3}")# Si no es igual marcara True
print(f"Desigualdad: 3 != 3 es {3 != 3}")# Si es igual marcara Falso
print(f"Mayor que: 30 > 3 es {30 > 3}")# Si el numero (30)es mayor que el numero (3) Saldria si False o True
print(f"Menor que: 30 < 3 es {30 < 3}")# Si el numero (30)es menor que el numero (3) Saldria si False o True
print(f"Mayor o igual que: 30 >= 3 es {30 >= 30}")#Si el numero (30)es mayor o igual que el numero (3) Saldria si False o True
print(f"Menor o igual que: 30 <= 3 es {30 <= 3}")#Si el numero (30)es menor o igual que el numero (3) Saldria si False o True

#Operadores Logicos
print(f"AND (&&): 30 + 3 == 33 and 20 - 5 == 15 es {30 + 3 == 33 and 20 - 5 == 15}")# Si son las 2 verdaderas True 
print(f"AND (&&): 30 + 3 == 33 and 20 - 5 == 25 es {30 + 3 == 33 and 20 - 5 == 25}")# Si falla aunque sea 1 dice False
print(f"OR (||): 30 + 3 == 33 or 20 - 5 == 25 es {30 + 3 == 33 or 20 - 5 == 25}")# Si tiene bien aunque sea 1 dice True
print(f"OR (||): 30 + 3 == 34 or 20 - 5 == 25 es {30 + 3 == 34 or 20 - 5 == 25}")# Si son las 2 falsas False
print(f"NOT (!): not 30 + 3 == 34 {not 30 + 3 == 34}")# Si niego de que sea verdad y no es verdad me saldra True
print(f"NOT (!): not 30 + 3 == 33 {not 30 + 3 == 33}")# Si niego de que sea verdad y es verdad me saldra False

# Operadores de asignacion
my_number = 20  # asignacion
print(my_number)
my_number += 5 # suma y asignacion
print(my_number)
my_number -= 5 # resta y asignacion
print(my_number)
my_number *= 5 # multiplicacion y asignacion
print(my_number)
my_number /= 5 # division y asignacion
print(my_number)
my_number %= 5 # modulo y asignacion
print(my_number)
my_number **=20  # exponente y asignacion
print(my_number)
my_number //= 5 # division entera y asignacion

#Operadores de Identidad
my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number}")# Igualdad
print(f"my_number is not my_new_number es {my_number is not my_new_number}")# Desigualdad

# Operador de pertenencia
print(f"'u' in 'mouredev' = {'u'in 'mouredev'}")# Esta La letra U en la palabra mouredev
print(f"'b' not in 'mouredev' = {'b' not in 'mouredev'}")# No esta La letra B en la palabra mouredev


# Operador de bit
a = 10 #1010 binario
b = 3 #0011 binario
print(f"ABD: 10 & 3 = {10 & 3}") # 0010 = 2 
print(f"OR: 10 | 3 = {10 | 3}") # 1011 = 11
print(f"XOR: 10 ^ 3 = {10 ^ 3}") # 1001 = 9
print(f"NOT: ~10 = { ~10}") # Niega todos los bits intecambia los bits
print(f"Desplazamiento a la derecha: 10 >> 2 = { 10 >> 2}") # Pasa a la derecha los bit (2) posiciones del 1010 = 0010
print(f"Desplazamiento a la izquierda: 10 << 2 = { 10 << 2}") # Pasa a la izquierda los bit (2) posiciones del 1010 = 0010

'''
Estructuras de control
'''

# Condicionales 
my_string = "Feluco" # Siempre se va ejecutar la que se cumple

if my_string == "Feluco":
    print("my_string es 'Feluco'") # Si dice la palabra que hesmo puesto en my_string igual saldra esa frase

elif my_string == "Programador": 
    print("my_string es 'Programador'") # Otra comprobacion 

else:
    print("my_string no es 'Feluco' ni Programador ") # Si no dice la palabra que hesmo puesto en my_string igual saldra esa frase

 # Iterativas

for i in range (6): # Pone en bucle todos los numeros (1,2,3,4,5) menos es que el ne pone siempre queda uno menos
    print(i)

i= 0 # Le asignamos un valor 

while i <= 10: # Le decimos que pare cundo sea mayor o igual que 10
    print(i)
    i += 1   # Y que vaya sumando cada vez mas 1 al valor (i)

# Manejo de excepciones 
try:
    print(10 / 0)
except:
    print("Se ha producido un fallo Feluco") # Mensaje cuando de fallo
finally:
    print("Ha finalizado el manejo de excepciones") # Mensaje para no quedar pillado      

'''
Dificultad Extra
'''
for number in range(10, 56):
    if number %2 == 0 and number != 16 and number % 3 != 0:
            print(number)
