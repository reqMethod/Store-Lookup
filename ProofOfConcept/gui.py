import main
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("790x720")

frame1 = Frame(root)
frame1.place(x=40, y=10)
frame2 = Frame(root)
frame2.place(x=10, y=10)

treev = ttk.Treeview(frame1, height=25)
treev.pack()

verscrlbar = ttk.Scrollbar(frame2, orient="vertical", command=treev.yview) # Creates a vertical scroll bar yview creates a vertical view
verscrlbar.pack()

# rowid storenum address number <- Headers
treev["columns"] = ("1", "2", "3", "4") # Defining number of columns
# Defining Headings
treev['show'] = 'headings'
# Assigning the width and anchor to the respective columns
treev.column("1", width=100, anchor='c')
treev.column("2", width=100, anchor='c')
treev.column("1", width=200, anchor='c')
treev.column("1", width=200, anchor='c')

# Assigning Names to the columns
treev.heading("1", text="ROW ID")
treev.heading("2", text="Store#")
treev.heading("3", text="Address")
treev.heading("4", text="Phone Number")

# Creating Functions
def add_one(storenum, address, number):
    global treev
    main.add_one(storenum, address, number)
    show()

def update(id, storenum, address,number):
    main.update(id, storenum, address, number)
    show()

def delete(id):
    main.delete(id)
    show()

id_label = Label(root, text="ROW ID: ")
id_label.place(x=10, y=550)
id_entry = Entry(root, width=10)
id_entry.place(x=70, y=550)

storenum_label = Label(root, text="STORE#: ")
storenum_label.place(x=140, y=550)
storenum_entry = Entry(root, width=10)
storenum_entry.place(x=218, y=550)

address_label = Label(root, text="ADDRESS: ")
address_label.place(x=340, y=550)
address_entry = Entry(root)
address_entry.place(x=410, y=550)

number_label = Label(root, text="Phone#: ")
number_label.place(x=540, y=550)
number_entry = Entry(root)
number_entry.place(x=580, y=550)

# Creating Buttons
createButton = Button(text="CREATE", bg="lightgreen", command=lambda:add_one(storenum_entry.get(), address_entry.get(), number_entry.get()))
createButton.place(x=720, y=550)

updateButton = Button(text="UPDATE", bg="orange", command=lambda:update(id_entry.get(), storenum_entry.get(), address_entry.get(), number_entry.get()))
updateButton.place(x=720, y=585)

deleteButton = Button(text="DELETE", bg="red", command=lambda:delete(id_entry.get()))
deleteButton.place(x=720, y=625)

def show():
    global treev
    treev.delete(*treev.get_children())
    for i in main.show():
        treev.insert("" , 'end', values = (i[0], i[1], i[2], i[3]))

show()
root.mainloop()