# N = 8     # o el número de reinas que tenga el problema
# lateral = true # o false
# M = 5     # o el número máximo que se desee reiniciar
# busquedaHC(N, lateral, M)

import copy
import time
import operator
import random

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

def create_matrix(N):
    matrix = [0] * N
    for i in range(N):
        matrix[i] = [0] * N
    for i in range(N):
        x = random.randint(0, N-1)
        print(N, x)
        matrix[i][x] = 1
    return matrix


def busquedaHC(N, lateral, M):
    # creamos una matriz con solamente 1 Q por row
    matrix = create_matrix(N)
    sin_laterales(N, matrix)



def sin_laterales(N, matrix):
    q_limpias = 0
    i = 0
    j = 0
    while i < len(matrix):
        while j < len(matrix):
            if matrix[i][j] == 1:
                if matrix[i+1][j+1] == 1:
                    # temp = copy.deepcopy(matrix)
                    matrix[i][j] = 0
                    if j < N:
                        matrix[i][j-1] = 1
                        #lo guardamos en un nodo o algo asi
                        i += 1
                elif matrix[i-1][j-1] == 1:
                        # temp = copy.deepcopy(matrix)
                        matrix[i][j] = 0
                        if j < N:
                            matrix[i][j+1] = 1
                            #lo guardamos en un nodo o algo asi
                            i += 1
                elif matrix[i+1][j-1] == 1:
                        # temp = copy.deepcopy(matrix)
                        matrix[i][j] = 0
                        if j < N:
                            matrix[i][j+1] = 1
                            #lo guardamos en un nodo o algo asi
                            i += 1
                elif matrix[i-1][j+1] == 1:
                        # temp = copy.deepcopy(matrix)
                        matrix[i][j] = 0
                        if j < N:
                            matrix[i][j-1] = 1
                            #lo guardamos en un nodo o algo asi
                            i += 1

                    # lo metemos en un nodo
                else:
                    q_limpias += 1
        if q_limpias == N-1:
            print(matrix)
            return matrix
            j += 1
        j = 0
    print("listo")


busquedaHC(8, True, 4)
