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

    def view_seat_matrix(self, id):
        if id not in self._seats:
            return "Invalid show ID"
        return self._seats[id]


# make object
cinema = Star_Cinema()
cineplex = Hall(5, 7, 1122)
cinema.entry_hall(cineplex)

cineplex.entry_show("show1", "Spider Man", "18:00")
cineplex.entry_show("show2", "Super Man", "20:00")


while True:
    print('\n')
    print('1. View all show list')
    print('2. View available seat')
    print('3. Book Ticket')
    print('4. Exit')

    n = int(input('Enter option: '))
    if n == 1:
        print("Show list:", cineplex.view_show_list())

    if n == 2:
        show_id = input("Enter show ID: ")
        seat_matrix = cineplex.view_seat_matrix(show_id)
        for row in seat_matrix:
            print(" ".join(['1' if seat == 'booked' else '0' for seat in row]))

    if n == 3:
        show_id = input("Enter show ID: ")
        seats_to_book = eval(
            input("Enter seats to book as a list of tuples (like that [(1, 2), (2, 3)]): "))
        print(cineplex.book_seats(show_id, seats_to_book))

    if n == 4:
        break
