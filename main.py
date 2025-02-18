from tkinter import *
from os import system
from tkinter import messagebox
import threading

root = Tk()
root.title("Vim Launcher")
root.resizable(False, False)

def about():
	sub_window = Toplevel()
	Label(sub_window, text = "Maintained and developed by therealzakie").grid()
	Label(sub_window, text = "Vim maintained developed by the Vim team").grid()

menu = Menu(root)
help_menu = Menu(menu, tearoff = 0)
help_menu.add_command(label = "About", command = about)
help_menu.add_command(label = "Quit", command = root.destroy)
menu.add_cascade(label = "Help", menu = help_menu)
root.config(menu=menu)

def run_vim():
	p = path.get()
	f = cmd.get()
	f.replace(" ", "")
	if f != "" and p != "":
		cmd.delete(0, END)
		path.delete(0, END)
		system(f'vim "{p}/{f}"')
	elif f != "" and p == "":
		cmd.delete(0, END)
		system(f"vim {f}")
	else:
		messagebox.showerror(title = "ERROR", message = "Please enter a file name with it's extension.")


Label(root, text = "Type the file you would to create/edit", font = ("TkDefaultFont", 20)).grid(row = 0, column = 0)
Label(root, text = "File name:").grid(row = 2, column = 0)
Label(root, text = "File directory (not including file name):").grid(row = 1, column = 0)
path = Entry(root)
path.grid(row = 1, column = 1)
cmd = Entry(root)
cmd.grid(row = 2, column = 1)
Button(root, text = "Run", command = run_vim).grid(row = 3)

root.mainloop()
