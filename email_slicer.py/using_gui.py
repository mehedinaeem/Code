import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

class EmailSlicerApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Email Slicer')
        self.setGeometry(700, 450, 500, 300)

        layout = QVBoxLayout()

        self.email_label = QLabel("Input your email address:")
        layout.addWidget(self.email_label)

        self.email_input = QLineEdit()
        layout.addWidget(self.email_input)

        self.result_label = QLabel()
        layout.addWidget(self.result_label)

        self.slice_button = QPushButton("Slice Email")
        self.slice_button.clicked.connect(self.slice_email)
        layout.addWidget(self.slice_button)

        self.exit_button = QPushButton("Exit")
        self.exit_button.clicked.connect(self.close)
        layout.addWidget(self.exit_button)

        self.setLayout(layout)

    def slice_email(self):
        email = self.email_input.text()
        try:
            (username, domain) = email.split("@")
            (domain, extension) = domain.split(".")
            result_text = f"Username: {username}\nDomain: {domain}\nExtension: {extension}"
            self.result_label.setText(result_text)
        except ValueError:
            self.result_label.setText("Invalid email format. Please use 'username@domain.extension'")

def main():
    app = QApplication(sys.argv)
    window = EmailSlicerApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
