 # Initialize a list to store user accounts
Accounts = []

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
        # self.loan_limit=2
        

    account_counter = 1000  # initialize an account counter

    def generate_account_number(self):
        # Generate a unique account number (e.g., based on a counter or random)
        # Return the generated account number
        self.account_number = f"{self.account_type[0].upper()}-{User.account_counter}"
        User.account_counter += 1
        return self.account_number

    # def deposit(self, amount):
    #     # Deposit the specified amount into the user's account
    #     pass

    # def withdraw(self, amount):
    #     # Check if withdrawal amount is greater than balance
    #     # If sufficient balance, withdraw the amount
    #     # If not, show an error message
    #     pass

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
        # Return the transaction history
        return self.transaction_history
    
    
    def get_balance(self):
        # Return the user's current balance
        print(f'your current Balance ${self.balance}')

    # def take_loan(self, amount):
    #     # Check if the user is eligible for a loan
    #     # If eligible, grant the loan and update the loan count
    #     pass

    def take_loan(self, amount):
        # Check if the user is eligible for a loan
        if self.loan_count < 2:
            # self.loan_count+=1
            # You can define additional criteria here (e.g., credit score)
            if amount <= 0:
                print("Invalid loan amount. Please request a valid loan amount.")
            elif amount > self.balance:
                print("Loan request exceeds your account balance.")
            else:
                self.balance += amount  # Grant the loan by adding it to the user's balance
                self.loan_count += 1  # Increment the loan count
                self.transaction_history.append(f"Loan taken: ${amount}")
                print(f"Loan of ${amount} granted.")
        else:
            print("You have reached the maximum number of allowed loans.")

    # def transfer(self, recipient, amount):
    #     # Transfer the specified amount to another user's account
    #     # Check if the recipient account exists, and if the user has sufficient balance
    #     pass

    def transfer(self, recipient, amount):
        self.recepient=recipient
        # Check if the recipient account exists
        # if not isinstance(recipient):
        #     print("Recipient account does not exist.")

        # Check if the user has sufficient balance for the transfer
        if amount <= 0:
            print("Invalid transfer amount. Please enter a valid amount.")
        elif amount > self.balance:
            print("Insufficient balance for the transfer.")

        # Perform the transfer
        self.balance -= amount
        # recipient.balance += amount

        # Update transaction history for both the sender and recipient
        self.transaction_history.append( f"Transferred ${amount}")
        # recipient.transaction_history.append(f"Received ${amount} from {self.name}")

        print(f"Successfully transferred ${amount}.")

    def is_bankrupt(self):
        # Check if the user is unable to withdraw their deposited amount
        # If bankrupt, show an error message
        if self.balance < 0:
            print('Bankrupt')
        else:
            print('Not bankrupt')
