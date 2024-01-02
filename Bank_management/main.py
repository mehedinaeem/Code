from user import User
from user import Accounts
from admin import Admin



# Create an instance of the admin
bank_admin = Admin()

while True:
    print("1. User")
    print("2. Admin")
    print("3. Exit")
    choice = input("Select a role (1/2/3): ")
    print()

    if choice == "1":
        # User Menu
        # Implement user interaction here
        print("Create an account First:")
        user_name = input('Enter name: ')
        user_email = input('Enter email: ')
        user_address = input('Enter address: ')
        user_account_type = input('Enter account type: ')

        # Create a new user account
        new_user = User(user_name, user_email, user_address, user_account_type)
        
        # Add the user to the list of accounts
        Accounts.append(new_user)

        while True:
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check available balance")
            print("4. Check Transaction history")
            print("5. Take loan")
            print("6. Transfer amount")
            print("7. Is Bankrupt")
            print("8. Exit")
            choice1 = input("Select a action (1/2/3/4/5/6/7/8): ")
            print()

            if choice1 == '1':
                amount = int(input('Enter amount: '))
                new_user.deposit(amount)

            elif choice1 == '2':
                amount = int(input('Enter amount: '))
                new_user.withdraw(amount)

            elif choice1 == '3':
                balance = new_user.get_balance()

            elif choice1 == '4':
                transactions = new_user.get_transaction_history()
                for transaction in transactions:
                    print(transaction)

            elif choice1 == '5':
                amount = int(input('Enter loan amount: '))
                new_user.take_loan(amount)

            elif choice1 == '6':
                # Implement the transfer functionality
                 new_user.transfer(recipient=input("Enter name:"),amount=int(input("Enter amount:")))

            elif choice1 == '7':
                if new_user.is_bankrupt():
                    print("The user is bankrupt.")
                else:
                    print("The user is not bankrupt.")

            else:
                break
            
            
#-----------------------------ADMIN PART -----------------------------

    elif choice == "2":
        # Admin Menu
        # Implement admin interaction here
        print("Admin options:")
        print("1. Create an account:")
        print("2. Delete a user account")
        print("3. View all user accounts")
        print("4. Check Total avaiable Balance:")
        print("5. Check Total loan amount:")
        print("6. Can on or off the loan feature:")
        print("7. Exit: ")
        admin_choice = input("Select an admin action (1/2/3/4/5/6/7): ")
        print()

        if admin_choice == '1':
           bank_admin.create_user()
           

        elif admin_choice == '2':
            # Implement user account deletion
            bank_admin.delete_user(input("Enter user:"))

        elif admin_choice == '3':
           bank_admin.see_all_users()

       

        elif admin_choice == '4':
            # Implement enabling/disabling the loan feature
            new_user.get_balance()
        
        elif admin_choice == '5':
            total_loan = bank_admin.total_loan_amount(input("Enter user:"))
            print(f"Total loan amount in the bank: ${total_loan}")
            
            
            
#--------------main part----------------         

    elif choice == "3":
        print("Exiting the system.")
        break

    else:
        print("Invalid choice. Please select 1, 2, or 3.")
