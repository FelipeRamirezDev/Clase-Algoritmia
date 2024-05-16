from PySide2.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton

class DialogoIDs(QDialog):
    def __init__(self, parent=None):
        super(DialogoIDs, self).__init__(parent)
        
        self.setWindowTitle('Ingresar IDs de Partículas')
        
        # Crear layout
        layout = QVBoxLayout()
        
        # Crear y agregar widgets al layout
        self.origen_label = QLabel('ID de Partícula Origen:')
        self.origen_input = QLineEdit()
        self.destino_label = QLabel('ID de Partícula Destino:')
        self.destino_input = QLineEdit()
        self.aceptar_button = QPushButton('Aceptar')
        
        layout.addWidget(self.origen_label)
        layout.addWidget(self.origen_input)
        layout.addWidget(self.destino_label)
        layout.addWidget(self.destino_input)
        layout.addWidget(self.aceptar_button)
        
        self.setLayout(layout)
        
        # Conectar botón aceptar
        self.aceptar_button.clicked.connect(self.accept)
    
    def get_ids(self):
        return self.origen_input.text(), self.destino_input.text()
