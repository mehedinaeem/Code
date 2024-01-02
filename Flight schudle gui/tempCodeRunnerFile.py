import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QTextEdit, QLabel, QLineEdit, QDialog, QMessageBox

from admin import FlightAdmin
from user import User

class AirlineApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.admin = FlightAdmin()
        self.user = User()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Airline Management System')
        self.setGeometry(800, 300, 400, 400)
        
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()
        
        self.admin_button = QPushButton('Admin Panel', self)
        self.admin_button.clicked.connect(self.admin_panel)
        
        self.user_button = QPushButton('User Panel', self)
        self.user_button.clicked.connect(self.user_panel)

        
        self.exit_button = QPushButton('Exit', self)
        self.exit_button.clicked.connect(self.close)

        layout.addWidget(self.admin_button)
        layout.addWidget(self.user_button)
        layout.addWidget(self.exit_button)

        self.central_widget.setLayout(layout)

    def admin_panel(self):
        self.admin_window = AdminPanel(self.admin)
        self.admin_window.show()

    def user_panel(self):
        self.user_window = UserPanel(self.admin, self.user)
        self.user_window.show()



# set widget for admin panel

class AdminPanel(QWidget):
    def __init__(self, admin):
        super().__init__()
        self.admin = admin
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Admin Panel')
        self.setGeometry(200, 200, 400, 400)

        layout = QVBoxLayout()

        self.add_button = QPushButton('Add Flight', self)
        self.add_button.clicked.connect(self.add_flight)
        layout.addWidget(self.add_button)

        self.update_button = QPushButton('Update Flight', self)
        self.update_button.clicked.connect(self.update_flight)
        layout.addWidget(self.update_button)

        self.delete_button = QPushButton('Delete Flight', self)
        self.delete_button.clicked.connect(self.delete_flight)
        layout.addWidget(self.delete_button)

        self.textbox = QTextEdit(self)
        layout.addWidget(self.textbox)

        self.setLayout(layout)
   
    def add_flight(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Add Flight")

        layout = QVBoxLayout()

        flight_id_label = QLabel("Flight ID:")
        flight_id_input = QLineEdit()
        layout.addWidget(flight_id_label)
        layout.addWidget(flight_id_input)

        flight_name_label = QLabel("Flight Name:")
        flight_name_input = QLineEdit()
        layout.addWidget(flight_name_label)
        layout.addWidget(flight_name_input)

        departure_time_label = QLabel("Departure Time:")
        departure_time_input = QLineEdit()
        layout.addWidget(departure_time_label)
        layout.addWidget(departure_time_input)

        destination_label = QLabel("Destination:")
        destination_input = QLineEdit()
        layout.addWidget(destination_label)
        layout.addWidget(destination_input)

        add_button = QPushButton("Add Flight")
        add_button.clicked.connect(lambda: self.add_flight_action(
            flight_id_input.text(),
            flight_name_input.text(),
            departure_time_input.text(),
            destination_input.text(),
            dialog
        ))
        layout.addWidget(add_button)

        dialog.setLayout(layout)
        dialog.exec_()

    def add_flight_action(self, flight_id, flight_name, departure_time, destination, dialog):
        if not flight_id or not flight_name or not departure_time or not destination:
            QMessageBox.critical(self, "Error", "All fields are required.")
            return

        flight_details = {
            'id': flight_id,
            'name': flight_name,
            'departure_time': departure_time,
            'destination': destination
        }

        self.admin.add_flight(flight_details)
        dialog.accept()
        self.textbox.append(f"Flight added: {flight_details}")

    def update_flight(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Update Flight")

        layout = QVBoxLayout()

        flight_id_label = QLabel("Flight ID:")
        flight_id_input = QLineEdit()
        layout.addWidget(flight_id_label)
        layout.addWidget(flight_id_input)

        new_flight_name_label = QLabel("New Flight Name:")
        new_flight_name_input = QLineEdit()
        layout.addWidget(new_flight_name_label)
        layout.addWidget(new_flight_name_input)

        new_departure_time_label = QLabel("New Departure Time:")
        new_departure_time_input = QLineEdit()
        layout.addWidget(new_departure_time_label)
        layout.addWidget(new_departure_time_input)

        new_destination_label = QLabel("New Destination:")
        new_destination_input = QLineEdit()
        layout.addWidget(new_destination_label)
        layout.addWidget(new_destination_input)

        update_button = QPushButton("Update Flight")
        update_button.clicked.connect(lambda: self.update_flight_action(
            flight_id_input.text(),
            new_flight_name_input.text(),
            new_departure_time_input.text(),
            new_destination_input.text(),
            dialog
        ))
        layout.addWidget(update_button)

        dialog.setLayout(layout)
        dialog.exec_()

    def update_flight_action(self, flight_id, new_flight_name, new_departure_time, new_destination, dialog):
        if not flight_id:
            QMessageBox.critical(self, "Error", "Flight ID is required.")
            return

        updated_details = {
            'name': new_flight_name,
            'departure_time': new_departure_time,
            'destination': new_destination
        }

        self.admin.update_flight(flight_id, updated_details)
        dialog.accept()
        self.textbox.append(f"Flight {flight_id} updated: {updated_details}")

    def delete_flight(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Delete Flight")

        layout = QVBoxLayout()

        flight_id_label = QLabel("Flight ID:")
        flight_id_input = QLineEdit()
        layout.addWidget(flight_id_label)
        layout.addWidget(flight_id_input)

        delete_button = QPushButton("Delete Flight")
        delete_button.clicked.connect(lambda: self.delete_flight_action(
            flight_id_input.text(),
            dialog
        ))
        layout.addWidget(delete_button)

        dialog.setLayout(layout)
        dialog.exec_()

    def delete_flight_action(self, flight_id, dialog):
        if not flight_id:
            QMessageBox.critical(self, "Error", "Flight ID is required.")
            return

        self.admin.delete_flight(flight_id)
        dialog.accept()
        self.textbox.append(f"Flight {flight_id} deleted.")

class UserPanel(QWidget):
    def __init__(self, admin, user):
        super().__init__()
        self.admin = admin
        self.user = user
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('User Panel')
        self.setGeometry(300, 300, 400, 400)

        layout = QVBoxLayout()

        self.search_button = QPushButton('Search Flights', self)
        self.search_button.clicked.connect(self.search_flights)
        layout.addWidget(self.search_button)

        self.subscribe_button = QPushButton('Subscribe to Delay Notifications', self)
        self.subscribe_button.clicked.connect(self.subscribe_to_notifications)
        layout.addWidget(self.subscribe_button)

        self.textbox = QTextEdit(self)
        layout.addWidget(self.textbox)

        self.setLayout(layout)

    def search_flights(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Search Flights")

        layout = QVBoxLayout()

        destination_label = QLabel("Destination:")
        destination_input = QLineEdit()
        layout.addWidget(destination_label)
        layout.addWidget(destination_input)

        departure_time_label = QLabel("Departure Time:")
        departure_time_input = QLineEdit()
        layout.addWidget(departure_time_label)
        layout.addWidget(departure_time_input)

        search_button = QPushButton("Search Flights")
        search_button.clicked.connect(lambda: self.search_flights_action(
            destination_input.text(),
            departure_time_input.text(),
            dialog
        ))
        layout.addWidget(search_button)

        dialog.setLayout(layout)
        dialog.exec_()

    def search_flights_action(self, destination, departure_time, dialog):
        search_criteria = {}

        if destination:
            search_criteria['destination'] = destination
        if departure_time:
            search_criteria['departure_time'] = departure_time

        flights = self.admin.get_all_flights()
        search_results = self.user.search_flights(search_criteria, flights)

        self.textbox.clear()
        if search_results:
            for result in search_results:
                self.textbox.append(f"Flight ID: {result['id']}, Flight Name: {result['name']}, Departure Time: {result['departure_time']}, Destination: {result['destination']}")
        else:
            self.textbox.append("No flights found matching the criteria.")

        dialog.accept()

    def subscribe_to_notifications(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Subscribe to Delay Notifications")

        layout = QVBoxLayout()

        flight_id_label = QLabel("Flight ID:")
        flight_id_input = QLineEdit()
        layout.addWidget(flight_id_label)
        layout.addWidget(flight_id_input)

        email_label = QLabel("Email Address:")
        email_input = QLineEdit()
        layout.addWidget(email_label)
        layout.addWidget(email_input)

        subscribe_button = QPushButton("Subscribe")
        subscribe_button.clicked.connect(lambda: self.subscribe_to_notifications_action(
            flight_id_input.text(),
            email_input.text(),
            dialog
        ))
        layout.addWidget(subscribe_button)

        dialog.setLayout(layout)
        dialog.exec_()

    def subscribe_to_notifications_action(self, flight_id, email, dialog):
        if not flight_id or not email:
            QMessageBox.critical(self, "Error", "Both Flight ID and Email Address are required.")
            return

        self.user.subscribe_to_delay_notifications(flight_id, email)
        dialog.accept()
        self.textbox.append(f"Subscribed to delay notifications for Flight {flight_id} at {email}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AirlineApp()
    window.show()
    sys.exit(app.exec_())
