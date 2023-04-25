import tkinter as tk
import sqlite3
# Need to add back in create table if not there
# need to add in confirmation message about submitting it and saying it was
#   successful


class AddData(tk.Frame):
    def __init__(self, parent, controller, other=None):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        question = tk.Label(self, text="Would you like to add a new trip or new expense?")
        b_trip = tk.Button(self, text="Add new trip",
                           command=lambda: controller.show_frame("CreateTrip"))
        b_expense = tk.Button(self, text="Add new Expense",
                              command=lambda: controller.show_frame("AddExpense"))

        question.grid(row=0, column=0)
        b_expense.grid(row=1, column=0)
        b_trip.grid(row=1, column=1)


class CreateTrip(tk.Frame):
    def __init__(self, parent, controller, other=None):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.myTrip = tk.Entry(self)
        self.myStartDate = tk.Entry(self)
        self.myEndDate = tk.Entry(self)
        self.myCategories = tk.Entry(self)
        self.myTripType = tk.Entry(self)
        self.myNotes = tk.Entry(self)

        # Labels and Buttons
        self.trip = tk.Label(self, text="Trip Name:")
        self.startDate = tk.Label(self, text="Start Date:")
        self.endDate = tk.Label(self, text="End Date:")
        self.categories = tk.Label(self, text="Categories:")
        self.tripType = tk.Label(self, text="Trip Type:")
        self.notes = tk.Label(self, text="Notes:")
        self.b_cancel = tk.Button(self, text="Cancel")
        self.b_submit = tk.Button(self, text="Submit", command=self.submit)

        # Text Grid
        self.myTrip.grid(row=0, column=1)
        self.myStartDate.grid(row=1, column=1)
        self.myEndDate.grid(row=2, column=1)
        self.myCategories.grid(row=3, column=1)
        self.myTripType.grid(row=4, column=1)
        self.myNotes.grid(row=5, column=1)

        # Label Grid
        self.trip.grid(row=0, column=0)
        self.startDate.grid(row=1, column=0)
        self.endDate.grid(row=2, column=0)
        self.categories.grid(row=3, column=0)
        self.tripType.grid(row=4, column=0)
        self.notes.grid(row=5, column=0)
        self.b_cancel.grid(row=6, column=0)
        self.b_submit.grid(row=6, column=1)

    def submit(self):
        '''
        conn = sqlite3.connect('trip_list.db')
        cur = conn.cursor()  # create cursor
        cur.execute("""CREATE TABLE IF NOT EXISTS trips (
                        'myTrip',
                        'myStartDate',
                        'myEndDate',
                        'myCategories',
                        'myTripType',
                        'myNotes'
                    )""")

        conn.commit()
        conn.close()
        '''

        conn = sqlite3.connect('trip_list.db')
        cur = conn.cursor()  # create cursor
        cur.execute("""INSERT INTO trips VALUES (:myTrip, :myStartDate, :myEndDate,
                                                :myCategories, :myTripType, 
                                                :myNotes)""",
                    {
                        'myTrip': self.myTrip.get(),
                        'myStartDate': self.myStartDate.get(),
                        'myEndDate': self.myEndDate.get(),
                        'myCategories': self.myCategories.get(),
                        'myTripType': self.myTripType.get(),
                        'myNotes': self.myNotes.get()
                    })

        conn.commit()
        conn.close()

        save = tk.Tk()
        msg = tk.Label(save, text=f"Your {self.myTrip.get()} has been added!")
        msg.grid(row=0, column=0, sticky='nsew')
        button = tk.Button(save, text="Okay", command=save.destroy)
        button.grid(row=1, column=0)

        # Clear Text Boxes
        self.myTrip.delete(0, tk.END)
        self.myStartDate.delete(0, tk.END)
        self.myEndDate.delete(0, tk.END)
        self.myCategories.delete(0, tk.END)
        self.myTripType.delete(0, tk.END)
        self.myNotes.delete(0, tk.END)

