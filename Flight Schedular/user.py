# user.py

class User:
    def search_flights(self, search_criteria, flights):
        results = []
        for flight in flights:
            if all(flight[key] == value for key, value in search_criteria.items()):
                results.append(flight)
        return results

    def subscribe_to_delay_notifications(self, flight_id, email):
        # subscribing to delay notifications
        
        # TODO: if delay send email 
        print(f"Subscribed to delay notifications for Flight {flight_id} at {email}")
