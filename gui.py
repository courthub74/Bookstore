"""
A program that stores this book information:
Title, Author
Year, ISBN

User can:
View all records
Search an entry
Add entry
Update entry
Delete
Close
"""

from tkinter import *

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

# LISTBOX
'''biglist = Listbox(app, width=40, height=10)
biglist.grid(row=2, column=0,pady=20)'''

# VIEW ALL BUTTON
viewall = Button(app, width=20, text="View all", font="arial 10")
viewall.grid(row=2,column=3)

# SEARCH ENTRY BUTTON
search = Button(app, width=20, text="Search entry", font="arial 10")
search.grid(row=3,column=3)

# ADD ENTRY BUTTON
add = Button(app, width=20, text="Add entry", font="arial 10")
add.grid(row=4,column=3)

# UPDATE BUTTON
update = Button(app, width=20, text="Update", font="arial 10")
update.grid(row=5,column=3)

# DELETE BUTTON
delete = Button(app, width=20, text="Delete", font="arial 10")
delete.grid(row=6,column=3)

# CLOSE BUTTON
close = Button(app, width=20, text="Close", font="arial 10")
close.grid(row=7,column=3)

app.mainloop()
