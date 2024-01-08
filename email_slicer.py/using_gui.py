import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class EmailSlicerApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Email Slicer')
        self.setGeometry(600, 300, 800, 500)
        self.setWindowIcon(QIcon('D:/Code/email_slicer.py/slice_icon.png'))

        # Set background color
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), Qt.gray)  
        self.setPalette(palette)

        main_layout = QVBoxLayout()

        self.result_container = QWidget(self)
        self.result_container.setLayout(QHBoxLayout())
        main_layout.addWidget(self.result_container)

        # Create a sub-layout for the bottom row
        bottom_row_layout = QHBoxLayout()

        self.email_label = QLabel(
            "Input your email addresses \n      separated by commas:", self)
        bottom_row_layout.addWidget(self.email_label)

        self.email_input = QLineEdit(self)
        # Set a fixed size for the input box
        self.email_input.setFixedSize(440, 60)
        self.email_input.setStyleSheet(
            "background-color:#9EAE9D; color:black;font-size:25px")
        bottom_row_layout.addWidget(self.email_input)

        self.slice_button = QPushButton("Slice Emails", self)
        self.slice_button.setFixedSize(80, 40)
        self.slice_button.setStyleSheet(
            "background-color: #4CAF50; color: white;font-weight:bold")
        self.slice_button.clicked.connect(self.slice_emails)
        bottom_row_layout.addWidget(self.slice_button)

        self.exit_button = QPushButton("Exit", self)
        self.exit_button.setFixedSize(80, 40)
        self.exit_button.setStyleSheet(
            "background-color: red; color: white; font-weight:bold")
        self.exit_button.clicked.connect(self.close)
        bottom_row_layout.addWidget(self.exit_button)

        main_layout.addLayout(bottom_row_layout)

        self.setLayout(main_layout)

    def slice_emails(self):
        emails = self.email_input.text().split(',')
        domain_usernames = {}

        for email in emails:
            try:
                (username, domain) = email.strip().split("@")

                # Store usernames for each domain
                if domain not in domain_usernames:
                    domain_usernames[domain] = []

                domain_usernames[domain].append(username)
            except ValueError:
                self.show_error_message(
                    "Invalid email format. Please use 'username@domain.extension'")
                return

        self.display_result(domain_usernames)

    def display_result(self, domain_usernames):
        # Clear previous results
        for i in reversed(range(self.result_container.layout().count())):
            self.result_container.layout().itemAt(i).widget().setParent(None)

        for domain, usernames in domain_usernames.items():
            domain_layout = QVBoxLayout()

            # Set margins to zero to eliminate default spacing
            domain_layout.setContentsMargins(0, 0, 0, 0)

            # Use HTML formatting to bold and underline the domain name
            domain_label_text = f"<b><u><span style='font-size: 20px;'>{domain}</span></u></b><br>total mail number: {len(usernames)}"

            domain_label = QLabel(domain_label_text)
            domain_layout.addWidget(domain_label)

            usernames_label = QLabel(
                f"<span style='text-decoration: underline; font-size:20 px;'>Usernames:</span><br>" + "<br>".join(usernames), self)

            domain_layout.addWidget(usernames_label)

            self.result_container.layout().addLayout(domain_layout)

    def show_error_message(self, message):
        error_label = QLabel(message)
        self.result_container.layout().addWidget(error_label)


def main():
    app = QApplication(sys.argv)
    window = EmailSlicerApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
