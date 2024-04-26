"""
EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
"""

class Programmer:

    surname: str = None

    def __init__(self, name: str, age: int, languages: list):
        self.name = name
        self.age = age
        self.languages = languages
    
    def print(self):
        print(
            f"Nombre: {self.name} | Apellidos: {self.surname} | Edd: {self.age} | Lenguajes: {self.languages}")

my_programmer = Programmer("Feluco", 18, ["Gran canaria", "Python", "Chavales"])
my_programmer.print()
my_programmer.surname = "Canarias"
my_programmer.print()
my_programmer.age = 18
my_programmer.print()


"""
DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
"""

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop (self):
        if self.count() == 0:
            return None
        return self.stack.pop()
    
    def count (self):
        return len (self.stack)
    
    def print (self):
        for item in reversed(self.stack):
            print(item)

my_stack = Stack()
my_stack.push("A")
my_stack.push("B")
my_stack.push("C")
print(my_stack)
my_stack.print()
my_stack.pop()
print(my_stack.count())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.count())

#FIFO

class Queue:

    def __init__(self):
        self.queue = []
  
    def equeue(self, item):
        self.append:(item)
    
    def deequeue(self):
            if self.count() == 0:
                return None
            return self.queue.pop(0)
    
    def count(self):
        return len (self.queue)
    
    def print(self):
        for item in self.queue:
            print(item)

my_queue = Queue()
my_queue.equeue("A")
my_queue.equeue("B")
my_queue.equeue("C")
print(my_queue.count())
my_queue.print()
my_queue.deequeue()
print(my_queue.count())
print(my_queue.deequeue())
print(my_queue.deequeue())
print(my_queue.deequeue())
print(my_queue.deequeue())
print(my_queue.deequeue())
print(my_queue.count())
