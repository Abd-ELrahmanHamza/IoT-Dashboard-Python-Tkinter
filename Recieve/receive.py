import paho.mqtt.client as mqtt
from time import sleep
import os
import cv2
from tkinter.constants import END
import paho.mqtt.publish as publish
import tkinter as tk
import tkinter.font as font
from tkinter.ttk import *
import plot
Topic =""
Server =""
client = mqtt.Client()
Temp_list = []
# what happens when connect
def on_connect(client, userdata, flags, rc):
    '''
    parameters
        client : object
        flags  : connected or not
        rc     : connection status
    '''
    client.subscribe(Topic)
    connectionInfoArea['text'] = "Server: "+Server+"\t"+"Topic: " + \
        Topic+"\n"+"Connected with result code: " + str(rc)+"\n"


# what happens on recieving a message
def on_message(client, userdata, msg):
    '''
    parameters
        client : object
        msg    : message recived (object)
    '''
    messagesArea['text'] += msg.topic + " ==> " + str(msg.payload)[2:-1]+"\n"
    try:
        Temp_list.append(float(str(msg.payload)[2:-1]))
    except:
        pass


def Connect():
    global Server
    global Topic
    global client
    Server = en1.get()
    Topic = en2.get()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(Server, 1883, 60)
    client.loop_start()




def close():
    window.destroy()


def clear():
    en1.delete(0, "end")
    en2.delete(0, "end")
    messagesArea['text'] = " "
    Temp_list = []


def Default():
    clear()
    en1.insert(END, 'broker.mqttdashboard.com')
    en2.insert(END, "Topic/IoT/1/")
    messagesArea['text'] = " "

def plotdata():
    plot.plotData(Temp_list)

window = tk.Tk()
window.title("Publisher")
window.geometry("600x300")


title = tk.Label(window, text="Receive", fg="red",
                 font=("Helvetica", 20, "bold"), width=30)
title.grid(row=0, column=0, columnspan=20, rowspan=2)

labelsWidth = 10
labelsHeight = 2

labelsFont = font.Font(family='Helvetica', size=10, weight='bold')
lbl1 = tk.Label(window, text="Server:",
                width=labelsWidth, height=labelsHeight)
lbl2 = tk.Label(window, text="Topic:",
                width=labelsWidth, height=labelsHeight)

lbl1['font'] = lbl2['font']  = labelsFont

entityWidth = 30

en1 = tk.Entry(window, text="Enter your server", width=entityWidth)
en2 = tk.Entry(window, text="Enter your Topic", width=entityWidth)

buttonsWidth = 10
buttonsHeight = 2
buttonsColSpan = 3

bottonsFont = font.Font(family='Helvetica', size=10, weight='bold')
connectbt = tk.Button(window, text="Connect", command=Connect,
                   bg="#33FF98", height=buttonsHeight, width=buttonsWidth)
closebt = tk.Button(window, text="Close", command=close,
                    bg="#FF5733", height=buttonsHeight, width=buttonsWidth)
clearbt = tk.Button(window, text="clear", command=clear,
                    bg="#33A7FF", height=buttonsHeight, width=buttonsWidth)
defaultbt = tk.Button(window, text="Default", command=Default,
                      bg="#FFC733", height=buttonsHeight, width=buttonsWidth)
plotbt = tk.Button(window, text="Plot", command=plotdata,
                      bg="#4caf50", height=buttonsHeight, width=buttonsWidth)
connectbt['font'] = closebt['font'] = clearbt['font'] = defaultbt['font'] = bottonsFont

messagesArea = tk.Label(window, height=10, width=30)
connectionInfoArea = tk.Label(window, fg="red",
                              font=("Helvetica", 10, "bold"),)

rowSpan = 2
columnSpan = 3
lbl1.grid(row=2, column=1, columnspan=columnSpan, rowspan=rowSpan)
lbl2.grid(row=rowSpan+3, column=1, columnspan=columnSpan, rowspan=rowSpan)

en1.grid(row=2, column=2+columnSpan, columnspan=columnSpan+3, rowspan=rowSpan)
en2.grid(row=rowSpan+3, column=2+columnSpan,
         columnspan=columnSpan+3, rowspan=rowSpan)


connectbt.grid(row=rowSpan+8, column=1, columnspan=columnSpan, rowspan=rowSpan+2)
closebt.grid(row=rowSpan+8, column=5, columnspan=columnSpan, rowspan=rowSpan+2)
clearbt.grid(row=rowSpan+8, column=9, columnspan=columnSpan, rowspan=rowSpan+2)
defaultbt.grid(row=rowSpan+8, column=13,
               columnspan=columnSpan, rowspan=rowSpan+2)
plotbt.grid(row=rowSpan+8, column=17,
            columnspan=columnSpan, rowspan=rowSpan+2)
connectionInfoArea.grid(row=15, column=0, columnspan=20, rowspan=1)
messagesArea.grid(row=17,column=0,columnspan=20,rowspan = 20)
window.mainloop()


