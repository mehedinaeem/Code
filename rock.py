import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

class RockPaperScissorsGame(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Rock Paper Scissors Game")
        self.setGeometry(100, 100, 400, 200)

        self.user_score = 0
        self.computer_score = 0

        self.user_choice_label = QLabel("Your Choice:", self)
        self.user_choice_label.setGeometry(20, 20, 100, 30)

        self.rock_button = QPushButton("Rock", self)
        self.rock_button.setGeometry(140, 20, 80, 30)
        self.rock_button.clicked.connect(lambda: self.set_user_choice("Rock"))

        self.paper_button = QPushButton("Paper", self)
        self.paper_button.setGeometry(230, 20, 80, 30)
        self.paper_button.clicked.connect(lambda: self.set_user_choice("Paper"))

        self.scissors_button = QPushButton("Scissors", self)
        self.scissors_button.setGeometry(320, 20, 80, 30)
        self.scissors_button.clicked.connect(lambda: self.set_user_choice("Scissors"))

        self.computer_choice_label = QLabel("Computer Choice:", self)
        self.computer_choice_label.setGeometry(20, 70, 150, 30)

        self.result_label = QLabel("", self)
        self.result_label.setGeometry(20, 120, 360, 30)

        self.play_button = QPushButton("Play", self)
        self.play_button.setGeometry(140, 170, 80, 30)
        self.play_button.clicked.connect(self.play_game)

    def set_user_choice(self, choice):
        self.user_choice = choice

    def get_computer_choice(self):
        return random.choice(["Rock", "Paper", "Scissors"])

    def determine_winner(self):
        computer_choice = self.get_computer_choice()
        self.computer_choice_label.setText(f"Computer Choice: {computer_choice}")

        if self.user_choice == computer_choice:
            result = "It's a tie!"
        elif (
            (self.user_choice == "Rock" and computer_choice == "Scissors") or
            (self.user_choice == "Paper" and computer_choice == "Rock") or
            (self.user_choice == "Scissors" and computer_choice == "Paper")
        ):
            result = "You win!"
            self.user_score += 1
        else:
            result = "Computer wins!"
            self.computer_score += 1

        self.result_label.setText(result)

    def play_game(self):
        if hasattr(self, 'user_choice'):
            self.determine_winner()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game_window = RockPaperScissorsGame()
    game_window.show()
    sys.exit(app.exec_())