# IoT Dashboard

Two IoT clients one is used to send and the other to receive provided with GUI, coded in python using tkinter.

## Send

![send](Images/send.png)

### Default button 
Fills default values which are: -

| Entry | Default value |
| ----- | ------------- |
| Server| broker.mqttdashboard.com|
| Topic|Topic/IoT/1/|
| Message|Default messages|

![send2](Images/send2.png)

### Clear button
Reset values of Entries

### Close
Terminates the program

### Send 
sends the message

## Receive

![receive](Images/Receive1.png)

### Default button
Fills default values which are: -

| Entry | Default value |
| ----- | ------------- |
| Server| broker.mqttdashboard.com|
| Topic|Topic/IoT/1/|

![receive](Images/Receive2.png)

### Clear button
Reset values of Entries

### Close
Terminates the program

### Connect
Connects to broker

when connected a message appears
![receive3](Images/Receive3.png)

## Example
When a message received from any connected thing like "send.py" it appears in receive window.
![receive4](Images/Receive4.png)
