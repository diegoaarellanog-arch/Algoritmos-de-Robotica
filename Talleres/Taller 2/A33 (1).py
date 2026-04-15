# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

# Importar el archivo de recursos (asegúrate de que imagen_rc.py esté en la carpeta)
import imagen_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 0, 500, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        # SLIDER RESISTENCIA (Hasta 1,000,000)
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(30, 180, 160, 22))
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(1000000)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        
        # SLIDER CAPACITOR
        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(30, 260, 160, 22))
        self.horizontalSlider_2.setMinimum(1)
        self.horizontalSlider_2.setMaximum(1000)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        
        # SLIDER VOLTAJE
        self.horizontalSlider_3 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(30, 340, 160, 22))
        self.horizontalSlider_3.setMaximum(100)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 136, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 220, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 300, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        
        # CONTENEDOR GRÁFICA
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(340, 70, 420, 331))
        self.label_5.setObjectName("label_5")
        
        # Setup Matplotlib
        self.figura = plt.figure()
        self.canvas = FigureCanvas(self.figura)
        self.ax = self.figura.add_subplot(111)
        layout = QtWidgets.QVBoxLayout(self.label_5)
        layout.addWidget(self.canvas)
        
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 410, 301, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(390, 400, 381, 161))
        self.label_7.setObjectName("label_7")
        
        # LABELS DINÁMICOS
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(200, 180, 70, 16))
        self.label_8.setObjectName("label_8")
        
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(200, 260, 70, 16))
        self.label_9.setObjectName("label_9")
        
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(200, 340, 70, 16))
        self.label_10.setObjectName("label_10")
        
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(280, 180, 55, 16))
        self.label_11.setObjectName("label_11")
        
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(280, 260, 55, 16))
        self.label_12.setObjectName("label_12")
        
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(280, 340, 55, 16))
        self.label_13.setObjectName("label_13")
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # CONEXIONES
        self.horizontalSlider.valueChanged.connect(self.actualizar_grafica)
        self.horizontalSlider_2.valueChanged.connect(self.actualizar_grafica)
        self.horizontalSlider_3.valueChanged.connect(self.actualizar_grafica)
        
        self.actualizar_grafica()

    def format_value(self, value):
        """ Función para acortar números usando prefijos K y M """
        if value >= 1000000:
            return f"{value/1000000:.1f} M"
        elif value >= 1000:
            return f"{value/1000:.1f} k"
        else:
            return str(value)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simulador de Circuito RC"))
        self.label.setText(_translate("MainWindow", "CARGA Y DESCARGA CAPACITOR"))
        self.label_2.setText(_translate("MainWindow", "RESISTENCIA"))
        self.label_3.setText(_translate("MainWindow", "CAPACITOR"))
        self.label_4.setText(_translate("MainWindow", "VOLTAJE"))
        self.label_6.setText(_translate("MainWindow", "Marlly Johanna Rodriguez - 114061\n"
"Jean Pierre Fajardo Malagon - 113807\n"
"Juan Esteban Carrillo Galindo - 119042\n"
"Diego Alejandro Arellano - 110847"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/images.png\"/></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "Ω"))
        self.label_12.setText(_translate("MainWindow", "uF"))
        self.label_13.setText(_translate("MainWindow", "V"))

    def actualizar_grafica(self):
        # Obtener valores
        r_raw = self.horizontalSlider.value()
        c_raw = self.horizontalSlider_2.value()
        v_val = self.horizontalSlider_3.value()

        # Actualizar labels con formato K y M
        self.label_8.setText(self.format_value(r_raw))
        self.label_9.setText(str(c_raw))
        self.label_10.setText(str(v_val))

        # Cálculos (R en Ohmios, C en Faradios)
        R = r_raw
        C = c_raw * 1e-6
        V = v_val
        tau = R * C

        # Evitar errores si tau es muy pequeño
        if tau == 0: tau = 0.001

        t = np.linspace(0, 5 * tau, 500)
        v_carga = V * (1 - np.exp(-t / tau))
        v_descarga = V * np.exp(-t / tau)

        self.ax.clear()
        self.ax.plot(t, v_carga, label='Carga', color='red')
        self.ax.plot(t, v_descarga, label='Descarga', color='blue')
        self.ax.set_title(f"Tau (τ) = {tau:.4f} s")
        self.ax.set_xlabel("Tiempo (s)")
        self.ax.set_ylabel("Voltaje (V)")
        self.ax.grid(True)
        self.ax.legend()
        self.canvas.draw()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())