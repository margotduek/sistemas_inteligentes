
# El estado inicial es una lista de listas, donde cada lista
#       interna contendrá 3 dígitos del 0 al 8 representa un renglón del 8‐puzzle.
#       El espacio serárepresentado por el número 0
# El estado meta que estará representado de la misma manera
# en algoritmo, 0 es BFS y 1 es DFS


import copy

# El dad de la raiz debe de ser 0
class Node(object):
    def __init__(self, value, dad, movement):
        self.value = value
        self.dad = dad
        self.movement = movement

# Clase queue tomada de https://www.pythoncentral.io/use-queue-beginners-guide/
class Queue:
  #Constructor creates a list
  def __init__(self):
      self.queue = list()

  #Adding elements to queue
  def enqueue(self,data):
      #Checking to avoid duplicate entry (not mandatory)
      if data not in self.queue:
          self.queue.insert(0,data)
          return True
      return False

  #Removing the last element from the queue
  def dequeue(self):
      if len(self.queue)>0:
          return self.queue.pop()
      return ("Queue Empty!")

  #Getting the size of the queue
  def size(self):
      return len(self.queue)


#inicial y final son nodos
def bfs(inicial, final):
    bfs_queue = Queue()
    bfs_queue.enqueue(inicial)
    actual = inicial.value
    while actual != final.value:
        actual_node = bfs_queue.dequeue()
        actual = actual_node.value
        nuevo = actual_node
        i = 0
        j = 0
        while (i < len(actual)):
            while(j < len(actual[i]) ):
                # Buscar el cero
                if actual[i][j] == 0:
                    #intercambiar el cero
                    if j > 0 and j < 2:
                        temp = copy.deepcopy(actual)
                        temp[i][j] = actual[i][j-1]
                        temp[i][j-1] = 0
                        bfs_queue.enqueue(Node(temp, actual_node, "L"))

                        temp = copy.deepcopy(actual)
                        temp[i][j] = actual[i][j+1]
                        temp[i][j+1] = 0
                        bfs_queue.enqueue(Node(temp, actual_node, "R"))
                    if i > 0 and i < 2:
                        temp = copy.deepcopy(actual)
                        temp[i][j] = actual[i-1][j]
                        temp[i-1][j] = 0
                        bfs_queue.enqueue(Node(temp, actual_node, "U"))


                        temp = copy.deepcopy(actual)
                        temp[i][j] = actual[i+1][j]
                        temp[i+1][j] = 0
                        bfs_queue.enqueue(Node(temp, actual_node, "D"))
                    if j == 0:
                        temp = copy.deepcopy(actual)
                        temp[i][j] = actual[i][j+1]
                        temp[i][j+1] = 0
                        bfs_queue.enqueue(Node(temp, actual_node, "R"))
                    if j == 2:
                        temp = copy.deepcopy(actual)
                        temp[i][j] = actual[i][j-1]
                        temp[i][j-1] = 0
                        bfs_queue.enqueue(Node(temp, actual_node, "L"))
                    if i == 0:
                        temp = copy.deepcopy(actual)
                        temp[i][j] = actual[i+1][j]
                        temp[i+1][j] = 0
                        bfs_queue.enqueue(Node(temp, actual_node, "D"))
                    if i == 2:
                        temp = copy.deepcopy(actual)
                        temp[i][j] = actual[i-1][j]
                        temp[i-1][j] = 0
                        bfs_queue.enqueue(Node(temp, actual_node, "U"))
                j+=1
            i+=1
        # Imprimir los valores de las matrices
        while actual_node.movement != "NA":
            print(actual_node.value)
            print('*******')
            print('*     *')
            print('* ' , actual_node.movement, ' *')
            print('*     *')
            print('*******')
            actual_node = actual_node.dad




def busquedaNoInformada(edoInicial, edoFinal, algoritmo):
    i = Node(edoInicial, 0, "NA")
    f = Node(edoFinal, 0, "NA")
    if algoritmo == 0:
        bfs(i, f)
    # elif algoritmo == 1:
    #     dfs(i, f)
    else:
        print("ponga un valor que sea valido")



edoInicial = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
edoFinal = [[1, 2, 0], [3, 4, 5], [6, 7, 8]]

# edoFinal = [[1, 4, 2], [3, 5, 0], [6, 7, 8]]
busquedaNoInformada(edoInicial, edoFinal, 0)
