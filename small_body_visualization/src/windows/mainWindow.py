from ..widgets.dataTable import PandasModel
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.widgets()
        self.init_window()
    
    def widgets(self):
        layout = QVBoxLayout()
        layout.addWidget(PandasModel)
        

    def init_window(self):
        self.setWindowTitle("Space's Small Body Visualization")
        self.resize(1400, 600)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())