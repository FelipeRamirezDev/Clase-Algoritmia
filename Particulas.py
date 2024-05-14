from Particula import Particula
import json

class Particulas:
    def __init__(self):
        self.__particulas = []
    
    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)
        
    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0, particula)
        
    def mostrar(self):
        for particula in self.__particulas:
            print(particula)
            
    def __str__( self ):
        return "".join(
            str( p ) + '\n' for p in self.__particulas
        )
        
    def __len__( self ):
        return len(self.__particulas)
    
    def __iter__( self ):
        self.cont = 0
        return self
    
    def __next__( self ):
        if self.cont < len(self.__particulas):
            particula = self.__particulas[self.cont]
            self.cont += 1
            return particula
        else:
            raise StopIteration
    
    def guardar(self, path):
        try:
            with open(path, 'w') as f:
                list_of_particles = [particula.to_dict() for particula in self.__particulas ]
                json.dump(list_of_particles, f, indent=5)
                return 1
        except:
            return 0
        
    def abrir(self, path):
        try:
            with open(path) as f:
                list_of_particles = json.load(f)
                self.__particulas = [Particula(**particula) for particula in list_of_particles]
                return 1
        except:
            return 0
        
    def ordenar_id_ascendente(self):
        self.__particulas.sort(key=lambda particula: particula.id)
    
    def ordenar_distancia_descendente(self):
        self.__particulas.sort(key=lambda particula: particula.distancia, reverse=True)
    
    def ordenar_velocidad_ascendente(self):
        self.__particulas.sort(key=lambda particula: particula.velocidad)
        
