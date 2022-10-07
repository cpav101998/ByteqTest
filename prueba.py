

                                                                #Prueba Test Byteq


from collections import deque
 
 
# Creo una clase para representar el obejto graph 
class Graph:
    # Constructor
    def __init__(self, edges, n):
 
        # Lista de listas para representar una lista de adyacencia
        self.adjList = [[] for _ in range(n)]
 
        for (src, dest) in edges:
            
            self.adjList[src].append(dest)
 
def BFS(g, source, n):
 
    # Crear una queue para hacer BFS
    q = deque()
 
    # Realizar un seguimiento de si se descubre un vértice o no
    discovered = [False] * (n + 1)
 
    # Marca el vértice de origen como descubierto
    discovered[source] = True
 
    # Asignar la distancia mínima del vértice fuente como 0 y
    q.append((source, 0))
 
    while q:

        vertex, min_dist = q.popleft()
 
        if vertex == n:
            return min_dist
 
        for u in g.adjList[vertex]:
            if not discovered[u]:
                # Marcar como descubierto y ponerlo en queue
                discovered[u] = True
 
                # AsignaR la distancia mínima del nodo actual
                q.append((u, min_dist + 1))
 
 
def findMinimumMoves(ladder, snake):
 
    # Número total de nodos en el graph
    n = 10 * 10 
 
    # Encuentrar todos los bordes involucrados y los almacena en una lista
    edges = []
    for i in range(n):
 
        j = 1
        while j <= 6 and i + j <= n:
            src = i
            # Destino de actualización # si hay alguna escalera
            # o serpiente desde la posición actual.
            _ladder = ladder.get(i + j) if (ladder.get(i + j)) else 0
            _snake = snake.get(i + j) if (snake.get(i + j)) else 0
 
            if _ladder or _snake:
                dest = _ladder + _snake
            else:
                dest = i + j
 
            edges.append((src, dest))
 
            j = j + 1
 
    # Construye un grafo dirigido
    g = Graph(edges, n)
 
    # Encuentra el camino más corto entre 1 y 100 usando BFS
    return BFS(g, 0, n)
 
 
if __name__ == '__main__':
 
    # Las serpientes y las escaleras se representan mediante un diccionario.
    ladder = {}
    snake = {}
 
    # insertar escaleras en el diccionario
    ladder[2] = 38
    ladder[21] = 42
    ladder[15] = 26
    ladder[7] = 14
    ladder[8] = 31
    ladder[36] = 44
    ladder[28] = 84
    ladder[78] = 98
    ladder[84] = 28
    ladder[71] = 91
    ladder[51] = 67
 
    # insertar serpientes en el diccionario
    snake[80] =99
    snake[75] = 95
    snake[88] = 92
    snake[68] = 89
    snake[11] = 49
    snake[60] = 64
    snake[95] = 75
    snake[98] = 79
    snake[25] = 46
    snake[6] = 16
    snake[53] = 74

    
 
    print(findMinimumMoves(ladder, snake))