import paho.mqtt.client as mqtt
from time import sleep
import os
import cv2
from mtcnn import MTCNN

# Server="192.168.1.2"
Server = "broker.mqttdashboard.com"
Topic = "IoT/H1"


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



client = mqtt.Client()
# When on connect it will pass parameters to defined on_connect message
# When message recieved it will pass parameters to defined on_message message
client.on_connect = on_connect
client.on_message = on_message


client.connect(Server, 1883, 60)
client.loop_forever()
