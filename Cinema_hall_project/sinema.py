class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall_obj):
        Star_Cinema.hall_list.append(hall_obj)


class Hall:
    def __init__(self, rows, cols, hall_no):
        self._seats = {}  # protected attribute
        self._show_list = []  # protected attribute
        self._rows = rows  # protected attribute
        self._cols = cols  # protected attribute
        self._hall_no = hall_no  # protected attribute

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)  # Tuple
        self._show_list.append(show_info)
        self._seats[id] = [['free' for _ in range(
            self._cols)] for _ in range(self._rows)]

    def book_seats(self, id, seats_to_book):
        if id not in self._seats:
            return "Invalid show ID"

        for seat in seats_to_book:
            row, col = seat
            if row < 1 or row > self._rows or col < 1 or col > self._cols:
                return "Invalid seat"
            if self._seats[id][row - 1][col - 1] == 'booked':
                return f"Seat ({row}, {col}) is already booked"
            self._seats[id][row - 1][col - 1] = 'booked'
        return "Seats booked successfully"

    def view_show_list(self):
        return self._show_list

    def view_available_seats(self, id):
        if id not in self._seats:
            return "Invalid show ID"

        available_seats = []
        for row in range(self._rows):
            for col in range(self._cols):
                if self._seats[id][row][col] == 'free':
                    available_seats.append((row + 1, col + 1))
        return available_seats


# make object
cinema = Star_Cinema()
cineplex = Hall(5, 7, 1122)
cinema.entry_hall(cineplex)

cineplex.entry_show("show1", "Spidern Man", "18:00")
cineplex.entry_show("show2", "Super Man", "20:00")

print('1.view all show list')
print('2.View avaiable seat')
print('3.Book Ticket')
print('4.Exit')

while True:
    n = int(input('Enter option: '))
    if n == 1:
        print("Show list:", cineplex.view_show_list())

    if n == 2:
        print("Available seats for show1:",
              cineplex.view_available_seats("show1"))

    if n == 3:
        print(cineplex.book_seats("show1", [(1, 2), (2, 3), (3, 4)])) 
        print(cineplex.book_seats("show1", [(1, 2), (2, 3)]))  # Already booked seats
        print(cineplex.book_seats("show3", [(1, 2), (2, 3)]))   # Invalid show ID
        
    if n== 4:
        break