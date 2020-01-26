from tkinter import *

#create a tkinter window
root = Tk()

#open window having dimension 100x100
root.geometry = ('100x100')

#create a button
btn = Button(root, text = 'click me !', bd = '5', command = root.destroy)

#set the position of the button on the top of the window
btn.pack(side = 'top')
root.mainloop()