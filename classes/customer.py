class Customer:
    NUM_CUSTOMERS = 0

    def __init__(self, first_name, last_name):
        Customer.NUM_CUSTOMERS += 1
        self.__customer_id = Customer.NUM_CUSTOMERS
        self.__first_name = first_name
        self.__last_name = last_name
        self.__history_transaction = []
        self.__coming_transaction = []

    def __str__(self):
        return f"{self.__customer_id}, {self.__first_name} {self.__last_name}"

    def get_str_info(self):
        return f"{self.__customer_id}, {self.__first_name} {self.__last_name}"

    def get_customer_id(self):
        return self.__customer_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def add_transaction(self, transaction):
        self.__coming_transaction.append(transaction)
        return transaction.NUM_TRANSACTION

    def moveto_history_transaction(self, transaction_id):
        for ele in range(len(self.__coming_transaction)):
            print(self.__coming_transaction[ele])
            if self.__coming_transaction[ele].get_id() == transaction_id:
                self.__history_transaction.append(self.__coming_transaction[ele])
                self.__coming_transaction.pop(ele)
                break

    def cancel_transaction(self, transaction_id):
        for ele in range(len(self.__coming_transaction)):
            if self.__coming_transaction[ele].get_id() == transaction_id:
                self.__coming_transaction[ele].set_status('Canceled')
                self.__history_transaction.append(self.__coming_transaction[ele])
                self.__coming_transaction.pop(ele)
                break

    def get_history_transactions_info(self):
        temp = "\n".join([ele.get_str_info() for ele in self.__history_transaction])
        return f'{self.get_str_info()}\n{temp}'

    def get_coming_transactions_info(self):
        temp = "\n".join([ele.get_str_info() for ele in self.__coming_transaction])
        return f'{self.get_str_info()}\n{temp}'
