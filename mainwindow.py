from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene, QDialog, QMenu, QGraphicsTextItem
from PySide2.QtCore import Slot
from PySide2.QtGui import QPen, QColor, QWheelEvent
from interfaz.ui_mainwindow import Ui_MainWindow
from Particula import Particula
from Particulas import Particulas
from algoritmos import puntos_mas_cercanos
from Grafo import Grafo
from dialogo_ids import DialogoIDs


class MainWindow( QMainWindow ):
    def __init__( self ):
        super( MainWindow, self ).__init__()
        
        self.particulas = Particulas()
        self.ui = Ui_MainWindow()
        
        #Cargar y Aplicar el Diseño de la Interfaz
        self.ui.setupUi( self )
        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)
        
        # Inicialización y configuración del grafo
        self.grafo = Grafo()
        self.node_items = {}
        self.edge_items = []
        
        #Cargar y aplicar el archivo css
        self.load_styles()
        
        
        # Configuracion de botones de ordenamientos para tener un QMenu
        self.menu_ordenamientos = QMenu()
        self.menu_ordenamientos.addAction("Id (ascendente)", self.click_ordenar_id)
        self.menu_ordenamientos.addAction("Distancia (descendente)", self.click_ordenar_distancia)
        self.menu_ordenamientos.addAction("Velocidad (ascendente)", self.click_ordenar_velocidad)
        self.ui.ordenamientos_pushButton1.setMenu(self.menu_ordenamientos)
        self.ui.ordenamientos_pushButton2.setMenu(self.menu_ordenamientos)
        
        
        # Agregar QMenu a boton ver (para mostrar los puntos y puntos mas cercanos)
        self.menu_puntos = QMenu()
        self.menu_puntos.addAction("Puntos", self.dibujar_puntos)
        self.menu_puntos.addAction("Puntos cercanos", self.mostrar_puntos_cercanos)
        self.ui.ver_pushButton.setMenu(self.menu_puntos)
        
        # Agregar QMenu a boton Grafos para mostrar el grafo y ejecutar los algoritmos
        self.menu_grafos = QMenu()
        self.menu_grafos.addAction("Representacion en grafo", self.dibujar_grafo)
        self.menu_grafos.addAction("Dijkstra", self.ejecutar_dijkstra)
        self.menu_grafos.addAction("Kruskal", self.ejecutar_kruskal)
        self.ui.grafos_pushButton.setMenu(self.menu_grafos)

        # Conectar los botones con sus respectivas funciones
        self.ui.agregar_final_pushButton.clicked.connect( self.click_agregar_final )
        self.ui.agregar_inicio_pushButton.clicked.connect( self.click_agregar_inicio )
        self.ui.mostrar_pushButton.clicked.connect( self.click_mostrar )
        self.ui.mostrarGrafo_pushButton.clicked.connect( self.click_mostrar_grafo )
        
        self.ui.mostrar_tabla_pushButton.clicked.connect( self.click_mostrar_tabla )
        self.ui.buscar_pushButton.clicked.connect( self.click_buscar )
        
        self.ui.actionAbrir.triggered.connect( self.action_open_file )
        self.ui.actionGuardar.triggered.connect( self.action_save_file )
        
        self.ui.dibujar_pushButton.clicked.connect( self.dibujar )
        self.ui.limpiar_pushButton.clicked.connect( self.limpiar )
        
    """La función wheelEvent está diseñada para manejar eventos de desplazamiento de la rueda del ratón"""    
    def wheelEvent(self, event: QWheelEvent) -> None:
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2, 1.2)
        else:
            self.ui.graphicsView.scale(0.8, 0.8)
    
    """funcion para cargar estilo css"""
    def load_styles(self):
        with open('interfaz/styles.css', 'r') as file:
            self.setStyleSheet(file.read())
            
    
    @Slot()
    def click_agregar_final( self ):
        id = str(self.ui.id_spinBox.value())
        origenX = self.ui.origenX_spinBox.value()
        origenY = self.ui.origenY_spinBox.value()
        destinoX = self.ui.destinoX_spinBox.value()
        destinoY = self.ui.destinoY_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()
        
        particula = Particula( id, origenX, origenY, destinoX, destinoY, velocidad, red, green, blue )
        self.particulas.agregar_final( particula )
        
    @Slot()
    def click_agregar_inicio(self):
        id = str(self.ui.id_spinBox.value())
        origenX = self.ui.origenX_spinBox.value()
        origenY = self.ui.origenY_spinBox.value()
        destinoX = self.ui.destinoX_spinBox.value()
        destinoY = self.ui.destinoY_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()
        
        particula = Particula( id, origenX, origenY, destinoX, destinoY, velocidad, red, green, blue )
        self.particulas.agregar_inicio( particula )
    
    @Slot()
    def click_mostrar(self):
        #limpiar pantalla
        self.ui.salida.clear()
        #mostrar los datos
        self.ui.salida.insertPlainText(str(self.particulas))
        self.particulas.mostrar()
    
    @Slot()
    def click_mostrar_tabla(self):
        self.ui.tabla.setColumnCount(10)
        headers = ['ID','Origen x', 'Origen y', 'Destino x', 'Destino y', 'Velocidad', 'Red', 'Green','Blue', 'Distancia']
        self.ui.tabla.setHorizontalHeaderLabels( headers )
        self.ui.tabla.setRowCount( len(self.particulas) )
        
        row = 0
        for particula in self.particulas:
            id = QTableWidgetItem(str(particula.id))
            origen_x = QTableWidgetItem(str(particula.origen_x))
            origen_y = QTableWidgetItem(str(particula.origen_y))
            destino_x = QTableWidgetItem(str(particula.destino_x))
            destino_y = QTableWidgetItem(str(particula.destino_y))
            velocidad = QTableWidgetItem(str(particula.velocidad))
            red = QTableWidgetItem(str(particula.red))
            green = QTableWidgetItem(str(particula.green))
            blue = QTableWidgetItem(str(particula.blue))
            distancia = QTableWidgetItem(str(particula.distancia))
            
            self.ui.tabla.setItem(row, 0, id)
            self.ui.tabla.setItem(row, 1, origen_x)
            self.ui.tabla.setItem(row, 2, origen_y)
            self.ui.tabla.setItem(row, 3, destino_x)
            self.ui.tabla.setItem(row, 4, destino_y)
            self.ui.tabla.setItem(row, 5, velocidad)
            self.ui.tabla.setItem(row, 6, red)
            self.ui.tabla.setItem(row, 7, green)
            self.ui.tabla.setItem(row, 8, blue)
            self.ui.tabla.setItem(row, 9, distancia)
            
            row += 1
            
    @Slot()
    def click_buscar(self):
        id = self.ui.buscar_lineEdit.text()
        
        encontrado = False
        for particula in self.particulas:
            if id == str(particula.id):
                self.ui.tabla.clear()
                headers = ['ID','Origen x', 'Origen y', 'Destino x', 'Destino y', 'Velocidad', 'Red', 'Green','Blue', 'Distancia']
                self.ui.tabla.setHorizontalHeaderLabels( headers )
                self.ui.tabla.setRowCount(1)
                
                id = QTableWidgetItem(str(particula.id))
                origen_x = QTableWidgetItem(str(particula.origen_x))
                origen_y = QTableWidgetItem(str(particula.origen_y))
                destino_x = QTableWidgetItem(str(particula.destino_x))
                destino_y = QTableWidgetItem(str(particula.destino_y))
                velocidad = QTableWidgetItem(str(particula.velocidad))
                red = QTableWidgetItem(str(particula.red))
                green = QTableWidgetItem(str(particula.green))
                blue = QTableWidgetItem(str(particula.blue))
                distancia = QTableWidgetItem(str(particula.distancia))
                
                self.ui.tabla.setItem(0, 0, id)
                self.ui.tabla.setItem(0, 1, origen_x)
                self.ui.tabla.setItem(0, 2, origen_y)
                self.ui.tabla.setItem(0, 3, destino_x)
                self.ui.tabla.setItem(0, 4, destino_y)
                self.ui.tabla.setItem(0, 5, velocidad)
                self.ui.tabla.setItem(0, 6, red)
                self.ui.tabla.setItem(0, 7, green)
                self.ui.tabla.setItem(0, 8, blue)
                self.ui.tabla.setItem(0, 9, distancia)
                
                encontrado = True
        
        if not encontrado:
            QMessageBox.warning(
                self,
                'No encontrado',
                f'Lo sentimos, no se encontro una particula con el id {id}'
            )    
    
    @Slot()
    def action_open_file(self):
        path = QFileDialog.getOpenFileName(
            self,
            'Abrir archivo',
            '.',
            'JSON (*.json)'
        )[0]
        self.particulas.abrir(path)
        
    @Slot()
    def action_save_file(self):
        path = QFileDialog.getSaveFileName(
            self,
            'Guardar archivo',
            '.',
            'JSON (*.json)'
        )[0]
        
        if self.particulas.guardar(path):
            QMessageBox.information(
                self,
                'EXITO',
                f'Se pudo crear el archivo {path}'
            )
        else:
            QMessageBox.information(
                self,
                'ERROR',
                f'NO se pudo crear el archivo {path}'
            )
            
    @Slot()
    def dibujar(self):
        pen = QPen()
        pen.setWidth(2)

        for particula in self.particulas:
            r = particula.red
            g = particula.green
            b = particula.blue

            color = QColor(r, g, b)
            pen.setColor(color)

            origen_x = particula.origen_x
            origen_y = particula.origen_y
            destino_x = particula.destino_x
            destino_y = particula.destino_y

            #dibujar elipse de 6x6px en las coordenadas de origen y destino
            self.scene.addEllipse(origen_x, origen_y, 6, 6, pen)
            self.scene.addEllipse(destino_x, destino_y, 6, 6, pen)
            """Dibuja una línea desde el centro de la elipse de origen hasta el centro de la elipse de destino.
            El ajuste de +3 en las coordenadas es para centrar el inicio y el final de la línea en el centro
            de las elipses."""
            self.scene.addLine(origen_x+3, origen_y+3, destino_x+3, destino_y+3, pen)

            
    @Slot()
    def limpiar(self):
        self.scene.clear()
    
    @Slot()
    def click_ordenar_id(self):
        self.particulas.ordenar_id_ascendente()
        
    @Slot()
    def click_ordenar_distancia(self):
        self.particulas.ordenar_distancia_descendente()
    
    @Slot()
    def click_ordenar_velocidad(self):
        self.particulas.ordenar_velocidad_ascendente()
        
    @Slot()
    def dibujar_puntos(self):
        pen = QPen()
        pen.setWidth(2)
        for particula in self.particulas:
            r = particula.red
            g = particula.green
            b = particula.blue
            
            color = QColor(r, g, b)
            pen.setColor(color)
            
            origen_x = particula.origen_x
            origen_y = particula.origen_y
            destino_x = particula.destino_x
            destino_y = particula.destino_y
            
            # Dibuja una elipse en las coordenadas de origen con un diametro de 6 unidades
            self.scene.addEllipse(origen_x, origen_y, 6, 6, pen)
            # Dibuja una elipse en las coordenadas de destino con un diametro de 6 unidades
            self.scene.addEllipse(destino_x, destino_y, 6, 6, pen)
            
    @Slot()
    def mostrar_puntos_cercanos(self):
        pen = QPen()
        pen.setWidth(2)
        pen.setColor(QColor(255, 255, 255))
        puntos = []
        
        for particula in self.particulas:
            #agregamos una tupla a la lista puntos de cada origen y destino de las particulas
            puntos.append( (particula.origen_x, particula.origen_y) )
            puntos.append( (particula.destino_x, particula.destino_y) )
            
        resultado = puntos_mas_cercanos( puntos )
        for punto1, punto2 in resultado:
            origen_x, destino_x = punto1
            origen_y, destino_y = punto2
            #El ajuste de +3 en las coordenadas es para centrar el inicio y el final de la línea en el centro
            #de las elipses.
            self.scene.addLine(origen_x+3, destino_x+3, origen_y+3, destino_y+3, pen)


    @Slot()
    def click_mostrar_grafo(self):
        # Limpiar pantalla
        self.ui.salida.clear()
        # Construir el grafo a partir de las partículas
        if not self.grafo.grafo:
            self.grafo.construir_desde_particulas(self.particulas)
        # Utiliza una variable para capturar el texto que representa el grafo
        texto_del_grafo = self.grafo.mostrar_grafo()
        # Mostrar el texto del grafo en QPlainTextEdit
        self.ui.salida.setPlainText(texto_del_grafo)
        # Mostrar el grafo en la terminal
        print(texto_del_grafo)
        
    @Slot()
    def dibujar_grafo(self):
        self.dibujar()
        radius = 3  # Radio del nodo para el ajuste de la posición del texto

        for origen, destinos in self.grafo.grafo.items():
            # Agregar etiqueta al nodo origen
            origen_label = QGraphicsTextItem(f'({origen[0]}, {origen[1]})')
            color_texto = QColor("#FFFFFF")
            origen_label.setDefaultTextColor(color_texto)
            origen_label.setPos(origen[0] + radius, origen[1] - 10)
            self.scene.addItem(origen_label)

            for destino, peso in destinos:
                # Agregar etiqueta al nodo destino solo si no ha sido agregada anteriormente
                if destino not in self.node_items:
                    destino_label = QGraphicsTextItem(f'({destino[0]}, {destino[1]})')
                    color_texto = QColor("#FFFFFF")
                    destino_label.setDefaultTextColor(color_texto)
                    destino_label.setPos(destino[0] + radius, destino[1] - 10)
                    self.scene.addItem(destino_label)
                    self.node_items[destino] = True  # Marca que el nodo destino ya tiene etiqueta

                # Agregar etiqueta de peso de la arista
                mid_x = (origen[0] + destino[0]) / 2
                mid_y = (origen[1] + destino[1]) / 2
                
                texto_peso = QGraphicsTextItem(f"{peso}")
                color_texto = QColor("#FFFFFF")
                texto_peso.setDefaultTextColor(color_texto)
                texto_peso.setPos(mid_x, mid_y - 10)
                self.scene.addItem(texto_peso)

                
    @Slot()
    def ejecutar_dijkstra(self):
        # Obtener los IDs de las partículas de inicio y destino
        dialogo = DialogoIDs(self)
        if dialogo.exec_() == QDialog.Accepted:
            inicio_id, destino_id = dialogo.get_ids()

        # Buscar las partículas correspondientes
        particula_inicio = next((p for p in self.particulas if p.id == inicio_id), None)
        particula_destino = next((p for p in self.particulas if p.id == destino_id), None)

        if particula_inicio is None or particula_destino is None:
            QMessageBox.warning(self, 'Error', 'Nodo de inicio o destino no encontrado')
            return
        
        inicio = (particula_inicio.origen_x, particula_inicio.origen_y)
        destino = (particula_destino.destino_x, particula_destino.destino_y)
        
        # Asegurarse de que el grafo está construido
        self.grafo.construir_desde_particulas(self.particulas)
        
        # Ejecutar Dijkstra
        distancias, padres = self.grafo.dijkstra(inicio)
        
        # Mostrar los resultados en la salida
        self.ui.salida.clear()
        self.ui.salida.insertPlainText("Distancias desde el nodo de inicio:\n")
        for nodo, distancia in distancias.items():
            self.ui.salida.insertPlainText(f"Nodo {nodo}: {distancia}\n")
        
        # Dibujar el camino más corto
        self.dibujar_camino_corto(padres, inicio, destino)

    def dibujar_camino_corto(self, padres, inicio, destino):
        pen = QPen()
        pen.setWidth(2)
        pen.setColor(QColor(255, 0, 0))  # Rojo para destacar el camino más corto
        
        # Inicializar el peso total
        peso_total = 0
        
        # Empezar desde el nodo de destino y retroceder hasta el nodo de inicio
        nodo_actual = destino
        while nodo_actual != inicio:
            if nodo_actual not in padres:
                print(f"Error: el nodo {nodo_actual} no tiene padre en el diccionario.")
                QMessageBox.warning(self, 'Error', f'El nodo {nodo_actual} no tiene padre en el diccionario.')
                return
            
            padre = padres[nodo_actual]
            if padre is None:
                break
            # Calcular la distancia entre el nodo actual y su padre
            distancia = self.grafo.distancia_entre_nodos(nodo_actual, padre)
            # Sumar la distancia al peso total
            peso_total += distancia
            # Dibujar la línea entre el nodo actual y su padre
            self.scene.addLine(padre[0] + 3, padre[1] + 3, nodo_actual[0] + 3, nodo_actual[1] + 3, pen)
            nodo_actual = padre
            
        # Mostrar el peso total en la escena
        texto_peso = QGraphicsTextItem(f"Peso Total: {peso_total}")
        color_texto = QColor("#FFFFFF")
        texto_peso.setDefaultTextColor(color_texto)
        texto_peso.setPos(-80, -80)  # Posición del texto en la escena
        self.scene.addItem(texto_peso)
        
        # Marcar el nodo de inicio
        pen.setColor(QColor(0, 255, 0))  # Verde para el nodo de inicio
        self.scene.addEllipse(inicio[0], inicio[1], 6, 6, pen)
        
        # Marcar el nodo de destino
        pen.setColor(QColor(0, 0, 255))  # Azul para el nodo de destino
        self.scene.addEllipse(destino[0], destino[1], 6, 6, pen)


    @Slot()
    def ejecutar_kruskal(self):
        # Construir el grafo a partir de las partículas
        self.grafo.construir_desde_particulas(self.particulas)
        mst = self.grafo.kruskal()
        
        # Limpiar la escena
        self.scene.clear()

        # Dibujar el MST
        pen = QPen()
        pen.setWidth(2)
        pen.setColor(QColor(255, 0, 0))  # Rojo para destacar las aristas del MST
        
        for origen, destino, peso in mst:
            self.scene.addEllipse(origen[0], origen[1], 6, 6, pen)
            self.scene.addEllipse(destino[0], destino[1], 6, 6, pen)
            self.scene.addLine(origen[0]+3, origen[1]+3, destino[0]+3, destino[1]+3, pen)
        
        # Mostrar el peso total del MST
        peso_total = sum(peso for _, _, peso in mst)
        texto_peso = QGraphicsTextItem(f"Peso Total del Arbol de Expansión Mínima (MST): {peso_total}")
        color_texto = QColor("#FFFFFF")
        texto_peso.setDefaultTextColor(color_texto)
        texto_peso.setPos(-80, -80)  # Posición del texto en la escena
        self.scene.addItem(texto_peso)