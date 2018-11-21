class Transaction:
    NUM_TRANSACTION = 1

    def __init__(self, theater_id, show_time, num_reserved_seats, payment, status):
        self.__transaction_id = Transaction.NUM_TRANSACTION
        self.__theater_id = theater_id
        self.__show_time = show_time
        self.__num_reserved_seats = num_reserved_seats
        self.__payment = payment
        self.__status = status
        Transaction.NUM_TRANSACTION += 1

    def get_transaction_all(self):
        return self.__transaction_id, self.__theater_id, self.__show_time,\
               self.__num_reserved_seats, self.__payment, self.__status

    def __str__(self):
        tran_id, thea_id, showtime, seats, payment, status = self.get_transaction_all()
        return f"TRANSACTION#{tran_id}, THEATER:{thea_id}, SHOWTIME:{showtime}," \
               f" SEAT#{seats}, PAYMENT:{payment}, STATUS:{status}"

    def get_str_info(self):
        tran_id, thea_id, showtime, seats, payment, status = self.get_transaction_all()
        return f"TRANSACTION#{tran_id}, THEATER:{thea_id}, SHOWTIME:{showtime}," \
               f" SEAT#{seats}, PAYMENT:{payment}, STATUS:{status}"

    def get_id(self):
        return self.__transaction_id

    def set_status(self, new_status):
        self.__status = new_status