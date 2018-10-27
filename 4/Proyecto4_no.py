
def busca_movimientos(tablero, turno):
    movimientos = list()
    for i in range(8):
        for j in range(8):
            if tablero[i][j] == ".":
                if i > 0:
                    if tablero[i-1][j] == ".":
                        movimientos.insert(0, [i-1,j])
                if i < 8:
                    if tablero[i+1][j] == ".":
                        movimientos.insert(0, [i+1,j])
                if j > 0:
                    if tablero[i][j-1] == ".":
                        movimientos.insert(0, [i,j-1])
                if j < 8:
                    if tablero[i][j+1] == ".":
                        movimientos.insert(0, [i,j+1])
                if i > 0 and j > 0:
                    if tablero[i-1][j-1] == ".":
                        movimientos.insert(0, [i-1,j-1])
                if i < 8 and j < 8:
                    if tablero[i+1][j+1] == ".":
                        movimientos.insert(0, [i+1,j+1])
                if i > 0 and j < 8:
                    if tablero[i-1][j+1] == ".":
                        movimientos.insert(0, [i-1,j+1])
                if j > 0 and i < 8:
                    if tablero[i+1][j-1] == ".":
                        movimientos.insert(0, [i+1,j-1])
    return movimientos

def gira_fichas(movimiento, tablero, color):
    x, y = movimiento
    tablero[x][y] = color
    i = x
    j = y
    while i+1 <= 8:
        if tablero[i][j] == color:
            oldi = i
            i = x
            while i < oldi:
                tablero[i][j] = color
                i += 1
                break
        i += 1
    while j+1 <= 8:
        if tablero[i][j] == color:
            oldj = j
            j = y
            while j < oldj:
                tablero[i][j] = color
                j += 1
            break
        j += 1

    i = x
    j = y
    while i-1 >= 0:
        if tablero[i][j] == color:
            oldi = i
            i = x
            while i < oldi:
                tablero[i][j] = color
                i -= 1
                break
        i -= 1
    while j-1 >= 0:
        if tablero[i][j] == color:
            oldj = j
            j = y
            while j < oldj:
                tablero[i][j] = color
                j -= 1
            break
        j -= 1
    # Faltan las diagonales :|
    


def othelo(nivel, fichas, inicio):
    tablero = ["x"] * 8
    for i in range(8):
        tablero[i] = ["."] * 8
    tablero[4][4] = "0"
    tablero[3][3] = "0"
    tablero[3][4] = "1"
    tablero[4][3] = "1"

    for i in range(8):
        print(tablero[i])

def minimax():



othelo(1,1,1)
