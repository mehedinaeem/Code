from user import User,Accounts
class Admin:
    def create_user(self):
        self.loan_amout = 0
        print("Create an account First:")
        user_name = input('Enter name: ')
        user_email = input('Enter email: ')
        user_address = input('Enter address: ')
        user_account_type = input('Enter account type: ')

        new_user = User(user_name, user_email, user_address, user_account_type)
        Accounts.append(new_user)

    def delete_user(self, user):
        if user in Accounts:
            Accounts.remove(user)
            print(f"Account with account number {user.account_number} has been deleted.")
        else:
            print("User not found in the list of accounts.")

    def see_all_users(self):
        print("All User Accounts:")
        for account in Accounts:
            print(f"Account Number: {account.account_number}, Name: {account.name}")

    def total_loan_amount(self, users):
        total_loan = sum(user.loan_amount for user in users if user.loan_amount > 0)
        return total_loan

