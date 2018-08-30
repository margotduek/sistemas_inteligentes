
# Un tour por Rumania
## Estado Inicial
  Arad ( para este prolema debe de ser una ciudad )
## Acciones posibles
  Recorrer una carretera
## Modelo de transición
  T(ciudad, carretera (i - j), cudad)
## Prueba meta
  Bucharest ( una ciudad )
## Costo del camino
  La suma de las distancias de las carreteras recorridas


# 8 puzzle
## Estado Inicial
  Una posición inicial del 8puzzle
## Acciones posibles
  Mover un número al espacio vacío siempre y cuando esté contiguo siempre y cuando se pueda
## Modelo de transición
  T(estado i del puzzle, accioón (U,D,L,R), estado j del puzzle)
  Tengo una función que le mando las acciones, si no devuelve nada es que no se pudo
  En este caso, habrían 2 posibilidades, moviendo el espacio en blanco para abajo o a la derecha
  algo que podría ayudar es una lista de estados visitados
## Prueba meta
  estado final
## Costo del camino
  la suma de las acciones


# 8 reinas
## Estado Inicial
  * Tablero vacío
  * Posición inicial del tablero
  * Tablero inicial lleno de reinas y quitar hasta que queden 8
## Acciones posibles
  Si el tablero está vacío
    * colocar una reina en el tablero en algún lugar donde no haya reina y donde no pueda atacar
  Si es posición inicial del Tablero
    * mover a la reina a un lugar donde no sea atacada
## Modelo de transición
  ()
## Prueba meta
## Costo del camino
