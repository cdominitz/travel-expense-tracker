import tkinter as tk
# from myMainPanel import MyMainPanel


class MyHomePage(tk.Frame):
    def __init__(self, parent, controller, other=None):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=1)
        self.rowconfigure(index=0, weight=1)
        self.rowconfigure(index=1, weight=1)

        self.newExpense = tk.Button(self, text="Add a new Expense",
                                    command=lambda: controller.show_frame("AddExpense"))
        self.newTrip = tk.Button(self, text="Add a new trip",
                                 command=lambda: controller.show_frame("CreateTrip"))
        self.seeExpenses = tk.Button(self, text="See my expenses",
                                     command=lambda: controller.show_frame("SeeExpenses"))
        self.seeTrips = tk.Button(self, text="See my trips",
                                  command=lambda: controller.show_frame("SeeTrips"))

        self.newExpense.grid(row=0, column=0, sticky='nsew')
        self.newTrip.grid(row=0, column=1, sticky='nsew')
        self.seeExpenses.grid(row=1, column=0, sticky='nsew')
        self.seeTrips.grid(row=1, column=1, sticky='nsew')
