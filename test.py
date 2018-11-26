from classes.customer import Customer
from classes.mytime import MyTime
from classes.reservation import Reservation
from classes.theater import Theater
from classes.transaction import Transaction

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
print()
print(">> Ann: coming_transactions")
print(ann.get_coming_transactions_info())
print()
print(">> Beth: coming_transactions")
print(beth.get_coming_transactions_info())
print()

print(">>> Cancel Ann's Reservation for Theater 1, showtime = 12:00")
theater1.cancel(ann, 1, MyTime(12, 0, 0))
print(theater1.get_reserved_seating_info())
print()
print(">> Ann: coming_transactions")
print(ann.get_coming_transactions_info())
print(">> Ann: history_transactions")
print(ann.get_history_transactions_info())
print()

print(">>> Clear reservations of Theater 1 after showtime is over.")
theater1.clear()
print()
print(">>> Print Theater information")
print(theater1.get_reserved_seating_info())
print()
print(">> Ann: coming_transactions")
print(ann.get_coming_transactions_info())
print(">> Ann: history_transactions")
print(ann.get_history_transactions_info())

print(">> Beth: coming_transactions")
print(beth.get_coming_transactions_info())
print(">> Beth: history_transactions")
print(beth.get_history_transactions_info())

"""
>>> Create and Print Customers 
    1,Ann,Smith 
    2,Beth,Thomas 
    3,Charlie,Rogers 
 
>>> Create and Print Theater
    Theater 1, Showtime: 12:00:00:, Movie: Superman 
    Total seats: 10, Reserved seats: 0 
 
>>> Add reservation to Theater
    Theater 1, Showtime: 12:00:00:, Movie: Superman 
    Total seats: 10, Reserved seats: 3 
 
    Theater 1, Showtime: 12:00:00:, Movie: Superman 
    Total seats: 10, Reserved seats: 8 
 
    Unsuccessful Reservation 
 
>>> Print Theater information
    Theater #1, Showtime: 12:00:00:, Movie: Superman 
    Total seats: 10, Reserved seats: 8 
    Booker: 1,Ann,Smith, Transaction #: 1, #Seats: 3, Status: Reserved 
    Booker: 2,Beth,Thomas, Transaction #: 2, #Seats: 5, Status: Reserved 
 
>> Ann: coming_transactions 
    1,Ann,Smith 
    Transaction #1, Theater 1, Showtime: 12:00:00:, #Seats: 3, Payment: 450, Status: Paid 
 
>> Beth: coming_transactions
    2,Beth,Thomas 
    Transaction #2, Theater 1, Showtime: 12:00:00:, #Seats: 5, Payment: 750, Status: Paid 
 
>>> Cancel Ann's Reservation for Theater 1, showtime = 12:00 
    Theater #1, Showtime: 12:00:00:, Movie: Superman 
    Total seats: 10, Reserved seats: 5 
    Booker: 2,Beth,Thomas, Transaction #: 2, #Seats: 5, Status: Reserved 
 
>> Ann: coming_transactions 
    1,Ann,Smith 
 
>> Ann: history_transactions 
    1,Ann,Smith 
    Transaction #1, Theater 1, Showtime: 12:00:00:, #Seats: 3, Payment: 450, Status: Canceled 

>>> Clear reservations of Theater 1 after showtime is over. 
>>> Print Theater information 
    Theater #1, Showtime: 12:00:00:, Movie: Superman 
    Total seats: 10, Reserved seats: 0 
 
>> Ann: coming_transactions 
    1,Ann,Smith 
 
>> Ann: history_transactions 
    1,Ann,Smith 
    Transaction #1, Theater 1, Showtime: 12:00:00:, #Seats: 3, Payment: 450, Status: Canceled 
 
>> Beth: coming_transactions
    2,Beth,Thomas 
 
>> Beth: history_transactions
    2,Beth,Thomas 
    Transaction #2, Theater 1, Showtime: 12:00:00:, #Seats: 5, Payment: 750, Status: Paid
"""
"""
# def get_sum(event):
#     num1 = int(num1Entry.get())
#     num2 = int(num2Entry.get())
#     sum = num1 + num2

#     sumEntry.insert(0, sum)

# def get_data(event=None):
#     print("String : ", strVar.get())
#     print("Integer : ", intVar.get())
# Label(root, text= "First name").grid(row =0, sticky=W, padx=4)
# Entry(root).grid(row=0, column=1, sticky=E, pady=4)

# Label(root, text= "Last name").grid(row =1, sticky=W, padx=4)
# Entry(root).grid(row=1, column=1, sticky=E, pady=4)

# Button(root, text="Submit").grid(row =3)
# ###
# Label(root, text="Description").grid(row=0, column=0, sticky=W)
# Entry(root, width=50).grid(row=0, column = 1)
# Button(root, text="Submit").grid(row=0, column=8)

# Label(root, text="Quality").grid(row=1, column=0, stick=W)
# Radiobutton(root, text="New", value=1).grid(row=2, column=0, sticky=W)
# Radiobutton(root, text="Good", value=2).grid(row=3, column=0, sticky=W)
# Radiobutton(root, text="Used", value=3).grid(row=4, column=0, sticky=W)

# Label(root, text="Benefits").grid(row=1, column=1, sticky=W)
# Checkbutton(root, text="Free Shipping").grid(row=2, column=1 ,sticky=W)
# Checkbutton(root, text="Bonus Gift").grid(row=3, column=1 ,sticky=W)
# ######
# num1Entry = Entry(root)
# num1Entry.pack(side=LEFT)

# Label(root, text="+").pack(side=LEFT)

# num2Entry = Entry(root)
# num2Entry.pack(side=LEFT)

# equalButton = Button(root, text="=")
# equalButton.bind("<Button-1>", get_sum)
# equalButton.pack(side=LEFT)

# sumEntry = Entry(root)
# sumEntry.pack(side=LEFT)
# #####

# strVar = StringVar()
# intVar = IntVar()

# strVar.set("Enter string")
# intVar.set("Enter string")

# strEntry = Entry(root, textVariable=strVar)
# strEntry.pack(side=LEFT)

# intEntry = Entry(root, textVariable=intVar)
# intEntry.pack(side=LEFT)

# theCheckBut = Checkbutton(root, text="switch", variable=boolVar)
# theCheckBut.bind("<Button-1>", bind_button)
# theCheckBut.pack(side=LEFT)

# getDataButton = Button(root, text="Get Data")
# getDataButton.bind("<Button-1>", get_data)
# getDataButton.pack(side=LEFT)
"""