import sys
from PyQt5 import QtWidgets, QtGui as qg, QtCore as qc


def show_qt_widget(current_date: str, text: str):
    app = QtWidgets.QApplication(sys.argv)
    text_edit = QtWidgets.QPushButton()
    text_edit.setWindowTitle(f'{current_date} {text}')
    text_edit.setFixedSize(500, 100)
    text_edit.setWindowOpacity(.8)
    text_edit.setStyleSheet('background-color:#1c1c1c;color:lime;')
    icon = qg.QIcon('./rUfLl.png')
    icon_size = qc.QSize(50, 50)
    text_edit.setIcon(icon)
    text_edit.setIconSize(icon_size)
    text_edit.show()
    text_edit.clicked.connect(text_edit.close)
    app.exec()