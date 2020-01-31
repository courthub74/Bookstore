from tkinter import *
import backend

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))


app = Tk()
app.iconbitmap("icons/Bookstore.ico")
app.title("Bookstore")

#########################################
# LABELS
# TITLE
title = Label(app, text="Title")
title.grid(row=0, column=0)

# YEAR
year = Label(app, text="Year")
year.grid(row=1, column=0)

# AUTHOR
author = Label(app, text="Author")
author.grid(row=0, column=2)

# ISBN
isbn = Label(app, text="ISBN")
isbn.grid(row=1, column=2)

##########################################
# ENTRIES
# TITLE
title_text=StringVar()
title = Entry(app,textvariable=title_text)
title.grid(row=0,column=1)
# YEAR
year_text=StringVar()
year = Entry(app,textvariable=year_text)
year.grid(row=1,column=1)
# AUTHOR
author_text=StringVar()
author = Entry(app,textvariable=author_text)
author.grid(row=0,column=3)
# ISBN
isbn_text=StringVar()
isbn = Entry(app,textvariable=isbn_text)
isbn.grid(row=1,column=3)

###########################################################

# BUTTONS
# VIEW ALL BUTTON
viewall = Button(app, width=12, text="View all",command=view_command)
viewall.grid(row=2,column=3)

# SEARCH ENTRY BUTTON
search = Button(app, width=12, text="Search entry",command=search_command)
search.grid(row=3,column=3)

# ADD ENTRY BUTTON
add = Button(app, width=12, text="Add entry",command=add_command)
add.grid(row=4,column=3)

# UPDATE BUTTON
update = Button(app, width=12, text="Update selected")
update.grid(row=5,column=3)

# DELETE BUTTON
delete = Button(app, width=12, text="Delete selected")
delete.grid(row=6,column=3)

# CLOSE BUTTON
close = Button(app, width=12, text="Close")
close.grid(row=7,column=3)
###################################################

# LISTBOX
list1=Listbox(app, height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

# SCROLLBAR
sb1 = Scrollbar(app)
sb1.grid(row=2,column=2,rowspan=6)

# SCROLLBAR CONFIG
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)



app.mainloop()
