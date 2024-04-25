"""
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
"""

'Operaciones'

s1 = "Feluco"
s2 = "Canarias"
s3 = "Hoy juega Las palmas contra el girona"

# Concatenacion
print(s1 + ", " + s2 + "!")

# Repeticion
print(s1 * 4)

# Indexacion
print(s2[0] + s2[1] + s2[2] + s2[3])

# Logintud
print(len(s2))

# Porcion
print(s2[3:]) # Hasta el final (:)
print(s2[5:8]) #Otra manera de coger un rango de caracteres
print(s2[: 4]) # Desde el principio (:)

# Busqueda
print("n" in s2) # Si esta el caracter en la palabra s2(Canaria) True
print("i" in s1) # Si esta el caracter en la palabra s1(Feluco)  False

# Reemplazo
print(s2.replace("a", "o")) #Cambiar una letra por otra 
print(s1.replace("o", "a"))

# Division
print(s2.split("n"))

# Mayusculas, mminuscalas y letras en mayusculas
print(s2.upper())#Todo en mayusculas
print(s1.lower())#Todo en minusculas 
print(s3.title()) #Siempre la primera letra de la palabra en mayusculas
print(s3.capitalize()) #Solo la primera letra de la primera palabra en mayusculas

# Eliminacion de espacios al principio y al final
print(" Hoy juega las palmas" .strip ()+ "En casa")

#Busqueda al principi y al final
print(s2.startswith("Ca"))
print(s2.startswith("Fe"))
print(s1.endswith("as"))
print(s1.endswith("co"))

# busqueda de posicion
print(s3.find("girona"))
print(s3.find("Las"))
print(s3.find("L"))
print(s3.lower().find("girona"))

# Busqueda de ocurrencias 
print(s3.lower().count("a"))#Cuantos caracteres tiene "a" en (s3) 

#Formateo
print("Saludo: {}, lenguaje: {}!".format(s1, s2))
print(f"Saludo: {s1}, lenguaje: {s2}!")# Disitnta manera de hacer

# Transformacion en lista de caracteres
print(list(s3))

# Transformacion en lista en cadena
l1 =[s1, ",", s2, "!"]
print("".join(l1))

 # Transformaciones numericas
s4 = "123456"
s4 = int(s4)
print(s4)

s5 = "123456.78"
s5 = float(s5) #Numero decimal
print(s5)

# Comprobaciones varias
s4 = "123456"
print(s1.isalnum())#Si contiene Letra y Numeros 
print(s4.isalpha())# Si Contiene solo letras
print(s4.isnumeric())# Si es un numero
 
"""
DIFICULTAD EXTRA (opcional):
* Crea un programa que analice dos palabras diferentes y realice comprobaciones
* para descubrir si son:
* - Palíndromos
* - Anagramas
* - Isogramas
"""
def check(word1: str, word2: str):

    # Palindromos
    print(f"¿{word1} es un palindromo?: {word1 == word1[::-1]}")
    print(f"¿{word2} es un palindromo?: {word2 == word2[::-1]}")

    # Anagramas
    print(f"¿{word1} es un anagrama de {word2}?: {sorted(word1) == sorted(word2)}")

    # Isogramas

    def isogram(word: str) -> bool:

        word_dict = dict()
        for character in word:
            word_dict[character] = word_dict.get(character, 0) + 1

        isogram = True
        values = list(word_dict.values())
        isogram_len = values[0]
        for word_count in values:
            if word_count != isogram_len:
                isogram = False
                break

        return isogram
    
    print(f"¿{word1} es un isograma?: {isogram(word1)}")
    print(f"¿{word2} es un isograma?: {isogram(word2)}")

check("radar", "Feluco")
# check("amor", "roma")
