import sys
from PyQt5 import QtWidgets, QtGui as qg, QtCore as qc


def show_qt_widget(current_date: str, text: str):
    app = QtWidgets.QApplication(sys.argv)
    button = QtWidgets.QPushButton()
    button.setWindowTitle(f'{current_date} {text}')
    button.setFixedSize(500, 100)
    button.setWindowOpacity(.8)
    button.setStyleSheet('background-color:#1c1c1c;color:lime;')
    icon = qg.QIcon('./rUfLl.png')
    icon_size = qc.QSize(50, 50)
    button.setIcon(icon)
    button.setIconSize(icon_size)
    button.show()
    button.clicked.connect(button.close)
    app.exec()