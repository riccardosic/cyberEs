from tkinter import *
from functools import partial
from server import threaded_client

def validateLogin(cellnumber):
	print("cell number entered :", cellnumber.get())
    # threaded_client()
	# print("password entered :", password.get())
	return

#window
tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('LOGIN')

#cellnumbe label and text entry box
cellnumberLabel = Label(tkWindow, text="Phone number").grid(row=0, column=0)
cellnumber = StringVar()
cellnumberEntry = Entry(tkWindow, textvariable=cellnumber).grid(row=0, column=1)  

# #password label and password entry box
# passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
# password = StringVar()
# passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  

validateLogin = partial(validateLogin, cellnumber)

#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)  

tkWindow.mainloop()