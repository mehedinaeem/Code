# main.py
from admin import FlightAdmin
from user import User

def main():
    admin = FlightAdmin()
    user = User()

    while True:
        print("1. Admin Panel")
        print("2. User Panel")
        print("3. Exit")
        choice = input("Enter your choice: ")



#-----------------------------Admin part-----------------------------------
        if choice == "1":
            print("Admin Panel")
            print("1. Add Flight")
            print("2. Update Flight")
            print("3. Delete Flight")
            admin_choice = input("Enter your admin choice: ")

            if admin_choice == "1":
                flight_details = {
                    'id': input("Flight ID: "),
                    'name': input("Flight Name: "),
                    'departure_time': input("Departure Time: "),
                    'destination': input("Destination: "),
                }
                admin.add_flight(flight_details)

            elif admin_choice == "2":
                flight_id = input("Enter the Flight ID to update: ")
                updated_details = {
                    'name': input("New Flight Name: "),
                    'departure_time': input("New Departure Time: "),
                    'destination': input("New Destination: "),
                }
                admin.update_flight(flight_id, updated_details)

            elif admin_choice == "3":
                flight_id = input("Enter the Flight ID to delete: ")
                admin.delete_flight(flight_id)



#-----------------------------------User part-----------------------------------------
        elif choice == "2":
            print("User Panel")
            print("1. Search Flights")
            print("2. Subcribe for Delay Notifications")
            user_choice = input("Enter your user choice: ")

            if user_choice == "1":
                search_criteria = {
                    'destination': input("Enter Destination: "),
                    'departure_time': input("Enter Departure Time: "),
                }
                flights = admin.get_all_flights()
                search_results = user.search_flights(search_criteria, flights)
                
                print("Search Results:")
                
                if search_results:
                    for result in search_results:
                        print(result)
                else:
                    print("No flight available")

            elif user_choice == "2":
                flight_id = input("Enter Flight ID to subscribe to delay notifications: ")
                email = input("Enter your email: ")
                user.subscribe_to_delay_notifications(flight_id, email)
                
                
                
                

        elif choice == "3":
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
