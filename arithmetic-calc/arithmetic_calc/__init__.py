import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QDoubleSpinBox,
    QMainWindow,
    QPushButton,
    QSpinBox,
    QWidget,
    QVBoxLayout,
    QLabel,
    QSizePolicy,
    QHBoxLayout,
)

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Arithmetic Calculator")
        self.setMinimumSize(500, 500)

        label = QLabel("Arithmetic Calculator")
        label.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        ops = QComboBox()
        ops.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed) # Changes the size of the variables 
        ops.addItem("+") # Adding options to the ComboBox
        ops.addItem("-")
        ops.addItem("x")
        ops.addItem("//")

        num1 = QSpinBox()
        num2 = QSpinBox()
        num1.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        num2.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        num1.setRange(-1000000, 1000000)
        num2.setRange(-1000000, 1000000)

        button1 = QPushButton("Calculate!")
        button2 = QPushButton("Reset")
      

        # Create a horizontal layout for the QComboBoxes
        combo_layout = QHBoxLayout()
        combo_layout.addWidget(num1)
        combo_layout.addWidget(ops)
        combo_layout.addWidget(num2)

        # Creating another Horizontal Layout for the Qbuttons
        button_layout = QHBoxLayout()
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)

        # Creates a central widget (Like a container to hold the other widgets)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # "QVBoxLayout" makes a vertical layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Add Widgets to the layout
        layout.addWidget(label)
        layout.addLayout(combo_layout)
        layout.addLayout(button_layout)

app = QApplication(sys.argv)
app.setStyleSheet("""
    QWidget {
        background-color:#b7e4e7;
    }
                  
    QLabel, QSpinBox, QComboBox {
        border-radius:20px;
    }
                  
    QLabel {
        color:#0097b2;
        font-weight:bold;
        font-size:37px;
        border: 2px solid #1E0343;
        padding-left:auto;
        padding-right:auto;
        margin-left:60px;
        margin-right:auto;
        background-color:#c8f9dc;
        letter-spacing:4px;
                         
    }
                  
    QSpinBox {
        height:100px;
        font-size:35px;
        border:2px solid #0E46A3;
        width:100px;
        background-color:#98befc;
                
    }
                  
    QComboBox {
        height:50px;
        width:100px;
        font-size:29px;
        border: 2px solid #0E46A3;
    }
                  
    QPushButton {
        background-color:#c8f9dc;
        font-size: 25px;
        font-weight:bold;
        border:2px solid #0E46A3;
        border-radius:20px;

    }
                  
    QPushButton:hover {
        color:#98befc;
    }
    QPushButton:pressed {
        color:red;
    }
""")

window = MainWindow()
window.show()

sys.exit(app.exec())
