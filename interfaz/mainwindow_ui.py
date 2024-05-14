# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(680, 759)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.actionPuntos = QAction(MainWindow)
        self.actionPuntos.setObjectName(u"actionPuntos")
        self.actionPuntos_mas_cercanos = QAction(MainWindow)
        self.actionPuntos_mas_cercanos.setObjectName(u"actionPuntos_mas_cercanos")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_3 = QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.mostrar_groupBox = QGroupBox(self.tab)
        self.mostrar_groupBox.setObjectName(u"mostrar_groupBox")
        self.gridLayout_2 = QGridLayout(self.mostrar_groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.mostrar_pushButton = QPushButton(self.mostrar_groupBox)
        self.mostrar_pushButton.setObjectName(u"mostrar_pushButton")
        self.mostrar_pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.mostrar_pushButton, 0, 0, 1, 1)

        self.ordenamientos_pushButton1 = QPushButton(self.mostrar_groupBox)
        self.ordenamientos_pushButton1.setObjectName(u"ordenamientos_pushButton1")
        self.ordenamientos_pushButton1.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.ordenamientos_pushButton1, 2, 0, 1, 1)

        self.mostrarGrafo_pushButton = QPushButton(self.mostrar_groupBox)
        self.mostrarGrafo_pushButton.setObjectName(u"mostrarGrafo_pushButton")

        self.gridLayout_2.addWidget(self.mostrarGrafo_pushButton, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.mostrar_groupBox, 6, 0, 1, 2)

        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 0))
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.agregar_groupBox = QGroupBox(self.groupBox)
        self.agregar_groupBox.setObjectName(u"agregar_groupBox")
        self.agregar_groupBox.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(self.agregar_groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.agregar_inicio_pushButton = QPushButton(self.agregar_groupBox)
        self.agregar_inicio_pushButton.setObjectName(u"agregar_inicio_pushButton")
        self.agregar_inicio_pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.agregar_inicio_pushButton)

        self.agregar_final_pushButton = QPushButton(self.agregar_groupBox)
        self.agregar_final_pushButton.setObjectName(u"agregar_final_pushButton")
        self.agregar_final_pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.agregar_final_pushButton)


        self.gridLayout.addWidget(self.agregar_groupBox, 7, 0, 1, 1)

        self.colores_groupBox = QGroupBox(self.groupBox)
        self.colores_groupBox.setObjectName(u"colores_groupBox")
        self.colores_groupBox.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_7 = QGridLayout(self.colores_groupBox)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.red_label = QLabel(self.colores_groupBox)
        self.red_label.setObjectName(u"red_label")

        self.gridLayout_7.addWidget(self.red_label, 0, 0, 1, 1)

        self.red_spinBox = QSpinBox(self.colores_groupBox)
        self.red_spinBox.setObjectName(u"red_spinBox")
        self.red_spinBox.setMaximum(255)

        self.gridLayout_7.addWidget(self.red_spinBox, 0, 1, 1, 1)

        self.green_label = QLabel(self.colores_groupBox)
        self.green_label.setObjectName(u"green_label")

        self.gridLayout_7.addWidget(self.green_label, 0, 2, 1, 1)

        self.green_spinBox = QSpinBox(self.colores_groupBox)
        self.green_spinBox.setObjectName(u"green_spinBox")
        self.green_spinBox.setMaximum(255)

        self.gridLayout_7.addWidget(self.green_spinBox, 0, 3, 1, 1)

        self.blue_label = QLabel(self.colores_groupBox)
        self.blue_label.setObjectName(u"blue_label")

        self.gridLayout_7.addWidget(self.blue_label, 0, 4, 1, 1)

        self.blue_spinBox = QSpinBox(self.colores_groupBox)
        self.blue_spinBox.setObjectName(u"blue_spinBox")
        self.blue_spinBox.setMaximum(255)

        self.gridLayout_7.addWidget(self.blue_spinBox, 0, 5, 1, 1)


        self.gridLayout.addWidget(self.colores_groupBox, 5, 0, 1, 1)

        self.destino_groupBox = QGroupBox(self.groupBox)
        self.destino_groupBox.setObjectName(u"destino_groupBox")
        self.destino_groupBox.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_9 = QGridLayout(self.destino_groupBox)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_2 = QLabel(self.destino_groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(10, 16777215))

        self.gridLayout_9.addWidget(self.label_2, 0, 0, 1, 1)

        self.destinoX_spinBox = QSpinBox(self.destino_groupBox)
        self.destinoX_spinBox.setObjectName(u"destinoX_spinBox")
        self.destinoX_spinBox.setMaximum(500)

        self.gridLayout_9.addWidget(self.destinoX_spinBox, 0, 1, 1, 1)

        self.destinoY_label = QLabel(self.destino_groupBox)
        self.destinoY_label.setObjectName(u"destinoY_label")
        self.destinoY_label.setMaximumSize(QSize(10, 16777215))

        self.gridLayout_9.addWidget(self.destinoY_label, 0, 2, 1, 1)

        self.destinoY_spinBox = QSpinBox(self.destino_groupBox)
        self.destinoY_spinBox.setObjectName(u"destinoY_spinBox")
        self.destinoY_spinBox.setMaximum(500)

        self.gridLayout_9.addWidget(self.destinoY_spinBox, 0, 3, 1, 1)


        self.gridLayout.addWidget(self.destino_groupBox, 2, 0, 1, 1)

        self.id_groupBox = QGroupBox(self.groupBox)
        self.id_groupBox.setObjectName(u"id_groupBox")
        self.id_groupBox.setMinimumSize(QSize(0, 0))
        self.id_groupBox.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_10 = QGridLayout(self.id_groupBox)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.id_spinBox = QSpinBox(self.id_groupBox)
        self.id_spinBox.setObjectName(u"id_spinBox")

        self.gridLayout_10.addWidget(self.id_spinBox, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.id_groupBox, 0, 0, 1, 1)

        self.velocidad_groupBox = QGroupBox(self.groupBox)
        self.velocidad_groupBox.setObjectName(u"velocidad_groupBox")
        self.velocidad_groupBox.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_8 = QGridLayout(self.velocidad_groupBox)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.velocidad_spinBox = QSpinBox(self.velocidad_groupBox)
        self.velocidad_spinBox.setObjectName(u"velocidad_spinBox")

        self.gridLayout_8.addWidget(self.velocidad_spinBox, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.velocidad_groupBox, 4, 0, 1, 1)

        self.origen_groupBox = QGroupBox(self.groupBox)
        self.origen_groupBox.setObjectName(u"origen_groupBox")
        self.origen_groupBox.setMinimumSize(QSize(0, 0))
        self.origen_groupBox.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_11 = QGridLayout(self.origen_groupBox)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label = QLabel(self.origen_groupBox)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setMaximumSize(QSize(10, 16777215))

        self.gridLayout_11.addWidget(self.label, 0, 0, 1, 1)

        self.origenX_spinBox = QSpinBox(self.origen_groupBox)
        self.origenX_spinBox.setObjectName(u"origenX_spinBox")
        self.origenX_spinBox.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_11.addWidget(self.origenX_spinBox, 0, 1, 1, 1)

        self.origenY_label = QLabel(self.origen_groupBox)
        self.origenY_label.setObjectName(u"origenY_label")
        self.origenY_label.setMinimumSize(QSize(0, 0))
        self.origenY_label.setMaximumSize(QSize(10, 16777215))

        self.gridLayout_11.addWidget(self.origenY_label, 0, 2, 1, 1)

        self.origenY_spinBox = QSpinBox(self.origen_groupBox)
        self.origenY_spinBox.setObjectName(u"origenY_spinBox")
        self.origenY_spinBox.setMinimumSize(QSize(0, 0))

        self.gridLayout_11.addWidget(self.origenY_spinBox, 0, 3, 1, 1)


        self.gridLayout.addWidget(self.origen_groupBox, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 2, 0, 1, 1)

        self.salida = QPlainTextEdit(self.tab)
        self.salida.setObjectName(u"salida")
        self.salida.setMinimumSize(QSize(0, 0))
        self.salida.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.salida, 2, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_5 = QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.buscar_pushButton = QPushButton(self.tab_2)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")
        self.buscar_pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_5.addWidget(self.buscar_pushButton, 1, 1, 1, 1)

        self.mostrar_tabla_pushButton = QPushButton(self.tab_2)
        self.mostrar_tabla_pushButton.setObjectName(u"mostrar_tabla_pushButton")
        self.mostrar_tabla_pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_5.addWidget(self.mostrar_tabla_pushButton, 1, 2, 1, 1)

        self.buscar_lineEdit = QLineEdit(self.tab_2)
        self.buscar_lineEdit.setObjectName(u"buscar_lineEdit")

        self.gridLayout_5.addWidget(self.buscar_lineEdit, 1, 0, 1, 1)

        self.ordenamientos_pushButton2 = QPushButton(self.tab_2)
        self.ordenamientos_pushButton2.setObjectName(u"ordenamientos_pushButton2")
        self.ordenamientos_pushButton2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_5.addWidget(self.ordenamientos_pushButton2, 1, 3, 1, 1)

        self.tabla = QTableWidget(self.tab_2)
        self.tabla.setObjectName(u"tabla")

        self.gridLayout_5.addWidget(self.tabla, 0, 0, 1, 4)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_6 = QGridLayout(self.tab_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.graphicsView = QGraphicsView(self.tab_3)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_6.addWidget(self.graphicsView, 0, 0, 1, 2)

        self.limpiar_pushButton = QPushButton(self.tab_3)
        self.limpiar_pushButton.setObjectName(u"limpiar_pushButton")
        self.limpiar_pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_6.addWidget(self.limpiar_pushButton, 1, 1, 1, 1)

        self.dibujar_pushButton = QPushButton(self.tab_3)
        self.dibujar_pushButton.setObjectName(u"dibujar_pushButton")
        self.dibujar_pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_6.addWidget(self.dibujar_pushButton, 1, 0, 1, 1)

        self.ver_pushButton = QPushButton(self.tab_3)
        self.ver_pushButton.setObjectName(u"ver_pushButton")
        self.ver_pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_6.addWidget(self.ver_pushButton, 2, 0, 1, 2)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 680, 22))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.id_spinBox, self.origenX_spinBox)
        QWidget.setTabOrder(self.origenX_spinBox, self.origenY_spinBox)
        QWidget.setTabOrder(self.origenY_spinBox, self.destinoX_spinBox)
        QWidget.setTabOrder(self.destinoX_spinBox, self.destinoY_spinBox)
        QWidget.setTabOrder(self.destinoY_spinBox, self.velocidad_spinBox)
        QWidget.setTabOrder(self.velocidad_spinBox, self.red_spinBox)
        QWidget.setTabOrder(self.red_spinBox, self.green_spinBox)
        QWidget.setTabOrder(self.green_spinBox, self.blue_spinBox)
        QWidget.setTabOrder(self.blue_spinBox, self.agregar_inicio_pushButton)
        QWidget.setTabOrder(self.agregar_inicio_pushButton, self.agregar_final_pushButton)
        QWidget.setTabOrder(self.agregar_final_pushButton, self.mostrar_pushButton)
        QWidget.setTabOrder(self.mostrar_pushButton, self.ordenamientos_pushButton1)
        QWidget.setTabOrder(self.ordenamientos_pushButton1, self.salida)
        QWidget.setTabOrder(self.salida, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.buscar_lineEdit)
        QWidget.setTabOrder(self.buscar_lineEdit, self.buscar_pushButton)
        QWidget.setTabOrder(self.buscar_pushButton, self.mostrar_tabla_pushButton)
        QWidget.setTabOrder(self.mostrar_tabla_pushButton, self.ordenamientos_pushButton2)
        QWidget.setTabOrder(self.ordenamientos_pushButton2, self.dibujar_pushButton)
        QWidget.setTabOrder(self.dibujar_pushButton, self.limpiar_pushButton)
        QWidget.setTabOrder(self.limpiar_pushButton, self.graphicsView)
        QWidget.setTabOrder(self.graphicsView, self.tabla)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Particulas", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionPuntos.setText(QCoreApplication.translate("MainWindow", u"Puntos", None))
        self.actionPuntos_mas_cercanos.setText(QCoreApplication.translate("MainWindow", u"Puntos mas cercanos", None))
        self.mostrar_groupBox.setTitle("")
        self.mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.ordenamientos_pushButton1.setText(QCoreApplication.translate("MainWindow", u"Ordenamientos", None))
        self.mostrarGrafo_pushButton.setText(QCoreApplication.translate("MainWindow", u"Lista de adyacencia (Grafo)", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Particula", None))
        self.agregar_groupBox.setTitle("")
        self.agregar_inicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar al inicio", None))
        self.agregar_final_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar al final", None))
        self.colores_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Colores", None))
        self.red_label.setText(QCoreApplication.translate("MainWindow", u"r", None))
        self.green_label.setText(QCoreApplication.translate("MainWindow", u"g", None))
        self.blue_label.setText(QCoreApplication.translate("MainWindow", u"b", None))
        self.destino_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Destino", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.destinoY_label.setText(QCoreApplication.translate("MainWindow", u"y", None))
        self.id_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Id", None))
        self.velocidad_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.origen_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Origen", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.origenY_label.setText(QCoreApplication.translate("MainWindow", u"y", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.mostrar_tabla_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.buscar_lineEdit.setText("")
        self.buscar_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Identificador de particulas", None))
        self.ordenamientos_pushButton2.setText(QCoreApplication.translate("MainWindow", u"Ordenamientos", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.limpiar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.dibujar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.ver_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ver", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

