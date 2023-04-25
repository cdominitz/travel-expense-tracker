import tkinter as tk
from homePage import *
from createTrip import *
from addExpense import *
from seeAllData import *
from myAccount import *


class MyMainPanel(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.maxsize(700, 550)
        self.configure(bg="#EBDFD6")

        # Top frame Layout
        topFrame = tk.Frame(self, width=700, height=50, bg="#565962")
        topFrame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
        topFrame.columnconfigure(index=0, weight=1)
        topFrame.columnconfigure(index=1, weight=3)
        topFrame.columnconfigure(index=2, weight=1)

        #Top Frame Info
        self.back = tk.Button(topFrame, text="back", bg="blue")
        self.title = tk.Label(topFrame, text="Page Title", bg="white", fg="black")
        self.settings = tk.Button(topFrame, text="settings")

        self.back.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
        self.title.grid(row=0, column=1, sticky='nsew', padx=10, pady=10)
        self.settings.grid(row=0, column=2, sticky='nsew', padx=10, pady=10)

        mainFrame = tk.Frame(self, width=700, height=500)
        mainFrame.grid(row=1, column=0, padx=10, pady=10)
        # Container for mainframe
        self.container = tk.Frame(mainFrame, width=500, height=500, bg="orange")
        self.container.grid(row=1, column=1, sticky='nsew')

        # collection of mainframes
        self.frames = {}
        for F in (MyHomePage, CreateTrip, AddExpense, EnterData, SeeExpenses,
                  AddData, SeeTrips, SeeData, Account):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self, other=None)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MyHomePage")

        # Bottom Frame Layout
        leftFrame = tk.Frame(mainFrame, width=100, height=50, bg="white")
        leftFrame.grid(row=1, column=0, padx=2, pady=2, sticky='nsew')

        # Bottom Frame Buttons
        self.home = tk.Button(leftFrame, text="Home",
                              command=lambda: self.show_frame(
                                  "MyHomePage"))
        self.add = tk.Button(leftFrame, text="Add Data",
                             command=lambda: self.show_frame(
                                 "AddData"))
        self.data = tk.Button(leftFrame, text="View Data",
                              command=lambda: self.show_frame("SeeData"))
        self.account = tk.Button(leftFrame, text="Account",
                                 command=lambda: self.show_frame("Account"))

        self.home.grid(row=0, column=0, sticky="nsew")
        self.add.grid(row=1, column=0, sticky="nsew")
        self.data.grid(row=2, column=0, sticky="nsew")
        self.account.grid(row=3, column=0, sticky="nsew")

    def show_frame(self, page_name, other=None):
        if page_name == "EnterData":
            frame = EnterData(parent=self.container, controller=self, other=other)
            frame.grid(row=0, column=0, sticky="nsew")
        else:
            frame = self.frames[page_name]

        frame.tkraise()
        frame.configure(bg="#D0D4DA")


if __name__ == "__main__":
    app = MyMainPanel()
    app.mainloop()
