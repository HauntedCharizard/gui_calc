import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QLabel

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SpinBox Example")

        self.layout = QVBoxLayout()

        self.spinBox1 = QSpinBox()
        self.spinBox1.setMinimum(0)
        self.spinBox1.setMaximum(100)
        self.spinBox1.valueChanged.connect(self.update_label)

        self.spinBox2 = QSpinBox()
        self.spinBox2.setMinimum(0)
        self.spinBox2.setMaximum(100)
        self.spinBox2.valueChanged.connect(self.update_label)

        self.label = QLabel("Sum: 0")

        self.layout.addWidget(self.spinBox1)
        self.layout.addWidget(self.spinBox2)
        self.layout.addWidget(self.label)

        self.setLayout(self.layout)

    def update_label(self):
        sum_val = self.spinBox1.value() + self.spinBox2.value()
        self.label.setText(f"Sum: {sum_val}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
