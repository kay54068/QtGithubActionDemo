import QtQuick 2.0
import QtQuick.Window 2.0

Window {
    width: 640
    height: 480
    visible: true
    title: qsTr("Qt Github Action Demo - v1.0.0 ")
    Text {
        text: "Run Demo on " + Qt.platform.os
        font.pixelSize: 30
        anchors.centerIn: parent
    }
}
