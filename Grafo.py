import heapq
from algoritmos import distancia_euclidiana

class Grafo:
    def __init__(self):
        self.grafo = {}
    
    def agregar_arista(self, origen, destino, peso):
        if origen not in self.grafo:
            self.grafo[origen] = []
        self.grafo[origen].append((destino, peso))
    
    def construir_desde_particulas(self, particulas):
        for particula in particulas:
            origen = (particula.origen_x, particula.origen_y)
            destino = (particula.destino_x, particula.destino_y)
            peso = particula.distancia
            self.agregar_arista(origen, destino, peso)
            self.agregar_arista(destino, origen, peso)  # Para asegurar que es no dirigido
    
    def mostrar_grafo(self):
        resultado = ""
        for origen, destinos in self.grafo.items():
            resultado += f"{origen} -> {destinos}\n"
        return resultado
    
    def distancia_entre_nodos(self, nodo1, nodo2):
        x1, y1 = nodo1
        x2, y2 = nodo2
        distancia = round( distancia_euclidiana(x1, y1, x2, y2), 2 )# Se redondea a 2 decimales
        return distancia
    
    def dijkstra(self, inicio):
        # Inicialización
        distancias = {nodo: float('infinity') for nodo in self.grafo}
        distancias[inicio] = 0
        cola_prioridad = [(0, inicio)]
        padres = {inicio: None}
        
        while cola_prioridad:
            distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)
            
            # Si la distancia actual es mayor que la almacenada, continuar
            if distancia_actual > distancias[nodo_actual]:
                continue
            
            # Explorar vecinos
            for vecino, peso in self.grafo.get(nodo_actual, []):
                distancia = distancia_actual + peso
                
                # Si se encuentra una distancia más corta
                if distancia < distancias[vecino]:
                    distancias[vecino] = distancia
                    padres[vecino] = nodo_actual
                    heapq.heappush(cola_prioridad, (distancia, vecino))
        
        return distancias, padres
    
    
    # Métodos para Kruskal
    def make_set(self, vertice):
        self.padre[vertice] = vertice
        self.rango[vertice] = 0

    def find(self, vertice):
        if self.padre[vertice] != vertice:
            self.padre[vertice] = self.find(self.padre[vertice])
        return self.padre[vertice]

    def union(self, vertice1, vertice2):
        raiz1 = self.find(vertice1)
        raiz2 = self.find(vertice2)

        if raiz1 != raiz2:
            if self.rango[raiz1] > self.rango[raiz2]:
                self.padre[raiz2] = raiz1
            else:
                self.padre[raiz1] = raiz2
                if self.rango[raiz1] == self.rango[raiz2]:
                    self.rango[raiz2] += 1

    def kruskal(self):
        # Inicializar estructuras para el algoritmo de Kruskal
        self.padre = {}
        self.rango = {}

        # Crear conjuntos disjuntos
        for vertice in self.grafo:
            self.make_set(vertice)

        # Crear lista de aristas con sus pesos
        aristas = []
        for origen in self.grafo:
            for destino, peso in self.grafo[origen]:
                aristas.append((peso, origen, destino))

        # Ordenar aristas por peso
        aristas.sort()

        mst = []
        for peso, origen, destino in aristas:
            if self.find(origen) != self.find(destino):
                self.union(origen, destino)
                mst.append((origen, destino, peso))

        return mst