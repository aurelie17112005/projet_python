import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 400
    height: 300
    title: "Lanceur de modules"

    Column {
        anchors.centerIn: parent
        spacing: 20

        Button {
            text: "Carrés magique"
            //onClicked: launcher.launch("module1")
        }

        Button {
            text: "Carrés latin"
            //onClicked: launcher.launch("module2")
        }

        Button {
            text: "Sudoku"
            //onClicked: launcher.launch("module3")
        }
    }
}