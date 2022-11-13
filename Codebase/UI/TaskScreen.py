# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Task_Editor.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 113)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(230, 80, 161, 21))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.DateTimeEdit = QtWidgets.QDateTimeEdit(Dialog)
        self.DateTimeEdit.setGeometry(QtCore.QRect(10, 50, 194, 22))
        self.DateTimeEdit.setObjectName("DateTimeEdit")
        self.PriorityNumber = QtWidgets.QSpinBox(Dialog)
        self.PriorityNumber.setGeometry(QtCore.QRect(350, 50, 42, 22))
        self.PriorityNumber.setMinimum(1)
        self.PriorityNumber.setMaximum(10)
        self.PriorityNumber.setObjectName("PriorityNumber")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(220, 50, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.LabelSelector = QtWidgets.QStackedWidget(Dialog)
        self.LabelSelector.setGeometry(QtCore.QRect(110, 80, 121, 21))
        self.LabelSelector.setObjectName("LabelSelector")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.checkBox_2 = QtWidgets.QCheckBox(self.page)
        self.checkBox_2.setGeometry(QtCore.QRect(0, 0, 67, 18))
        self.checkBox_2.setObjectName("checkBox_2")
        self.LabelSelector.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.checkBox = QtWidgets.QCheckBox(self.page_2)
        self.checkBox.setGeometry(QtCore.QRect(0, 0, 91, 18))
        self.checkBox.setObjectName("checkBox")
        self.LabelSelector.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.checkBox_3 = QtWidgets.QCheckBox(self.page_3)
        self.checkBox_3.setGeometry(QtCore.QRect(0, 0, 67, 18))
        self.checkBox_3.setObjectName("checkBox_3")
        self.LabelSelector.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.checkBox_4 = QtWidgets.QCheckBox(self.page_4)
        self.checkBox_4.setGeometry(QtCore.QRect(0, 0, 67, 18))
        self.checkBox_4.setObjectName("checkBox_4")
        self.LabelSelector.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.checkBox_5 = QtWidgets.QCheckBox(self.page_5)
        self.checkBox_5.setGeometry(QtCore.QRect(0, 0, 91, 18))
        self.checkBox_5.setObjectName("checkBox_5")
        self.LabelSelector.addWidget(self.page_5)
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 10, 131, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 10, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(346, 30, 41, 20))
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(250, 30, 61, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 80, 81, 16))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        self.LabelSelector.setCurrentIndex(0)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.checkBox_2.setText(_translate("Dialog", "Academic"))
        self.checkBox.setText(_translate("Dialog", "Entertainment"))
        self.checkBox_3.setText(_translate("Dialog", "Sport"))
        self.checkBox_4.setText(_translate("Dialog", "Family"))
        self.checkBox_5.setText(_translate("Dialog", "Personal Care"))
        self.label.setText(_translate("Dialog", "Task Name:"))
        self.label_2.setText(_translate("Dialog", "Time and Date:"))
        self.label_3.setText(_translate("Dialog", "Priority:"))
        self.label_4.setText(_translate("Dialog", "Description:"))
        self.label_5.setText(_translate("Dialog", "Select Label(s):"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())