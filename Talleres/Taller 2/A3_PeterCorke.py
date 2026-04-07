#sudo raspi-config -*- coding: utf-8 -*-  wvkbd-mobintl

import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import roboticstoolbox as rtb
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(662, 560)  # más alto para los sliders
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 20, 330, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 370, 331, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 440, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 130, 361, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(130, 100, 131, 20))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(331, 20, 330, 422))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setText("")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")

        # --- Sliders para q1, q2, q3 ---
        slider_x = 20
        slider_w = 200
        label_w  = 60
        val_w    = 40

        self.sliders      = []
        self.slider_labels = []
        self.slider_vals  = []

        for i in range(3):
            y = 160 + i * 55

            # Etiqueta "q1:", "q2:", "q3:"
            lbl = QtWidgets.QLabel(self.centralwidget)
            lbl.setGeometry(QtCore.QRect(slider_x, y, label_w, 20))
            lbl.setFont(QtGui.QFont())
            lbl.setText(f"q{i+1}:")
            lbl.hide()
            self.slider_labels.append(lbl)

            # Slider
            sl = QtWidgets.QSlider(QtCore.Qt.Horizontal, self.centralwidget)
            sl.setGeometry(QtCore.QRect(slider_x + label_w, y, slider_w, 20))
            sl.setMinimum(0)
            sl.setMaximum(round(np.pi * 100) * 2)  # multiplicamos por 100 para tener 2 decimales
            sl.setValue(0)   # valor inicial = 0.3 rad/m
            sl.hide()
            self.sliders.append(sl)

            # Valor numérico
            val_lbl = QtWidgets.QLabel(self.centralwidget)
            val_lbl.setGeometry(QtCore.QRect(slider_x + label_w + slider_w + 5, y, val_w, 20))
            val_lbl.setText("0.30")
            val_lbl.hide()
            self.slider_vals.append(val_lbl)

            # Conectar señal
            sl.valueChanged.connect(self.on_slider_changed)

        self.label_2.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.comboBox.raise_()
        self.label_6.raise_()

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 662, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Canvas interactivo
        self.fig_interactivo = Figure(figsize=(4, 4), dpi=100)
        self.canvas_interactivo = FigureCanvas(self.fig_interactivo)
        self.canvas_interactivo.setParent(self.centralwidget)
        self.canvas_interactivo.setGeometry(QtCore.QRect(331, 20, 330, 392))
        self.canvas_interactivo.hide()

        # Toolbar
        self.toolbar = NavigationToolbar(self.canvas_interactivo, self.centralwidget)
        self.toolbar.setGeometry(QtCore.QRect(331, 412, 330, 30))
        self.toolbar.hide()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.comboBox.currentIndexChanged.connect(self.mostrar_diagrama)

        # Guardar config actual del robot
        self._robot_links  = None
        self._robot_nombre = None

    # ------------------------------------------------------------------
    def get_q(self):
        """Lee los valores actuales de los 3 sliders → lista [q1, q2, q3]."""
        return [sl.value() / 100.0 for sl in self.sliders]

    def on_slider_changed(self):
        """Actualiza etiqueta de valor y redibuja el robot."""
        for i, (sl, val_lbl) in enumerate(zip(self.sliders, self.slider_vals)):
            val_lbl.setText(f"{sl.value() / 100.0:.2f}")
        if self._robot_links is not None:
            self.actualizar_robot(self._robot_links, self.get_q(), self._robot_nombre)

    def mostrar_sliders(self, show=True):
        for sl, lbl, val in zip(self.sliders, self.slider_labels, self.slider_vals):
            sl.setVisible(show)
            lbl.setVisible(show)
            val.setVisible(show)

    # ------------------------------------------------------------------
    def mostrar_diagrama(self):
        h = 0
        L1 = 0.5
        L2 = 0.5
        L3 = 0.5

        index = self.comboBox.currentIndex()

        self.label_6.hide()
        self.canvas_interactivo.hide()
        self.toolbar.hide()
        self.mostrar_sliders(False)

        if index == 0:
            self._robot_links  = None
            self._robot_nombre = None

        elif index == 1:  # Cartesiano PPP
            links = [
                rtb.DHLink(d=0, a=0, theta=-np.pi/2, alpha=-np.pi/2, sigma=1, offset=h),
                rtb.DHLink(d=0, a=0, theta=-np.pi/2, alpha=-np.pi/2, sigma=1, offset=L1),
                rtb.DHLink(d=0, a=0, theta=0,        alpha=0,        sigma=1, offset=L2 + L3),
            ]
            self._robot_links  = links
            self._robot_nombre = "Cartesiano PPP"
            self.canvas_interactivo.show()
            self.toolbar.show()
            self.mostrar_sliders(True)
            self.actualizar_robot(links, self.get_q(), "Cartesiano PPP")
            self.label_5.setText("Articulaciones: 3 (PPP)")

        elif index == 2:  # Esférico RRP
            links = [
                rtb.DHLink(d=h+L1, a=0, theta=0, alpha=np.pi/2,  sigma=0, offset=0),
                rtb.DHLink(d=0,    a=0, theta=0, alpha=-np.pi/2, sigma=0, offset=np.pi/2),
                rtb.DHLink(d=0,    a=0, theta=0, alpha=0,        sigma=1, offset=L2 + L3),
            ]
            self._robot_links  = links
            self._robot_nombre = "Esferico RRP"
            self.canvas_interactivo.show()
            self.toolbar.show()
            self.mostrar_sliders(True)
            self.actualizar_robot(links, self.get_q(), "Esferico RRP")
            self.label_5.setText("Articulaciones: 3 (RRP)")

        elif index == 3:  # Cilíndrico RPP
            links = [
                rtb.DHLink(d=h+L1, a=0, theta=0,        alpha=0,        sigma=0, offset=0),
                rtb.DHLink(d=0,    a=0, theta=-np.pi/2, alpha=-np.pi/2, sigma=1, offset=0),
                rtb.DHLink(d=0,    a=0, theta=0,        alpha=0,        sigma=1, offset=L2 + L3),
            ]
            self._robot_links  = links
            self._robot_nombre = "Cilindrico RPP"
            self.canvas_interactivo.show()
            self.toolbar.show()
            self.mostrar_sliders(True)
            self.actualizar_robot(links, self.get_q(), "Cilindrico RPP")
            self.label_5.setText("Articulaciones: 3 (RPP)")

    # ------------------------------------------------------------------
    def actualizar_robot(self, links, q, nombre):
        self.fig_interactivo.clf()
        ax = self.fig_interactivo.add_subplot(111, projection='3d')
        self.fig_interactivo.subplots_adjust(left=0.05, right=0.95, top=0.98, bottom=0.05)
        ax.set_title("")
        ax.set_facecolor('#f0f0f0')
        self.fig_interactivo.patch.set_facecolor('#f0f0f0')

        robot = rtb.DHRobot(links, name=nombre)
        T_all = robot.fkine_all(q)

        x_coords, y_coords, z_coords = [0], [0], [0]
        for i in range(len(T_all)):
            pos = T_all[i].t
            x_coords.append(pos[0])
            y_coords.append(pos[1])
            z_coords.append(pos[2])

        tipos = ['base'] + ['P' if link.sigma == 1 else 'R' for link in robot.links]

        n        = min(len(x_coords), len(tipos))
        x_coords = x_coords[:n]
        y_coords = y_coords[:n]
        z_coords = z_coords[:n]
        tipos    = tipos[:n]

        # Línea del robot
        ax.plot(x_coords, y_coords, z_coords,
                'o-', linewidth=3, markersize=8,
                color='darkorange', alpha=0.4, zorder=5)

        poses       = [np.eye(4)] + [T_all[i].A for i in range(len(T_all))]
        poses       = poses[:n]
        axis_labels = ['X', 'Y', 'Z']
        axis_colors = ['r', 'g', 'b']
        scale_ejes  = 0.2

        for idx in range(n):
            T      = poses[idx]
            origin = T[:3, 3]

            if tipos[idx] == 'P':
                self.dibujar_articulacion_prismatica(ax, origin, T, color='royalblue')
            elif tipos[idx] == 'R':
                self.dibujar_articulacion_revoluta(ax, origin, T, color='tomato')

            for j, (color, label) in enumerate(zip(axis_colors, axis_labels)):
                direction = T[:3, j] * scale_ejes
                ax.quiver(origin[0], origin[1], origin[2],
                          direction[0], direction[1], direction[2],
                          color=color, linewidth=2.0, arrow_length_ratio=0.4)
                tip = origin + T[:3, j] * scale_ejes * 1.4
                ax.text(tip[0], tip[1], tip[2], label,
                        fontsize=6, color=color, fontweight='bold')

        # Efector final
        T_tcp      = T_all[-1].A
        origin_tcp = T_tcp[:3, 3]

        # Línea hasta efector
        ax.plot([x_coords[-1], origin_tcp[0]],
                [y_coords[-1], origin_tcp[1]],
                [z_coords[-1], origin_tcp[2]],
                '-', linewidth=3, color='darkorange', alpha=0.4)

        ax.scatter(origin_tcp[0], origin_tcp[1], origin_tcp[2],
                   color='black', s=40, zorder=6)

        scale_tcp = scale_ejes
        for j, (color, label) in enumerate(zip(axis_colors, axis_labels)):
            direction = T_tcp[:3, j] * scale_tcp
            ax.quiver(origin_tcp[0], origin_tcp[1], origin_tcp[2],
                      direction[0], direction[1], direction[2],
                      color=color, linewidth=2.0, arrow_length_ratio=0.4)
            tip = origin_tcp + T_tcp[:3, j] * scale_tcp * 1.3
            ax.text(tip[0], tip[1], tip[2], label,
                    fontsize=6, color=color, fontweight='bold')

        ax.set_xlim(-1, 1)
        ax.set_ylim(-1, 1)
        ax.set_zlim(0,  1)
        ax.set_xlabel('X', fontsize=9, labelpad=10)
        ax.set_ylabel('Y', fontsize=9, labelpad=10)
        ax.set_zlabel('Z', fontsize=9, labelpad=10)
        ax.tick_params(axis='both', labelsize=7)

        self.canvas_interactivo.draw()

    # ------------------------------------------------------------------
    def dibujar_articulacion_prismatica(self, ax, origen, T, color='royalblue', escala=0.08):
        s = escala
        R = T[:3, :3]
        local_vertices = np.array([
            [-s, -s, -s], [+s, -s, -s], [+s, +s, -s], [-s, +s, -s],
            [-s, -s, +s], [+s, -s, +s], [+s, +s, +s], [-s, +s, +s],
        ])
        vertices = np.array([origen + R @ v for v in local_vertices])
        caras = [
            [vertices[0], vertices[1], vertices[2], vertices[3]],
            [vertices[4], vertices[5], vertices[6], vertices[7]],
            [vertices[0], vertices[1], vertices[5], vertices[4]],
            [vertices[2], vertices[3], vertices[7], vertices[6]],
            [vertices[0], vertices[3], vertices[7], vertices[4]],
            [vertices[1], vertices[2], vertices[6], vertices[5]],
        ]
        cubo = Poly3DCollection(caras, alpha=0.15, facecolor=color,
                                edgecolor='navy', linewidth=0.8)
        ax.add_collection3d(cubo)

    # ------------------------------------------------------------------
    def dibujar_articulacion_revoluta(self, ax, origen, T, color='tomato', escala=0.08):
        radio  = escala
        grosor = escala * 0.5
        n_pts  = 30
        R      = T[:3, :3]

        theta = np.linspace(0, 2 * np.pi, n_pts)
        circulo_local = np.array([
            np.array([radio * np.cos(t), radio * np.sin(t), 0.0])
            for t in theta
        ])
        top_local = circulo_local + np.array([0, 0,  grosor])
        bot_local = circulo_local + np.array([0, 0, -grosor])

        top = np.array([origen + R @ v for v in top_local])
        bot = np.array([origen + R @ v for v in bot_local])

        ax.add_collection3d(Poly3DCollection(
            [list(map(tuple, top))],
            alpha=0.15, facecolor=color, edgecolor='darkred', linewidth=0.8))
        ax.add_collection3d(Poly3DCollection(
            [list(map(tuple, bot))],
            alpha=0.15, facecolor=color, edgecolor='darkred', linewidth=0.8))
        for i in range(n_pts - 1):
            cara = [tuple(bot[i]), tuple(bot[i+1]),
                    tuple(top[i+1]), tuple(top[i])]
            ax.add_collection3d(Poly3DCollection(
                [cara], alpha=0.08, facecolor=color, edgecolor='none'))

    # ------------------------------------------------------------------
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow",
            "<html><head/><body><p align=\"center\">"
            "<span style=\" font-weight:700;\">DIAGRAMA CINEMATICO<br/>&amp; <br/>"
            "POP-UP MENU </span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow",
            "<html><head/><body><p align=\"center\">Integrantes: </p>"
            "<p align=\"center\">Arellano Diego         |        Carrillo Esteban<br/>"
            "Fajardo Jean Pierre        |        Rodriguez Marlly    </p></body></html>"))
        self.label_3.setText(_translate("MainWindow",
            "<html><head/><body><p>"
            "<img src=\":/img/UNIVERSIDAD_ECCI.png\" width = \"300\"/>"
            "</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Tipo de Robot:"))
        self.label_5.setText(_translate("MainWindow", "Articulaciones:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Seleccionar"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Cartesiano"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Esferico"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Cilindrico"))


import recurso_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
