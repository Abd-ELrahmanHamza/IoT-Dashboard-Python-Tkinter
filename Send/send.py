from tkinter.constants import END
from typing import Text
import paho.mqtt.publish as publish
import tkinter as tk
from tkinter.ttk import *
def Send():
    Server=en1.get()
    Topic=en2.get()
    message=en3.get()
    publish.single(Topic,message,hostname=Server)
def close():
    window.destroy()
def clear():
    en1.delete(0,"end")
    en2.delete(0,"end")
    en3.delete(0,"end")
def Default():
    clear()
    en1.insert(END,'192.168.1.2')
    en2.insert(END,"IoT/H1")
    en3.insert(END,"Default messages")

window = tk.Tk()
window.title("Publisher")
window.geometry("600x600")

img =tk.PhotoImage(file="PNG_transparency_demonstration_1.png")
img1 = img.subsample(5,5)
lbl4 = tk.Label(window,image=img1)
lbl4.grid(row=2,column=5,columnspan=2,rowspan=1)

lbl1 = tk.Label(window,text = "Server:")
lbl2 = tk.Label(window,text = "Topic:")
lbl3 = tk.Label(window,text = "Message:")

en1 = tk.Entry(window,text="Enter your server")
en2 = tk.Entry(window,text="Enter your Topic")
en3 = tk.Entry(window,text="Enter your Message")

sendbt = tk.Button(window,text = "send",command=Send)
closebt = tk.Button(window,text = "Close",command=close)
clearbt = tk.Button(window,text="clear",command=clear)
defaultbt = tk.Button(window,text="Default",command=Default)

lbl1.grid(row=2,column=2)
lbl2.grid(row=3,column=2)
lbl3.grid(row=4,column=2)
en1.grid(row=2,column=3)
en2.grid(row=3,column=3)
en3.grid(row=4,column=3)
sendbt.grid(row=5,column=4)
closebt.grid(row=5,column=5)
clearbt.grid(row=5,column=3)
defaultbt.grid(row=5,column=2)
window.mainloop()

Server = "192.168.1.2"
Topic = "IoT/H1"
h=60
#publish.single(Topic,"this is value from H1 =%d"%h,hostname=Server)
