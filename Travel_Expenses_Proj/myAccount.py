import tkinter as tk

class Account(tk.Frame):
    def __init__(self, parent, controller, other=None):
        tk.Frame.__init__(self, parent)
        self.controller = controller

 #   def __init__(self, first, last, email, password):
    #    self._first = first
     #   self._last = last
      #  self._email = email
       # self._password = password
        self._contacts = {}
        self._events = {}
        self._bio = None
        self._pic = None

    def add_contact(self, new_contact):
        self._contacts[new_contact.get_name()] = new_contact

    def add_event(self, new_event):
        self._events[new_event.get_event_name()] = new_event

    def update_bio(self, new_bio):
        self._bio = new_bio

    def update_pic(self, new_pic):
        self._pic = new_pic

class Contact:
    def __init__(self, name, email, phone):
        self._name = name
        self._email = email
        self._phone = phone

    def get_name(self):
        return self._name

    def get_email(self):
        return self._email

    def get_phone(self):
        return self._phone
