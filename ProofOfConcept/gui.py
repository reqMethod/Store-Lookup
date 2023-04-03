import main
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("1920x1080")

frame1 = Frame(root)
frame1.place(x=40, y=10)
frame2 = Frame(root)
frame2.place(x=10, y=10)

treev = ttk.Treeview(frame1, height=25)
treev.pack()

verscrlbar = ttk.Scrollbar(frame2, orient="vertical", command=treev.yview) # Creates a vertical scroll bar yview creates a vertical view
verscrlbar.pack()

# rowid storenum name number <- Headers
treev["columns"] = ("1", "2", "3", "4", "5", "6", "7") # Defining number of columns
# Defining Headings
treev['show'] = 'headings'
# Assigning the width and anchor to the respective columns
treev.column("1", width=100, anchor='c')
treev.column("2", width=100, anchor='c')
treev.column("3", width=200, anchor='c')
treev.column("4", width=200, anchor='c')
treev.column("5", width=200, anchor='c')
treev.column("6", width=300, anchor='c')
treev.column("7", width=50, anchor='c')

# Assigning Names to the columns
treev.heading("1", text="ROW ID")
treev.heading("2", text="Store#")
treev.heading("3", text="Name")
treev.heading("4", text="Phone Number")
treev.heading("5", text="Email")
treev.heading("6", text="Address")
treev.heading("7", text="Trial")

# Creating Functions
def add_one(storenum, name, number, email, address, trial):
    main.add_one(storenum, name, number, email, address, trial)
    show()

def update(id, storenum, name, number, email, address, trial):
    main.update(id, storenum, name, number, email, address, trial)
    show()

def delete(id):
    main.delete(id)
    show()

id_label = Label(root, text="ROW ID: ")
id_label.place(x=10, y=550)
id_entry = Entry(root, width=10)
id_entry.place(x=70, y=550)

storenum_label = Label(root, text="STORE#: ")
storenum_label.place(x=175, y=550)
storenum_entry = Entry(root, width=10)
storenum_entry.place(x=240, y=550)

name_label = Label(root, text="Name: ")
name_label.place(x=10, y=600)
name_entry = Entry(root, width=30)
name_entry.place(x=70, y=600)

number_label = Label(root, text="Phone#: ")
number_label.place(x=10, y=650)
number_entry = Entry(root, width=30)
number_entry.place(x=70, y=650)

email_label = Label(root, text="Email: ")
email_label.place(x=360, y=650)
email_entry = Entry(root, width=20)
email_entry.place(x=410, y=650)

address_label = Label(root, text="Address: ")
address_label.place(x=10, y=700)
address_entry = Entry(root, width=50)
address_entry.place(x=70, y=700)

trial_label = Label(root, text="Trial: ")
trial_label.place(x=360, y=600)
trial_entry = Entry(root, width=10)
trial_entry.place(x=400, y=600)


# Creating Buttons
createButton = Button(text="CREATE", bg="lightgreen", command=lambda:add_one(storenum_entry.get(), name_entry.get(), number_entry.get(), email_entry.get(), address_entry.get(), trial_entry.get()))
createButton.place(x=650, y=550)

updateButton = Button(text="UPDATE", bg="orange", command=lambda:update(id_entry.get(), storenum_entry.get(), name_entry.get(), number_entry.get(), email_entry.get(), address_entry.get(), trial_entry.get()))
updateButton.place(x=650, y=585)

deleteButton = Button(text="DELETE", bg="red", command=lambda:delete(id_entry.get()))
deleteButton.place(x=650, y=625)



def show():
    global treev
    treev.delete(*treev.get_children())
    for i in main.show():
        treev.insert("" , 'end', values = (i[0], i[1], i[2], i[3], i[4], i[5], i[6]))

show()
root.mainloop()