import sys
from PySide6.QtCore import QUrl, QObject, Signal, Slot
from PySide6.QtQuick import QQuickView  # Remplace QQmlApplicationEngine par QQuickView
from PySide6.QtWidgets import QApplication
from CarreMagic import CarreMagic
from CarreLatin import CarreLatin
from Sudoku import Sudoku


class App(QObject):
    result_signal = Signal(str)

    def __init__(self):
        super().__init__()

        self.app = QApplication(sys.argv)

        # Utiliser QQuickView pour afficher le fichier QML
        self.view = QQuickView()

        # Charger le fichier QML
        self.view.setSource(QUrl.fromLocalFile("qml/Main.qml"))

        # Assurer que le QML a accès à l'objet Python 'app'
        self.context = self.view.rootContext()
        self.context.setContextProperty("app", self)

    @Slot(int)
    def generate_magic_square(self, p):
        magic_square = CarreMagic(p)
        square_str = magic_square.to_string()
        self.result_signal.emit(square_str)

    @Slot(int)
    def generate_latin_square(self, n):
        latin_square = CarreLatin(n)
        latin_square_str = latin_square.to_string()
        self.result_signal.emit(latin_square_str)

    @Slot(str)
    def solve_sudoku(self, puzzle):
        grid = [list(map(int, row.split())) for row in puzzle.splitlines()]
        sudoku = Sudoku(grid)
        if sudoku.solve():
            sudoku_str = sudoku.to_string()
            self.result_signal.emit(sudoku_str)
        else:
            self.result_signal.emit("No solution found")


if __name__ == "__main__":
    app = App()
    app.view.show()  # Afficher la vue
    sys.exit(app.app.exec())  # Démarrer l'application
