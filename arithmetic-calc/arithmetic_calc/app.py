import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    
    QComboBox,
    QDoubleSpinBox,
    QMainWindow,
    QPushButton,
    QSpinBox,
    QWidget,
    QApplication,
    QVBoxLayout,
    QLabel
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Arithmetic Calculator")

        layout = QVBoxLayout()
        widgets = [
            QComboBox,
            QSpinBox,
            
        ]

        for w in widgets:
            layout.addWidget(w())

        widget = QWidget()
        widget.setLayout(layout)
        self.setMinimumSize(400,400)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)
        
        button = QPushButton("Test Button", self)
        button.move(150,150)


app = QApplication(sys.argv)
app.setStyleSheet("""
    QWidget {
                  background-color:#B2FFFF;
                  color:white;

    }
    QSpinBox, QPushButton, QComboBox, QDoubleSpinBox {
                  background-color:#318CE7;
    }
    QPushButton {
                align-content: center; 
    }
""")


window = MainWindow()
window.show()

app.exec()
