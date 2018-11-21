from Transaction import Transaction
from reservation import Reservation
from mytime import MyTime

class Theater:
    NUM_THEATER, TICKET_PRICE = 1, 150

    def __init__(self, movie, hour, num_seats):
        self.__theater_id = Theater.NUM_THEATER
        self.__showtime = MyTime(hour, 0, 0)
        self.__movie = movie
        self.__num_seats = num_seats
        self.__num_reserved = 0
        self.__reserved_seats = []
        Theater.NUM_THEATER += 1

    def __str__(self):
        return f"Theater #{self.__theater_id}, Showtime: {self.__showtime}:, Movie: {self.__movie}\n" \
               f"Total seats: {self.__num_seats}, Reserved seats: {self.__num_reserved}"

    def get_str_info(self):
        return f"Theater #{self.__theater_id}, Showtime: {self.__showtime}:, Movie: {self.__movie}\n" \
               f"Total seats: {self.__num_seats}, Reserved seats: {self.__num_reserved}"

    def get_reserved_seating_info(self):
        """
        return string of basic theater information and list of reservation See sample output below.
        print(">>> Print Theater information") print(theater1.get_reserved_seating_info())

        Print Theater information Theater #1,
        Showtime: 12:00:00:, Movie: Superman
        Total seats: 10,Reserved seats: 8
        Booker: 1,Ann,Smith, Transaction #: 1,#Seats: 3, Status: Reserved
        Booker: 2,Beth,Thomas, Transaction #: 2, #Seats: 5, Status: Reserved
        """
        return f"{self.get_str_info()}, '\n', {',\n'.join([str(reservation) for reservation in self.__reserved_seats])}"

    def reserve(self, customer, num_reserved_seat):
        """
        1) create transaction and add to coming_transactions list belonging to customer. Return transaction ID.
        2) create reservation and add to the list of reservations for this theater
        3) update num_reserved
        4) return 1 if reservation is successful; otherwise, return -1
        print(">>> Add reservation to Theater ")
        if (theater1.reserve(ann, 3) == -1):
            print("Unsuccessful Reservation")
        else:
            print(theater1)

         Add reservation to Theater  Theater 1, Showtime: 12:00:00:, Movie: Superman Total seats: 10, Reserved seats: 3
        """
        if self.__num_reserved + num_reserved_seats <= self.__num_seats:
            transaction = Transaction(self.__theater_id, self.__showtime, num_reserved_seats, num_reserved_seats * Theater.TICKET_PRICE, "Paid")
            customer.add_transaction(transaction)
            reservation = Reservation(self.__theater_id, self.__showtime, customer, transaction.get_transaction_id(), num_reserved_seats, "Reserved")
            self.__reserved_seatings.append(reservation)
            self.__num_reserved += num_reserved_seats
            return 1
        return -1

    def clear(self):
        """
        1) write information from list of reservations to text file.
            Filename format is “reservation_theaterID_showtimeHour.txt”.
            See sample output of text file below
        2) move transaction from coming_transactions to history_transactions for all ticket booker
        3) set list of reservations to be empty and set num_reserved = 0

        print(">>> Clear reservations of Theater 1 after showtime is over.") theater1.clear()

        """
        pass

    def search_reserved_seating(self, customer, theater_id, showtime):
        """
        search list of reservations for reservation with the given customer, theater_id and showtime.
        Return transaction ID of such reservation.
        If not exist, return -1. • remove_reserved_seating(transaction_id):
         remove reservation with transaction ID from the list
        :param customer:
        :param theater_id:
        :param showtime:
        :return:
        """
        pass

    def cancel(self, customer, theater_id, showtime):
        """
        1) search for transaction ID with the given information of customer, theater_id and showtime,
        2) cancel transaction with the specific transaction ID from customer,
        3) remove reservation from the list
        """
        pass
