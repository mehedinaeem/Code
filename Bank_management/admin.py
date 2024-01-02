from user import Accounts
from user import User
class Admin:
    def create_user(self):
        # Create a new user account and add it to the user list
        # User Menu
        # Implement user interaction here
        self.loan_amout=0
        print("Create an account First:")
        user_name = input('Enter name: ')
        user_email = input('Enter email: ')
        user_address = input('Enter address: ')
        user_account_type = input('Enter account type: ')

        # Create a new user account
        new_user = User(user_name, user_email, user_address, user_account_type)
        
        # Add the user to the list of accounts
        Accounts.append(new_user)

    def delete_user(self, user):
        # Delete a user account
        if user in Accounts:
            Accounts.remove(user)
            print(f"Account with account number {user.account_number} has been deleted.")
        else:
            print("User not found in the list of accounts.")

    def see_all_users(self):
        # Display a list of all user accounts
        print("All User Accounts:")
        for account in Accounts:
            print(f"Account Number: {account.account_number}, Name: {account.name}")

    def total_available_balance(self, users):
        # Calculate and return the total balance of all user accounts
        pass

    def total_loan_amount(self, users):
        pass

    def toggle_loan_feature(self, is_enabled):
        # Enable or disable the loan feature of the bank
        pass

# Add admin-specific methods and attributes here
