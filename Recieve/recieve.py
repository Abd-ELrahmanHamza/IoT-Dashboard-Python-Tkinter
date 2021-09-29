import paho.mqtt.client as mqtt
from time import sleep
import os
import cv2
from mtcnn import MTCNN
from tkinter.constants import END
from typing import Text
import paho.mqtt.publish as publish
import tkinter as tk
import tkinter.font as font
from tkinter.ttk import *

Topic =""
Server =""
client = mqtt.Client()

# what happens when connect
def on_connect(client, userdata, flags, rc):
    '''
    parameters
        client : object
        flags  : connected or not
        rc     : connection status
    '''
    print("Connected with result code: " + str(rc))
    client.subscribe(Topic)


# what happens on recieving a message
def on_message(client, userdata, msg):
    '''
    parameters
        client : object
        msg    : message recived (object)
    '''
    print(msg.topic + " ==> " + str(msg.payload))
    if "Camera" in str(msg.payload):
        print("open camera")
        cascPath = os.path.dirname(
            cv2.__file__) + "/data/haarcascade_frontalface_alt2.xml"
        faceCascade = cv2.CascadeClassifier(cascPath)
        video_capture = cv2.VideoCapture(0)
        while True:
            # Capture frame-by-frame
            ret, frame = video_capture.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray,
                                                scaleFactor=1.1,
                                                minNeighbors=5,
                                                minSize=(60, 60),
                                                flags=cv2.CASCADE_SCALE_IMAGE)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                # Display the resulting frame
            cv2.imshow('Video', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        video_capture.release()
        cv2.destroyAllWindows()
        video_capture.release()
        cv2.destroyAllWindows()
        # cap = cv2.VideoCapture(0)

        # while(True):
        #     # Capture frame-by-frame
        #     ret, frame = cap.read()

        #     # Our operations on the frame come here
        #     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #     # Display the resulting frame
        #     cv2.imshow('frame', gray)
        #     if cv2.waitKey(1) & 0xFF == ord('q'):
        #         break





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


def Default():
    clear()
    en1.insert(END, 'broker.mqttdashboard.com')
    en2.insert(END, "Topic/IoT/1/")


window = tk.Tk()
window.title("Publisher")
window.geometry("500x300")


title = tk.Label(window, text="Recieve", fg="red",
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
connectbt['font'] = closebt['font'] = clearbt['font'] = defaultbt['font'] = bottonsFont

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


window.mainloop()


