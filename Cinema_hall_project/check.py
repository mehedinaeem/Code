class Hall:
    def __init__(self, rows, cols, hall_no):
        self.seats = {}  # Dictionary to store seat information
        self.show_list = []  # List of show information
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

class Star_Cinema:
    hall_list = []  # Class attribute to store Hall objects

    def entry_hall(self, hall_obj):
        self.hall_obj=hall_obj
        Star_Cinema.hall_list.append(hall_obj)

# Example usage:
hall1 = Hall(rows=5, cols=10, hall_no=1)
hall2 = Hall(rows=7, cols=12, hall_no=2)

cinema = Star_Cinema()
cinema.entry_hall(hall1)
cinema.entry_hall(hall2)

print(hall1.hall_no,hall1.rows,hall1.cols,hall1.seats)



# # Checking the hall_list
# for hall in Star_Cinema.hall_list:
#     print(f"Hall {hall.hall_no}: Rows {hall.rows}, Columns {hall.cols}")
