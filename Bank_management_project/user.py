class User:
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_number = self.generate_account_number()
        self.balance = 0
        self.transaction_history = []
        self.loan_count = 0
        self.loan_amount = 0

    account_counter = 1000  # Initialize an account counter

    def generate_account_number(self):
        self.account_number = f"{self.account_type[0].upper()}-{User.account_counter}"
        User.account_counter += 1
        return self.account_number

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount}")
            print(f"Successfully deposited ${amount}.")
        else:
            print("Invalid deposit amount. Please deposit a positive amount.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                self.transaction_history.append(f"Withdrew ${amount}")
                print(f'Successfully withdrew ${amount}.')
            else:
                print(f"Withdrawal amount exceeded. Insufficient balance.")
        else:
            print(f"Invalid withdrawal amount. Please withdraw a positive amount.")

    def get_transaction_history(self):
        return self.transaction_history

    def get_balance(self):
        print(f'Your current Balance ${self.balance}')

    def take_loan(self, amount):
        if self.loan_count < 2:
            if amount <= 0:
                print("Invalid loan amount. Please request a valid loan amount.")
            elif amount > self.balance:
                print("Loan request exceeds your account balance.")
            else:
                self.balance += amount
                self.loan_amount += amount
                self.loan_count += 1
                self.transaction_history.append(f"Loan taken: ${amount}")
                print(f"Loan of ${amount} granted.")
        else:
            print("You have reached the maximum number of allowed loans.")

    def transfer(self, recipient, amount):
        if amount <= 0:
            print("Invalid transfer amount. Please enter a valid amount.")
        elif amount > self.balance:
            print("Insufficient balance for the transfer.")
        else:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(
                f"Transferred ${amount} to {recipient.name}")
            recipient.transaction_history.append(
                f"Received ${amount} from {self.name}")
            print(f"Successfully transferred ${amount} to {recipient.name}.")

    def is_bankrupt(self):
        if self.balance < 0:
            print('Bankrupt')
        else:
            print('Not bankrupt')


# Initialize a list to store user accounts
Accounts = []
