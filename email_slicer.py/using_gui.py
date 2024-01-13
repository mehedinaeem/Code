import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class EmailSlicerApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Email Slicer')
        self.setGeometry(600, 300, 800, 500)
        self.setWindowIcon(QIcon('D:/Code/email_slicer.py/slice_icon.png'))

        # Set background image
        background_label = QLabel(self)
        pixmap = QPixmap('D:/Code/email_slicer.py/Email Slicer.png')
        background_label.setPixmap(pixmap)
        background_label.setGeometry(20, -15, 800, 500)

        main_layout = QVBoxLayout()

        self.result_container = QWidget(self)
        self.result_layout = QVBoxLayout(self.result_container)
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
        self.slice_button.setFixedSize(120, 40)
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
        for i in reversed(range(self.result_layout.count())):
            self.result_layout.itemAt(i).widget().setParent(None)

        for domain, usernames in domain_usernames.items():
            table_widget = QTableWidget(self)
            table_widget.setColumnCount(2)

            # Set column widths to 500 pixels
            table_widget.setColumnWidth(0, 400)
            table_widget.setColumnWidth(1, 400)

            table_widget.setHorizontalHeaderLabels(['Domain', 'Username'])

            # Bold the header titles
            header_font = QFont('Arial', 12, QFont.Bold)
            table_widget.horizontalHeaderItem(0).setFont(header_font)
            table_widget.horizontalHeaderItem(1).setFont(header_font)

            for username in usernames:
                row_position = table_widget.rowCount()
                table_widget.insertRow(row_position)

                domain_item = QTableWidgetItem(domain)
                username_item = QTableWidgetItem(username)

                table_widget.setItem(row_position, 0, domain_item)
                table_widget.setItem(row_position, 1, username_item)

            # Set fixed size for each row
            table_widget.verticalHeader().setDefaultSectionSize(30)

            self.result_layout.addWidget(table_widget)

    def show_error_message(self, message):
        error_label = QLabel(message)
        self.result_layout.addWidget(error_label)


def main():
    app = QApplication(sys.argv)
    window = EmailSlicerApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
