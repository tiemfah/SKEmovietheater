from classes.customer import *
from classes.mytime import *
from classes.reservation import *
from classes.theater import *
from classes.transaction import *

print(">>> Create and Print Customers")
ann = Customer("Ann", "Smith")
beth = Customer("Beth", "Thomas")
charlie = Customer("Charlie", "Rogers")
print(ann)
print(beth)
print(charlie)
print()

print(">>> Create and Print Theater ")
theater1 = Theater("Superman", 12, 10)
print(theater1)
print()

print(">>> Add reservation to Theater ")
if theater1.reserve(ann, 3) == -1:
    print("Unsuccessful Reservation")
    print(theater1)
print()
if theater1.reserve(beth, 5) == -1:
    print("Unsuccessful Reservation")
else:
    print(theater1)
print()
if theater1.reserve(charlie, 4) == -1:
    print("Unsuccessful Reservation")
else:
    print(theater1)
print()

print(">>> Print Theater information")
print(theater1.get_reserved_seating_info())
print(">> Ann: coming_transactions")
print(ann.get_coming_transactions_info())
print(">> Beth: coming_transactions")
print(beth.get_coming_transactions_info())

print(">>> Cancel Ann's Reservation for Theater 1, showtime = 12:00")
theater1.cancel(ann, 1, MyTime(12, 0, 0))
print(theater1.get_reserved_seating_info())
print(">> Ann: coming_transactions")
print(ann.get_coming_transactions_info())
print(">> Ann: history_transactions")
print(ann.get_history_transactions_info())
print()

print(">>> Clear reservations of Theater 1 after showtime is over.")
theater1.clear()
print(">>> Print Theater information")
print(theater1.get_reserved_seating_info())
print(">> Ann: coming_transactions")
print(ann.get_coming_transactions_info())
print(">> Ann: history_transactions")
print(ann.get_history_transactions_info())

print(">> Beth: coming_transactions")
print(beth.get_coming_transactions_info())
print(">> Beth: history_transactions")
print(beth.get_history_transactions_info())
