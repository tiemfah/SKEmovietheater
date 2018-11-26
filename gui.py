from tkinter import *
from tkinter import ttk

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
### MOVIE ###
#
#

#  NAME
mname = Label(tab1, text='Movie name')
mname.grid(column=0, row=0)

movie_name = Entry(tab1)
movie_name.grid(column=1, row=0)

#  SEAT
mseat = Label(tab1, text='Seat capacity')
mseat.grid(column=0, row=1)

movie_seat_cap = Entry(tab1)
movie_seat_cap.grid(column=1, row=1)

m_submit = Button(tab1, text='Add')
m_submit.grid(column=1, row=3)

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
b_submit.grid(column=1, row=3)


window.mainloop()
