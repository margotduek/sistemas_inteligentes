
# El estado inicial es una lista de listas, donde cada lista
#       interna contendrá 3 dígitos del 0 al 8 representa un renglón del 8‐puzzle.
#       El espacio serárepresentado por el número 0
# El estado meta que estará representado de la misma manera


import copy
import time
import operator

# El dad de la raiz debe de ser 0
class Node(object):
    def __init__(self, value, dad, movement, h):
        self.value = value
        self.dad = dad
        self.movement = movement
        self.h = h

# Clase queue tomada de https://www.pythoncentral.io/use-queue-beginners-guide/
class Queue:
    #Constructor creates a list
    def __init__(self):
        self.queue = list()

    #Adding elements to queue
    def enqueue(self,data):
        #Checking to avoid duplicate h_fichas(temp, final)entry (not mandatory)
        if data not in self.queue:
            self.queue.insert(0,data)
            return True
        return False

    def sort(self, h):
        self.queue.sort(key=operator.attrgetter('h'))
        return self.queue

    #Adding elements to queue
    def enqueuestack(self,data, pos):
        #Checking to avoid duplicate entry (not mandatory)
        if data not in self.queue:
            self.queue.insert(pos,data)
            return True
        return False

    #Removing the last element from the queue
    def dequeue(self):
        if len(self.queue)>0:
            return self.queue.pop(0)
        return ("Queue Empty!")


    #Getting the size of the queue
    def size(self):
        return len(self.queue)

def lo_metemos(x, visitados):
    if x in visitados:
        # print("F")
        # print("F --> " , x)
        return False
    visitados.insert(0,x)
    # print("T")
    return True

def calculate_h_fichas(x, final):
    h = 0
    i = 0
    j = 0
    while i < len(x):
        while j < len(x):
            if x[i][j] != final[i][j]:
                h = h + 1
            j += 1
        j = 0
        i += 1
    return h

def calculate_manhattan(x, final):
    h = 0
    i = 0
    j = 0
    while i < len(x):
        while j < len(x):
            if x[i][j] != final[i][j]:
                val = x[i][j]
                posi = [(index, row.index(val)) for index, row in enumerate(final) if val in row]
                posii = posi[0]
                h += abs(posii[0] - i)
                h += abs(posii[1] - j)

            j += 1
        j = 0
        i += 1
    return h




#inicial y final son nodos
def bfs(inicial, final):
    bfs_queue = Queue()
    visitados = list()
    bfs_queue.enqueue(inicial)
    actual = inicial.value

    while actual != final.value:
        actual_node = bfs_queue.dequeue()
        actual = actual_node.value
        i = 0
        j = 0
        h = 0
        while (i < len(actual)):
            while(j < len(actual[i]) ):
                # Buscar el cero
                if actual[i][j] == 0:
                    #intercambiar el cero
                    if j > 0 and j < 2:
                        temp = copy.deepcopy(actual)
                        temp[i][j] = actual[i][j-1]
                        temp[i][j-1] = 0
                        if lo_metemos(temp, visitados):
                            h = calculate_h_fichas(temp, final.value)
                            bfs_queue.enqueuestack(Node(temp, actual_node, "L", h),bfs_queue.size())

                        temp = copy.deepcopy(actual)
                        temp[i][j] = actual[i][j+1]
                        temp[i][j+1] = 0
                        if lo_metemos(temp, visitados):
                            h = calculate_h_fichas(temp, final.value)
                            bfs_queue.enqueuestack(Node(temp, actual_node, "R", h),bfs_queue.size())
                    if i > 0 and i < 2:
                        temp = copy.deepcopy(actual)
                        temp[i][j] = actual[i-1][j]
                        temp[i-1][j] = 0
                        if lo_metemos(temp, visitados):
                            h = calculate_h_fichas(temp, final.value)
                            bfs_queue.enqueuestack(Node(temp, actual_node, "U", h),bfs_queue.size())


                        temp = copy.deepcopy(actual)
                        temp[i][j] = actual[i+1][j]
                        temp[i+1][j] = 0
                        if lo_metemos(temp, visitados):
                            h = calculate_h_fichas(temp, final.value)
                            bfs_queue.enqueuestack(Node(temp, actual_node, "D", h),bfs_queue.size())
                    if j == 0:
                        temp = copy.deepcopy(actual)
                        temp[i][j] = actual[i][j+1]
                        temp[i][j+1] = 0
                        if lo_metemos(temp, visitados):
                            h = calculate_h_fichas(temp, final.value)
                            bfs_queue.enqueuestack(Node(temp, actual_node, "R", h),bfs_queue.size())
                    if j == 2:
                        temp = copy.deepcopy(actual)
                        temp[i][j] = actual[i][j-1]
                        temp[i][j-1] = 0
                        if lo_metemos(temp, visitados):
                            h = calculate_h_fichas(temp, final.value)
                            bfs_queue.enqueuestack(Node(temp, actual_node, "L", h),bfs_queue.size())
                    if i == 0:
                        temp = copy.deepcopy(actual)
                        temp[i][j] = actual[i+1][j]
                        temp[i+1][j] = 0
                        if lo_metemos(temp, visitados):
                            h = calculate_h_fichas(temp, final.value)
                            bfs_queue.enqueuestack(Node(temp, actual_node, "D", h),bfs_queue.size())
                    if i == 2:
                        temp = copy.deepcopy(actual)
                        temp[i][j] = actual[i-1][j]
                        temp[i-1][j] = 0
                        if lo_metemos(temp, visitados):
                            h = calculate_h_fichas(temp, final.value)
                            bfs_queue.enqueuestack(Node(temp, actual_node, "U", h),bfs_queue.size())
                    bfs_queue.sort(h)
                j+=1
            j = 0
            i+=1
        i = 0

    # Imprimir los valores de las matrices
    while actual_node.movement != "NA":
        print(actual_node.value)
        print('*******')
        print('*     *')
        print('* ' , actual_node.movement, ' *')
        print('*     *')
        print('*******')
        actual_node = actual_node.dad



