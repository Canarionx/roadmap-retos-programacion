'''
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
'''

'''
Las pilas son tipos abstactos de datos que se encuentran en un formato de tipo lista
a cuyos elementos se accede de una forma particular (LIFO) Last In First Out que se puede 
traducir como "Lo último en entrar será lo último en salir"
'''

# Pila/Stack (LIFO)

stack = []

# push
stack.append("1")
stack.append("2")
stack.append("3")
print(stack)

# pop
stack_item = stack[len(stack) - 1]
del stack[len(stack) - 1]
print(stack_item)

print(stack.pop())

print(stack)

# Cola/Queue (FIFO)

queue = []

# enqueue
queue.append(1)
queue.append(2)
queue.append(3)

print(queue)

# dequeue
queue_item = queue[0]
del queue[0]
print(queue_item)

print(queue.pop(0))

print(queue)

'''
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 */
'''
 # Web

def web_navigation():
 
    stack = []

    while True:
      
        action = input(
           "Añade una url o interactua con palabras adelante/atras/salir:"
        )

        if action == "salir":
            print("Saliendo del navegador web.")
            break
        elif action == "adelante":
           pass
        elif action == "atras":
           if len(stack) > 0:
              stack.pop()
        else:
           stack.append(action)
        
        if len(stack) > 0:
           print(f"Has navegado a la web: {stack[len(stack) - 1]}")
        else:
           stack.append(action)

        if len(stack) > 0:
           print(f"Has navegado a la web: {stack[len(stack) - 1]}.")
        else:
           print("Estas en la pagina de inicio.")


web_navigation()

def shared_printed():
   
   queue = []

   while True:
      
        action = input("Añade un documento o selecciona imprimir/salir:")
        
        if action == "salir":
            break
        elif action == "imprimir":
           if len(queue) > 0:
            print(f"Imprimiendo: {queue.pop(0)}")
           pass
        else:
           queue.append(action)
        
        print(f"Cola de impresion: {queue}")

shared_printed()
