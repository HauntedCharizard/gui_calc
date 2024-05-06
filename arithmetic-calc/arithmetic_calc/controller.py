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

        self.ops = QComboBox()  # Fix: Define ops as an attribute of MainWindow
        self.ops.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        self.ops.addItem("+")
        self.ops.addItem("-")
        self.ops.addItem("×")
        self.ops.addItem("÷")

        self.num1 = QSpinBox()
        self.num2 = QSpinBox()
        self.num1.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        self.num2.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        self.num1.setRange(-1000000, 1000000)
        self.num2.setRange(-1000000, 1000000)

        self.ans_label = QLabel("Answer: ")
        self.ans_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.ans_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        button1 = QPushButton("Calculate!")
        button2 = QPushButton("Reset")

        # Create a horizontal layout for the QComboBoxes
        combo_layout = QHBoxLayout()
        combo_layout.addWidget(self.num1)
        combo_layout.addWidget(self.ops)  # Fix: Use self.ops instead of ops
        combo_layout.addWidget(self.num2)

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
        layout.addWidget(self.ans_label)
        layout.addLayout(button_layout)

        # Connect the "clicked" signal of the "Calculate!" button to the calculation function
        button1.clicked.connect(self.calculate)

    def calculate(self):
        # Get the selected operator
        operator = self.ops.currentText()  # Fix: Use self.ops instead of ops
        num1 = self.num1.value()
        num2 = self.num2.value()

        # Perform the corresponding operation
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "×":
            result = num1 * num2
        elif operator == "÷":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Division by zero"

        # Update the answer label with the result
        self.ans_label.setText(f"Answer: {result}")


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
        color:#78befc;
    }
  
                  
""")

window = MainWindow()
window.show()

sys.exit(app.exec())
