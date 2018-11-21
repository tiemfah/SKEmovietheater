class Reservation:
    def __init__(self, theater_id, showtime, customer, transaction_id, num_reserved_seats, status):
        self.__theater_id = theater_id
        self.__showtime = showtime
        self.__booker = customer
        self.__transaction_id = transaction_id
        self.__num_reserved_seats = num_reserved_seats
        self.__status = status

    def __str__(self):
        return f"BOOKER:#{self.__booker.get_customer_id()} {self.__booker.get_first_name()} {self.__booker.get_last_name()} " \
               f"TRANSACTION#{self.__theater_id} SEATS:{self.__num_reserved_seats} STATUS:{self.__status}"

    def get_str_info(self):
        return f"BOOKER:#{self.__booker.get_customer_id()} {self.__booker.get_first_name()} {self.__booker.get_last_name()} " \
               f"TRANSACTION#{self.__theater_id} SEATS:{self.__num_reserved_seats} STATUS:{self.__status}"
