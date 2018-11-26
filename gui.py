from tkinter import *
from tkinter import ttk


# def get_sum(event):
#     num1 = int(num1Entry.get())
#     num2 = int(num2Entry.get())
#     sum = num1 + num2

#     sumEntry.insert(0, sum)

def get_data(event=None):
    print("String : ", strVar.get())
    print("Integer : ", intVar.get())

root = Tk()

# Label(root, text= "First name").grid(row =0, sticky=W, padx=4)
# Entry(root).grid(row=0, column=1, sticky=E, pady=4)

# Label(root, text= "Last name").grid(row =1, sticky=W, padx=4)
# Entry(root).grid(row=1, column=1, sticky=E, pady=4)

# Button(root, text="Submit").grid(row =3)
####
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
#######
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
######

strVar = StringVar()
intVar = IntVar()

strVar.set("Enter string")
intVar.set("Enter string")

strEntry = Entry(root, textVariable=strVar)
strEntry.pack(side=LEFT)

intEntry = Entry(root, textVariable=intVar)
intEntry.pack(side=LEFT)

theCheckBut = Checkbutton(root, text="switch", variable=boolVar)
theCheckBut.bind("<Button-1>", bind_button)
theCheckBut.pack(side=LEFT)

getDataButton = Button(root, text="Get Data")
getDataButton.bind("<Button-1>", get_data)
getDataButton.pack(side=LEFT)

root.mainloop()
