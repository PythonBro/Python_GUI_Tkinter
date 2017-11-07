# This program is written by Python3
# coding : UTF-8
# developer : Masazumi Katoh
# filename : GraphViewer_Ver.1.0.1.py
# last update : 2017/11/06
# version : 1.0.1

import tkinter as Tk

# initial setting
filepath = "../data/20170928_bme280.csv"

# create main frame
root = Tk.Tk()

root.title(u"Graph Viewer Ver.1.0.1")
root.geometry("800x600")

# label
static1 = Tk.Label(text = u"Label")
static1.pack()

button1 = Tk.Button(text = u"Button", width = 5)
button1.pack()

check1 = Tk.Checkbutton(text = u"check1")
check1.pack()

check2 = Tk.Checkbutton(text = u"check2")
check2.pack()

var = Tk.StringVar(root)
var.set("one") # initial value
box = Tk.OptionMenu(root, var, "one", "two", "three", "four")
box.pack()

radio1 = Tk.Radiobutton(text = u"radio1")
radio1.pack()
radio2 = Tk.Radiobutton(text = u"radio2")
radio2.pack()
radio3 = Tk.Radiobutton(text = u"radio3")
radio3.pack()

top1 = Tk.Toplevel()
top1.title(u"pop up")

msg = Tk.Message(top1, text = u"about_message")
msg.pack()

button2 = Tk.Button(top1, text = u"Dismiss", command=top1.destroy)
button2.pack()

list1 = Tk.Listbox()
list1.pack()

root.mainloop()
