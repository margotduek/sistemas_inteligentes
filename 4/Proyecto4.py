import os
import copy
n = 8
tablero = [['.' for x in range(n)] for y in range(n)]
dirx = [-1, 0, 1, -1, 1, -1, 0, 1]
diry = [-1, -1, -1, 0, 0, 1, 1, 1]
boardminimo = -1
boardmaximo = n * n + 4 * n + 4 + 1

abc = ['A','B','C','D','E','F','G','H']

def crear_tablero():
    if n % 2 == 0:
        z = int((n - 2) / 2)
        tablero[z][z] = '1'
        tablero[n - 1 - z][z] = '0'
        tablero[z][n - 1 - z] = '0'
        tablero[n - 1 - z][n - 1 - z] = '1'



def movimiento_valido(tablero, x, y, jugador):
    if x < 0 or x > n - 1 or y < 0 or y > n - 1:
        return False
    if tablero[y][x] != '.':
        return False
    (tableroTemp, tot_taken) = haz_movimiento(copy.deepcopy(tablero), x, y, jugador)
    if tot_taken == 0:
        return False
    return True


def revisa_nodo_ultimo(tablero, jugador):
    for y in range(n):
        for x in range(n):
            if movimiento_valido(tablero, x, y, jugador):
                return False
    return True


def imprime_tablero():
    m = len(str(n - 1))
    for y in range(n):
        row = ''
        for x in range(n):
            row += tablero[y][x]
            row += ' ' * m
        print(row + ' ' + str(y))
    print()
    row = ''
    for x in range(n):
        row += abc[x].zfill(m) + ' '
    print(row + '\n')


def haz_movimiento(tablero, x, y, jugador):
    tot_taken = 0
    tablero[y][x] = jugador
    for d in range(8):
        taken = 0
        for i in range(n):
            dx = x + dirx[d] * (i + 1)
            dy = y + diry[d] * (i + 1)
            if dx < 0 or dx > n - 1 or dy < 0 or dy > n - 1:
                taken = 0; break
            elif tablero[dy][dx] == jugador:
                break
            elif tablero[dy][dx] == '.':
                taken = 0; break
            else:
                taken += 1
        for i in range(taken):
            dx = x + dirx[d] * (i + 1)
            dy = y + diry[d] * (i + 1)
            tablero[dy][dx] = jugador
        tot_taken += taken
    return (tablero, tot_taken)


def revisa_tablero(tablero, jugador):
    total = 0
    for y in range(n):
        for x in range(n):
            if tablero[y][x] == jugador:
                if (x == 0 or x == n - 1) and (y == 0 or y == n - 1):
                    total += 4 # corner
                elif (x == 0 or x == n - 1) or (y == 0 or y == n - 1):
                    total += 2 # side
                else:
                    total += 1
    return total


def Minimax(tablero, jugador, depth, maximizingPlayer):
    if depth == 0 or revisa_nodo_ultimo(tablero, jugador):
        return revisa_tablero(tablero, jugador)
    # Max current jugador
    if maximizingPlayer:
        bestValue = boardminimo
        for y in range(n):
            for x in range(n):
                if movimiento_valido(tablero, x, y, jugador):
                    (tableroTemp, tot_taken) = haz_movimiento(copy.deepcopy(tablero), x, y, jugador)
                    v = Minimax(tableroTemp, jugador, depth - 1, False)
                    bestValue = max(bestValue, v)
    else:
        bestValue = boardmaximo
        for y in range(n):
            for x in range(n):
                if movimiento_valido(tablero, x, y, jugador):
                    (tableroTemp, tot_taken) = haz_movimiento(copy.deepcopy(tablero), x, y, jugador)
                    v = Minimax(tableroTemp, jugador, depth - 1, True)
                    bestValue = min(bestValue, v)
    return bestValue

def el_mejor(tablero, jugador, depth):
    maxPoints = 0
    mx = -1; my = -1
    for y in range(n):
        for x in range(n):
            if movimiento_valido(tablero, x, y, jugador):
                (tableroTemp, tot_taken) = haz_movimiento(copy.deepcopy(tablero), x, y, jugador)
                points = Minimax(tableroTemp, jugador, depth, True)
                if points > maxPoints:
                    maxPoints = points
                    mx = x; my = y
    return (mx, my)

# Ascii value to int for x-axis position
def ascci2pos(asc):
    return int(ord(asc)-65)

# Main function that implements functionality
def othello(level=4, bow=1, start=0):
    global tablero
    jugador = '0'
    if bow == 0:
        com = '0'
        jugador = '1'
    elif bow == 1:
        com = '1'
        jugador = '0'
    else:
        print("Color Invalido")
        os._exit(0)
    if int(start) > 1 and int(start) < 0:
        print("Comienzo invalido")
        os._exit(0)
    crear_tablero()
    while True:
        for p in range(2):
            imprime_tablero()
            print ('jugador: {}'.format(str(p+1)))
            if revisa_nodo_ultimo(tablero, jugador):
                print('Ya no puedes jugar, se acabó el juego :( ')
                print('Score de la persona: ' + str(revisa_tablero(tablero, jugador)))
                print ('Score de la máquina  : ' + str(revisa_tablero(tablero, com)))
                os._exit(0)
            if p == int(start): # user's turn
                while True:
                    xy = input('X Y: ')
                    if xy == '': os._exit(0)
                    x = ascci2pos(xy[0].upper())
                    y = int(xy[1])
                    if movimiento_valido(tablero, x, y, jugador):
                        (tablero, tot_taken) = haz_movimiento(tablero, x, y, jugador)
                        print('# de fichas del color : ' + str(tot_taken))
                        break
                    else:
                        print('haz un movimiento que sea valido ')
            else:
                (x, y) = el_mejor(tablero, com, level)
                if not (x == -1 and y == -1):
                    (tablero, tot_taken) = haz_movimiento(tablero, x, y, com)
                    print('LA compu tiró (X Y): ' + str(x) + ' ' + str(y))
                    print('# de fichas del color : ' + str(tot_taken))


othello(1,0,0)