#inicial y final son nodos
def bfs2(inicial, final):
    bfs_queue = Queue()
    visitados = list()
    bfs_queue.enqueue(inicial)
    actual = inicial.value

    while actual != final.value:
        actual_node = bfs_queue.dequeue()
        actual = actual_node.value
        i = 0
        j = 0
        h = 0
        while (i < len(actual)):
            while(j < len(actual[i]) ):
                # Buscar el cero
                if actual[i][j] == 0:
                    #intercambiar el cero
                    if j > 0 and j < 2:
                        temp = copy.deepcopy(actual)
                        temp[i][j] = actual[i][j-1]
                        temp[i][j-1] = 0
                        if lo_metemos(temp, visitados):
                            h = calculate_manhattan(temp, final.value)
                            bfs_queue.enqueuestack(Node(temp, actual_node, "L", h),bfs_queue.size())

                        temp = copy.deepcopy(actual)
                        temp[i][j] = actual[i][j+1]
                        temp[i][j+1] = 0
                        if lo_metemos(temp, visitados):
                            h = calculate_manhattan(temp, final.value)
                            bfs_queue.enqueuestack(Node(temp, actual_node, "R", h),bfs_queue.size())
                    if i > 0 and i < 2:
                        temp = copy.deepcopy(actual)
                        temp[i][j] = actual[i-1][j]
                        temp[i-1][j] = 0
                        if lo_metemos(temp, visitados):
                            h = calculate_manhattan(temp, final.value)
                            bfs_queue.enqueuestack(Node(temp, actual_node, "U", h),bfs_queue.size())


                        temp = copy.deepcopy(actual)
                        temp[i][j] = actual[i+1][j]
                        temp[i+1][j] = 0
                        if lo_metemos(temp, visitados):
                            h = calculate_manhattan(temp, final.value)
                            bfs_queue.enqueuestack(Node(temp, actual_node, "D", h),bfs_queue.size())
                    if j == 0:
                        temp = copy.deepcopy(actual)
                        temp[i][j] = actual[i][j+1]
                        temp[i][j+1] = 0
                        if lo_metemos(temp, visitados):
                            h = calculate_manhattan(temp, final.value)
                            bfs_queue.enqueuestack(Node(temp, actual_node, "R", h),bfs_queue.size())
                    if j == 2:
                        temp = copy.deepcopy(actual)
                        temp[i][j] = actual[i][j-1]
                        temp[i][j-1] = 0
                        if lo_metemos(temp, visitados):
                            h = calculate_manhattan(temp, final.value)
                            bfs_queue.enqueuestack(Node(temp, actual_node, "L", h),bfs_queue.size())
                    if i == 0:
                        temp = copy.deepcopy(actual)
                        temp[i][j] = actual[i+1][j]
                        temp[i+1][j] = 0
                        if lo_metemos(temp, visitados):
                            h = calculate_manhattan(temp, final.value)
                            bfs_queue.enqueuestack(Node(temp, actual_node, "D", h),bfs_queue.size())
                    if i == 2:
                        temp = copy.deepcopy(actual)
                        temp[i][j] = actual[i-1][j]
                        temp[i-1][j] = 0
                        if lo_metemos(temp, visitados):
                            h = calculate_manhattan(temp, final.value)
                            bfs_queue.enqueuestack(Node(temp, actual_node, "U", h),bfs_queue.size())
                    bfs_queue.sort(h)
                j+=1
            j = 0
            i+=1
        i = 0

    # Imprimir los valores de las matrices
    while actual_node.movement != "NA":
        print(actual_node.value)
        print('*******')
        print('*     *')
        print('* ' , actual_node.movement, ' *')
        print('*     *')
        print('*******')
        actual_node = actual_node.dad


def busquedaAstar(edoInicial, edoFinal, hueristica):
    i = Node(edoInicial, 0, "NA", 0)
    f = Node(edoFinal, 0, "NA", 0)
    if hueristica == 1:
        print("Manhattan: ")
        bfs2(i, f)
    elif hueristica == 0:
        print("Fichas: ")
        bfs(i, f)
    else:
        print("ponga un valor que sea valido")



# edoInicial = [[0, 1, 2], [4, 5, 3], [7, 8, 6]]
# edoFinal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
edoInicial = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
edoFinal = [[3, 1, 2], [4, 5, 8], [6, 7, 0]]
# edoFinal = [[1, 2, 5], [3, 0, 4], [6, 7, 8]]

# edoFinal = [[1, 4, 2], [3, 5, 0], [6, 7, 8]]
busquedaAstar(edoInicial, edoFinal, 1)
time.sleep(5)
busquedaAstar(edoInicial, edoFinal, 0)
