from tkinter import *
from tkinter import ttk
import tkinter as tk
import sqlite3


class SeeData(tk.Frame):
    def __init__(self, parent, controller, other=None):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        question = tk.Label(self, text="Would you like to view your expense"
                                       "records or trips?")
        b_trips = tk.Button(self, text="View Trip Records",
                            command=lambda: controller.show_frame("SeeTrips"))
        b_expenses = tk.Button(self, text="View Expense Records",
                               command=lambda: controller.show_frame("SeeExpenses"))

        question.grid(row=0, column=0)
        b_expenses.grid(row=1, column=0)
        b_trips.grid(row=1, column=1)


class SeeExpenses(tk.Frame):
    def __init__(self, parent, controller, other=None):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.file = 'expense_list.db'
        self.table = 'expenses'

        columns = ('Trip', 'Date', 'Category', 'Expense', 'Currency',
                   'Cost', 'Notes')
        self.tree = ttk.Treeview(self, columns=columns, show='headings')

        self.tree.heading('Trip', text="Trip")
        self.tree.heading('Date', text="Date")
        self.tree.heading('Category', text="Category")
        self.tree.heading('Expense', text="Expense")
        self.tree.heading('Currency', text="Currency")
        self.tree.heading('Cost', text="Cost")
        self.tree.heading('Notes', text="Notes")

        print_data(self.tree, self.file, self.table, columns)


class SeeTrips(tk.Frame):
    def __init__(self, parent, controller, other=None):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.file = 'trip_list.db'
        self.table = 'trips'

        columns = ('Name', 'Start', 'End', 'Categories', 'Type', 'Notes')

        self.tree = ttk.Treeview(self, columns=columns, show='headings')

        self.tree.heading('Name', text="Name")
        self.tree.heading('Start', text="Start Date")
        self.tree.heading('End', text="End Date")
        self.tree.heading('Categories', text="Categories")
        self.tree.heading('Type', text="Type")
        self.tree.heading('Notes', text="Notes")

        print_data(self.tree, self.file, self.table, columns)


def print_data(tree, file, table, columns):
    tree.pack()
    for heading in columns:
        tree.column(heading, width=int(500/len(columns)))
    con1 = sqlite3.connect(file)
    cur1 = con1.cursor()

    cur1.execute(f"SELECT * FROM {table}")

    rows = cur1.fetchall()

    for row in rows:
        print(row)
        tree.insert("", tk.END, values=row)
    con1.close()
