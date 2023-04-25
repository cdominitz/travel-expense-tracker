import tkinter as tk
import sqlite3


class AddExpense(tk.Frame):
    def __init__(self, parent, controller, other=None):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.myTripList = ["Select Trip"]

        # populate trip options
        conn2 = sqlite3.connect('trip_list.db')
        cur2 = conn2.cursor()
        cur2.execute("Select *, oid FROM trips")
        trips = cur2.fetchall()
        for trip in trips:
            self.myTripList.append(trip[0])
        # commit changes
        conn2.commit()
        # close connection
        conn2.close()

        self.selTrip = tk.StringVar()
        self.selTrip.set("Select Trip")
        trip = tk.Label(self, text="Select Trip:")
        self.myTrip = tk.OptionMenu(self, self.selTrip, *self.myTripList)
        b_trip = tk.Button(self, text="Select Trip", command=self.enterInfo)
        trip.grid(row=0, column=0)
        self.myTrip.grid(row=0, column=1)
        b_trip.grid(row=0, column=2)

    def enterInfo(self):
        if self.selTrip.get() == "Select Trip":
            err = tk.Tk()
            msg = tk.Label(err, text="Please select a trip")
            msg.grid(row=0, column=0, sticky='nsew')
            button = tk.Button(err, text="Okay", command=err.destroy)
            button.grid(row=1, column=0)
        else:
            self.controller.show_frame("EnterData", self.selTrip.get())
            self.selTrip.set("Select Trip")


class EnterData(tk.Frame):
    def __init__(self, parent, controller, other):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.myCategoryList = [0]
        self.selTrip = other
        conn2 = sqlite3.connect('trip_list.db')
        cur2 = conn2.cursor()
        cur2.execute("Select *, oid FROM trips")
        trips = cur2.fetchall()
        for trip in trips:
            if trip[0] == self.selTrip:
                self.myCategoryList = (trip[3].split(", "))
        conn2.commit()
        conn2.close()

        self.selCategory = tk.StringVar()
        self.selCategory.set("Select your category")

        # Text Boxes
        self.myTrip = tk.Label(self, text=self.selTrip)
        self.myDate = tk.Entry(self)
        self.myCategory = tk.OptionMenu(self, self.selCategory, *self.myCategoryList)
        self.myExpense = tk.Entry(self)
        self.myCurrency = tk.Entry(self)
        self.myCost = tk.Entry(self)
        self.myNotes = tk.Entry(self)

        # Labels and Buttons
        self.trip = tk.Label(self, text="Selected Trip: ")
        self.date = tk.Label(self, text="Date Purchased:")
        self.category = tk.Label(self, text="Category:")
        self.expense = tk.Label(self, text="Expense Name:")
        self.currency = tk.Label(self, text="Currency:")
        self.cost = tk.Label(self, text="Cost:")
        self.notes = tk.Label(self, text="Notes:")
        self.b_cancel = tk.Button(self, text="Cancel")
        self.b_submit = tk.Button(self, text="Submit", command=self.submit)

        # Text Grid
        self.myTrip.grid(row=0, column=1)
        self.myDate.grid(row=1, column=1)
        self.myCategory.grid(row=2, column=1)
        self.myExpense.grid(row=3, column=1)
        self.myCurrency.grid(row=4, column=1)
        self.myCost.grid(row=5, column=1)
        self.myNotes.grid(row=6, column=1)

        # Label Grid
        self.trip.grid(row=0, column=0)
        self.date.grid(row=1, column=0)
        self.category.grid(row=2, column=0)
        self.expense.grid(row=3, column=0)
        self.currency.grid(row=4, column=0)
        self.cost.grid(row=5, column=0)
        self.notes.grid(row=6, column=0)
        self.b_cancel.grid(row=7, column=0)
        self.b_submit.grid(row=7, column=1)


    def submit(self):
        '''
        conn = sqlite3.connect('expense_list.db')
        cur = conn.cursor()  # create cursor

        cur.execute("""CREATE TABLE IF NOT EXISTS expenses(
                trip,
                date,
                category,
                expense_name,
                currency,
                cost,
                notes
                )""")

        conn.commit()
        conn.close()
        '''
        conn = sqlite3.connect('expense_list.db')
        cur = conn.cursor()  # create cursor

        cur.execute("""INSERT INTO expenses VALUES (:myTrip, :myDate, :myCategory, 
                                                :myExpense, :myCurrency, :myCost, 
                                                :myNotes)""",
                    {
                        'myTrip': self.selTrip,
                        'myDate': self.myDate.get(),
                        'myCategory': self.selCategory.get(),
                        'myExpense': self.myExpense.get(),
                        'myCurrency': self.myCurrency.get(),
                        'myCost': self.myCost.get(),
                        'myNotes': self.myNotes.get()
                    })

        conn.commit()
        conn.close()

        save = tk.Tk()
        msg = tk.Label(save, text=f"Your {self.myExpense.get()} has been added!")
        msg.grid(row=0, column=0, sticky='nsew')
        button = tk.Button(save, text="Okay", command=save.destroy)
        button.grid(row=1, column=0)

        # Clear Text Boxes
        self.myDate.delete(0, tk.END)
        self.selCategory.set("Select your category")
        self.myExpense.delete(0, tk.END)
        self.myCurrency.delete(0, tk.END)
        self.myCost.delete(0, tk.END)
        self.myNotes.delete(0, tk.END)

