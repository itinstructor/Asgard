# Form implementation generated from reading ui file 'preferences.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_PreferencesDialog(object):
    def setupUi(self, PreferencesDialog):
        PreferencesDialog.setObjectName("PreferencesDialog")
        PreferencesDialog.resize(400, 296)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=PreferencesDialog)
        self.buttonBox.setGeometry(QtCore.QRect(50, 260, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(parent=PreferencesDialog)
        self.label.setGeometry(QtCore.QRect(30, 40, 121, 16))
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(parent=PreferencesDialog)
        self.frame.setGeometry(QtCore.QRect(10, 10, 381, 241))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.spinBoxGripperUpperRange = QtWidgets.QSpinBox(parent=self.frame)
        self.spinBoxGripperUpperRange.setGeometry(QtCore.QRect(150, 30, 88, 23))
        self.spinBoxGripperUpperRange.setMaximum(2000)
        self.spinBoxGripperUpperRange.setObjectName("spinBoxGripperUpperRange")
        self.frame.raise_()
        self.buttonBox.raise_()
        self.label.raise_()

        self.retranslateUi(PreferencesDialog)
        self.buttonBox.accepted.connect(PreferencesDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(PreferencesDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(PreferencesDialog)

    def retranslateUi(self, PreferencesDialog):
        _translate = QtCore.QCoreApplication.translate
        PreferencesDialog.setWindowTitle(_translate("PreferencesDialog", "Preferences"))
        self.label.setText(_translate("PreferencesDialog", "Gripper Upper Range:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PreferencesDialog = QtWidgets.QDialog()
    ui = Ui_PreferencesDialog()
    ui.setupUi(PreferencesDialog)
    PreferencesDialog.show()
    sys.exit(app.exec())
