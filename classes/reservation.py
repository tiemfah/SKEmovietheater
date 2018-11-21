class Reservation:
    def __init__(self, theater_id, showtime, customer, transaction_id, num_reserved_seats, status):
        self.__theater_id = theater_id
        self.__showtime = showtime
        self.__booker = customer
        self.__transaction_id = transaction_id
        self.__num_reserved_seats = num_reserved_seats
        self.__status = status

    def get_all(self):
        return self.__theater_id, self.__showtime, self.__booker,\
               self.__transaction_id, self.__num_reserved_seats, self.__status

    def __str__(self):
        the_id, showtime, booker, transaction_id, num, status = self.get_all()
        return f"BOOKER:#{booker.get_customer_id()} {booker.get_first_name()} {booker.get_last_name()} " \
               f"TRANSACTION#{transaction_id} SEATS:{num} STATUS:{status}"

    def get_str_info(self):
        the_id, showtime, booker, transaction_id, num, status = self.get_all()
        return f"BOOKER:#{booker.get_customer_id()} {booker.get_first_name()} {booker.get_last_name()} " \
               f"TRANSACTION#{transaction_id} SEATS:{num} STATUS:{status}"
