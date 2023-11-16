
#! python -m PyQt5.uic.pyuic -x untitled.ui -0 ui.py
class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow
        self.ui.setupUi(self)
        