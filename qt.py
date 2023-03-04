import sys
from PyQt5 import QtWidgets, QtGui as qg, QtCore as qc


def show_qt_widget(current_date: str, text: str):
    app = QtWidgets.QApplication(sys.argv)
    btn = QtWidgets.QPushButton()
    btn.setWindowTitle(f'{current_date} {text}')
    btn.setFixedSize(500, 100)
    btn.setWindowOpacity(.8)
    btn.setStyleSheet('background-color:#1c1c1c;color:lime;')
    icon = qg.QIcon('./rUfLl.png')
    icon_size = qc.QSize(50, 50)
    btn.setIcon(icon)
    btn.setIconSize(icon_size)
    btn.show()
    btn.clicked.connect(btn.close)
    app.exec()