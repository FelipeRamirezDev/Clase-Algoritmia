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