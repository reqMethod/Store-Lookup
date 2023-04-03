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


def showSpecific(storenum):
    main.showSpecific(storenum)
    show()


search_label = Label(root, text="Search by Store#:")
search_label.place(x=40, y=600)
search_entry = Entry(root, width=10)
search_entry.place(x=150, y=600)

# Creating Buttons

searchButton = Button(text="SEARCH", bg="dark blue", command=lambda:showSpecific(search_entry.get()))
searchButton.place(x=260, y=600)

def show():
    global treev
    treev.delete(*treev.get_children())
    for i in main.showSpecific(search_entry.get()):
        treev.insert("" , 'end', values = (i[0], i[1], i[2], i[3], i[4], i[5], i[6]))

show()
root.mainloop()