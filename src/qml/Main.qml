import QtQuick 2.12
import QtQuick.Controls 2.12

ApplicationWindow {
    visible: true
    width: 600
    height: 400
    title: "Lanceur de modules"

    Column {
        anchors.centerIn: parent
        spacing: 20

        Button {
            text: "Carré magique"
            onClicked: {
                app.generate_magic_square(3)
            }
        }

        Button {
            text: "Carré latin"
            onClicked: {
                app.generate_latin_square(4)
            }
        }

        Button {
            text: "Sudoku"
            onClicked: {
                var puzzle = `5 3 0 0 7 0 0 0 0
                              6 0 0 1 9 5 0 0 0
                              0 9 8 0 0 0 0 6 0
                              8 0 0 0 6 0 0 0 3
                              4 0 0 8 0 3 0 0 1
                              7 0 0 0 2 0 0 0 6
                              0 6 0 0 0 0 2 8 0
                              0 0 0 4 1 9 0 0 5
                              0 0 0 0 8 0 0 7 9`
                app.solve_sudoku(puzzle)
            }
        }

        TextArea {
            id: resultArea
            width: parent.width
            height: 200
            wrapMode: TextArea.Wrap
            placeholderText: "Les résultats s'afficheront ici"
        }

        Connections {
            target: app
            onResult_signal: {
                resultArea.text = message
            }
        }
    }
}
