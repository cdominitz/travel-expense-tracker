from tkinter import *

root = Tk()


logGoogle = Button(root, text="Log in with Google Account")
logFacebook = Button(root, text="Log in with Facebook")
logUsername = Button(root, text="Log in with Username")
createAccount = Button(root, text="or Create Account")

logGoogle.pack()
logFacebook.pack()
logUsername.pack()
createAccount.pack()

root.mainloop()
