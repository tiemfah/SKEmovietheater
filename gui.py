### GUI PACK ##
from tkinter import *
from tkinter import ttk
### CINEMA APP ###
from classes.customer import Customer
from classes.mytime import MyTime
from classes.reservation import Reservation
from classes.theater import Theater
from classes.transaction import Transaction


movie_list, command, m_command, b_command, r_command = [], '', '', '', ''

# cinema function
def show_movies(list):
    if len(list) > 0:
        temp = ''
        i = 1
        for movie in list:
            name, seat, available = movie.get_name_seat_available()
            temp += f"{i:<2}. {name:<10} {seat} seats / remaining {available} seats \n"
            i += 1
        return temp+ '\n'
    else:
        return 'No movies\n'
"""
"""
# movie gui function
def get_add_movie(Event):
    movie_list.append(Theater(movie_name.get(), 1, int(movie_seat_cap.get())))
    x = StringVar()
    #  update
    zxc = show_movies(movie_list)
    x.set(zxc)
    report = Label(tab3, textvariable= x)
    report.grid(row=1)

def get_delete_movie(Event):
    index_del = int(dentry.get())
    movie_list.pop(index_del-1)
    #  update
    x = StringVar()
    zxc = show_movies(movie_list)
    x.set(zxc)
    report = Label(tab3, textvariable= x)
    report.grid(row=1)
"""
"""
# booking gui function
def get_booking(Event):
    name, movie_index, num_seat = str(booker_name.get()), int(m_num.get()), int(nseat.get())
    #  create customer
    temp_cus = Customer(name, '')
    #  book him/her
    movie_list[movie_index-1].reserve(temp_cus, num_seat)

    mv_n_info = StringVar()
    mv_n_info.set(show_movie_info(Event))
    mv_n_report = Label(tab3, textvariable= mv_n_info)
    mv_n_report.grid(row=3)
"""
"""
# report gui function
def show_movie_info(Event):
    try:
        return movie_list[int(ent_r.get())-1].get_reserved_seating_info() + '\n'
    except:
        return "Choose one!"
def search_mv_info(Event):
    mv_n_info = StringVar()
    mv_n_info.set(show_movie_info(Event))
    mv_n_report = Label(tab3, textvariable= mv_n_info)
    mv_n_report.grid(row=3)
def delete_booking(Event):
    # movie_list[r_command].cancel(customer_x[0],movie_list[int(ent_r.get())-1].get_tt_id(), 1)
    movie_list[int(ent_r.get())-1].del_customer(int(r_sub_int.get())-1)
    # update
    mv_n_info = StringVar()
    temp_mv_n = show_movie_info(None)
    mv_n_info.set(temp_mv_n)
    mv_n_report = Label(tab3, textvariable= mv_n_info)
    mv_n_report.grid(row=3)
"""
"""
window = Tk()
window.title("SKE-Theater")

tab_control = ttk.Notebook(window)
 
tab1 = ttk.Frame(tab_control)
 
tab2 = ttk.Frame(tab_control)

tab3 = ttk.Frame(tab_control)
 
tab_control.add(tab1, text='Movie')
 
tab_control.add(tab2, text='Booking')

tab_control.add(tab3, text='Reports')
 
tab_control.pack(expand=1, fill='both')

#
#
### MOVIE TAB ###
#
#

#  NAME
mname = Label(tab1, text='Movie name')
movie_name = Entry(tab1)

mname.grid(column=0, row=1)
movie_name.grid(column=1, row=1)

#  SEAT
mseat = Label(tab1, text='Seat capacity')
movie_seat_cap = Entry(tab1)

mseat.grid(column=0, row=2)
movie_seat_cap.grid(column=1, row=2)

# submit button
m_submit = Button(tab1, text='Add')
m_submit.bind("<Button-1>", func=get_add_movie)
m_submit.grid(column=1, row=3)
# delete entry + button
dtext = Label(tab1, text="Delete movie (n)")
dtext.grid(column=0, row=4)
dentry = Entry(tab1)
dentry.grid(column=1, row=4)
m_del = Button(tab1, text='Delete')
m_del.bind("<Button-1>", func=get_delete_movie)
m_del.grid(column=1, row=5)

#
#
### BOOKING ###
#
#

# MOVIE SELECT
tb2lb1 = Label(tab2, text='Movie number')
tb2lb1.grid(column=0, row=0)

m_num = Entry(tab2)
m_num.grid(column=1, row=0)

#  BOOKER NAME
bname = Label(tab2, text='Booker name')
bname.grid(column=0, row=1)

booker_name = Entry(tab2)
booker_name.grid(column=1, row=1)

#  SEAT NUM
numseat = Label(tab2, text='Number of seat')
numseat.grid(column=0, row=2)

nseat = Entry(tab2)
nseat.grid(column=1, row=2)

b_submit = Button(tab2, text='Book')
b_submit.bind("<Button-1>", func=get_booking)
b_submit.grid(column=1, row=3)
#
#
### REPORT ###
#
#
# SHOW TAB INFO
tb3lb1 = Label(tab3, text="Movie Report")
tb3lb1.grid(column=0, row=0)

# all movie info
x = StringVar()
zxc = show_movies(movie_list)
x.set(zxc)
report = Label(tab3, textvariable= x)
report.grid(row=1)

#  movie n info
msg_r = Label(tab3, text="Choose movie to edit")
msg_r.grid(column=0, row= 2)

ent_r = Entry(tab3)
ent_r.grid(column=1, row=2)

but_r = Button(tab3, text="Search")
but_r.bind("<Button-1>", func=search_mv_info)
but_r.grid(column=2, row=2)

mv_n_info = StringVar()
mv_n_info.set(show_movie_info(Event))
mv_n_report = Label(tab3, textvariable= mv_n_info)
mv_n_report.grid(row=3)


# delete booking choice
r_sub_msg =Label(tab3, text='delete booking (n)')
r_sub_msg.grid(column=0, row=4)

r_sub_int = Entry(tab3)
r_sub_int.grid(column=1, row=4)

del_book_but = Button(tab3, text="Delete")
del_book_but.bind("<Button-1>", func=delete_booking)
del_book_but.grid(column=2, row=4)

window.mainloop()
