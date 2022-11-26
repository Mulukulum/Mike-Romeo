import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui
import datetime



from MainWindow import Ui_MainWindow as AmberWindowUI

from TaskDisplay import Ui_Form as TaskDispUI

class AmberApplicationWindow(QtWidgets.QMainWindow):

    def __init__(self) -> None:
        super(AmberApplicationWindow,self).__init__()
        self.ui=AmberWindowUI()
        self.ui.setupUi(self)
        self.ui.date_label.setText(f"{datetime.date.today().strftime('%A, %B %d %Y')}")
        self.ui.vert=QtWidgets.QVBoxLayout(self.ui.WidgetFrame)
        self.ui.vert.setObjectName(u"Layout for Widget")
        

    def AddTask(self):
        frame=QtWidgets.QFrame(self.ui.WidgetFrame)
        framelayout=QtWidgets.QVBoxLayout(frame)
        framelayout.addWidget(TaskDisplayWidget())

        layout= self.ui.vert    

        layout.addWidget(frame)

        




class TaskDisplayWidget(QtWidgets.QWidget):

    def __init__(self) -> None:
        super().__init__()
        ui=TaskDispUI()
        ui.setupUi(self)
        

app=QtWidgets.QApplication(sys.argv)
win=AmberApplicationWindow()
win.AddTask()
win.show()
sys.exit(app.exec_())

    





