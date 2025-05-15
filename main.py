from tkinter import *

root = Tk()

root.title("Go Link UTM Creator")
root.geometry('500x300')

lbl = Label(root, text = "Business Unit:")
lbl.grid()

txt = Entry(root, width=10)
txt.grid(column=1, row=0)

menu = Menu(root)
item = Menu(menu)
item.add_command(label="New")
menu.add_cascade(label="File", menu=item)
root.config(menu=menu)

def clicked():

    res = "You wrote: " + txt.get()
    lbl.configure(text = res)

btn = Button(root, text = "Click Me",
             fg = "red", command=clicked)

btn.grid(column=2, row=0)

root.mainloop()
