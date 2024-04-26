import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel

class NestedLayoutExample(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Create the main vertical layout
        main_layout = QVBoxLayout()

        # Create a horizontal layout
        horizontal_layout = QHBoxLayout()

        # Create widgets to add to the horizontal layout
        label1 = QLabel("Label 1")
        label2 = QLabel("Label 2")
        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")

        # Add widgets to the horizontal layout
        horizontal_layout.addWidget(label1)
        horizontal_layout.addWidget(button1)
        horizontal_layout.addWidget(label2)
        horizontal_layout.addWidget(button2)

        # Add the horizontal layout to the main vertical layout
        main_layout.addLayout(horizontal_layout)

        # Add some extra widgets to the main vertical layout
        button3 = QPushButton("Button 3")
        button4 = QPushButton("Button 4")
        main_layout.addWidget(button3)
        main_layout.addWidget(button4)

        self.setLayout(main_layout)

        self.setWindowTitle("Nested Layout Example")
        self.show()

def main():
    app = QApplication(sys.argv)
    ex = NestedLayoutExample()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
