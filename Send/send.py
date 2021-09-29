from tkinter.constants import END
from typing import Text
import paho.mqtt.publish as publish
import tkinter as tk
import tkinter.font as font
from tkinter.ttk import *


def Send():
    Server = en1.get()
    Topic = en2.get()
    message = en3.get()
    publish.single(Topic, message, hostname=Server)


def close():
    window.destroy()


def clear():
    en1.delete(0, "end")
    en2.delete(0, "end")
    en3.delete(0, "end")


def Default():
    clear()
    en1.insert(END, 'broker.mqttdashboard.com')
    en2.insert(END, "Topic")
    en3.insert(END, "Default messages")


window = tk.Tk()
window.title("Publisher")
window.geometry("500x300")


title = tk.Label(window, text="Send", fg="red",
                 font=("Helvetica", 20, "bold"), width=30)
title.grid(row=0, column=0, columnspan=20, rowspan=2)

labelsWidth = 10
labelsHeight = 2

labelsFont = font.Font(family='Helvetica', size=10, weight='bold')
lbl1 = tk.Label(window, text="Server:", 
                width=labelsWidth, height=labelsHeight)
lbl2 = tk.Label(window, text="Topic:", 
                width=labelsWidth, height=labelsHeight)
lbl3 = tk.Label(window, text="Message:",
                width=labelsWidth, height=labelsHeight)
lbl1['font'] = lbl2['font'] = lbl3['font'] = labelsFont

entityWidth = 30

en1 = tk.Entry(window, text="Enter your server",width = entityWidth)
en2 = tk.Entry(window, text="Enter your Topic",width = entityWidth)
en3 = tk.Entry(window, text="Enter your Message", width=entityWidth)

buttonsWidth = 10
buttonsHeight = 2
buttonsColSpan = 3

bottonsFont = font.Font(family='Helvetica', size=10, weight='bold')
sendbt = tk.Button(window, text="send", command=Send,
                   bg="#33FF98", height=buttonsHeight, width=buttonsWidth)
closebt = tk.Button(window, text="Close", command=close,
                    bg="#FF5733", height=buttonsHeight, width=buttonsWidth)
clearbt = tk.Button(window, text="clear", command=clear,
                    bg="#33A7FF", height=buttonsHeight, width=buttonsWidth)
defaultbt = tk.Button(window, text="Default", command=Default,
                      bg="#FFC733", height=buttonsHeight, width=buttonsWidth)
sendbt['font'] = closebt['font'] = clearbt['font'] = defaultbt['font'] = bottonsFont

rowSpan = 2
columnSpan = 3
lbl1.grid(row=2, column=1,columnspan=columnSpan ,rowspan = rowSpan)
lbl2.grid(row=rowSpan+3, column=1, columnspan=columnSpan, rowspan=rowSpan)
lbl3.grid(row=rowSpan+5, column=1, columnspan=columnSpan, rowspan=rowSpan)

en1.grid(row=2, column=2+columnSpan, columnspan=columnSpan+3, rowspan=rowSpan)
en2.grid(row=rowSpan+3, column=2+columnSpan, columnspan=columnSpan+3, rowspan=rowSpan)
en3.grid(row=rowSpan+5, column=2+columnSpan, columnspan=columnSpan+3, rowspan=rowSpan)

sendbt.grid(row=rowSpan+8, column=1,columnspan=columnSpan, rowspan=rowSpan+2)
closebt.grid(row=rowSpan+8, column=5,columnspan=columnSpan, rowspan=rowSpan+2)
clearbt.grid(row=rowSpan+8, column=9,columnspan=columnSpan, rowspan=rowSpan+2)
defaultbt.grid(row=rowSpan+8, column=13, columnspan=columnSpan, rowspan=rowSpan+2)

window.mainloop()
