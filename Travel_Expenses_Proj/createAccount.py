from tkinter import *
import sqlite3

f_createAccount = Tk()
# Create/Connect to database
conn = sqlite3.connect('user_accounts.db')

cur = conn.cursor()     # create cursor
# Create Table
'''
cur.execute("CREATE TABLE accounts(first_name, last_name, email, password)")
'''

def submit():
    conn = sqlite3.connect('user_accounts.db')
    cur = conn.cursor()  # create cursor
    cur.execute("""INSERT INTO accounts VALUES (:myFirstName, :myLastName,
                                            :myEmail, :myPassword)""",
                {
                    'myFirstName': myFirstName.get(),
                    'myLastName': myLastName.get(),
                    'myEmail': myEmail.get(),
                    'myPassword': myPassword.get()
                })
    conn.commit()
    conn.close()

    myFirstName.delete(0, END)
    myLastName.delete(0, END)
    myEmail.delete(0, END)
    myPassword.delete(0, END)
    myRePassword.delete(0, END)


# def createAccount():
# initialize all variables
firstName = Label(f_createAccount, text="First Name:")
myFirstName = Entry(f_createAccount)
lastName = Label(f_createAccount, text="Last Name:")
myLastName = Entry(f_createAccount)
email = Label(f_createAccount, text="Email Address:")
myEmail = Entry(f_createAccount)
password = Label(f_createAccount, text="Password:")
myPassword = Entry(f_createAccount)
rePassword = Label(f_createAccount, text="Re-enter Password")
myRePassword = Entry(f_createAccount)
submit = Button(f_createAccount, text="Submit", command=submit)

# upload to grid
firstName.grid(row=0, column=0)
myFirstName.grid(row=0, column=1)
lastName.grid(row=1, column=0)
myLastName.grid(row=1, column=1)
email.grid(row=2, column=0)
myEmail.grid(row=2, column=1)
password.grid(row=3, column=0)
myPassword.grid(row=3, column=1)
rePassword.grid(row=4, column=0)
myRePassword.grid(row=4, column=1)
submit.grid(row=5, column=1)

# commit changes
conn.commit()
# close connection
conn.close()
f_createAccount.mainloop()
