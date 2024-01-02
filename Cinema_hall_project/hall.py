class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall_obj):
        self.hall_obj = hall_obj
        Star_Cinema.hall_list.append(hall_obj)

class Hall:
    def __init__(self, rows, cols, hall_no):
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

# Make an object
cayabani = Hall(5, 7, 1122)
sinema = Star_Cinema()
sinema.entry_hall(cayabani)

print(sinema.hall_list[0],sinema.hall_list[1],sinema.hall_list[2])

# Access the attributes of the first hall in the hall_list
# if Star_Cinema.hall_list:
#     first_hall = Star_Cinema.hall_list[0]
#     print("Hall No:", first_hall.hall_no)
#     print("Rows:", first_hall.rows)
#     print("Columns:", first_hall.cols)
