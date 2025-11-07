import sys
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from CarreMagic import CarreMagic



app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()
engine.load("qml/Main.qml")

if not engine.rootObjects():
    sys.exit(-1)

sys.exit(app.exec())