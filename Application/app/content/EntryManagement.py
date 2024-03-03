import os
import cv2
from flask import Flask
import datetime
import requests

AREA_MANAGER_SERVICE_HOST = "localhost"
AREA_MANAGER_SERVICE_PORT = "50051"

USER_VALIDATION_SERVICE_HOST = "localhost"
USER_VALIDATION_SERVICE_PORT = "50053"


app = Flask(__name__)

def check_in(areaID):#areaID, crownpassID):

    cap = cv2.VideoCapture(0)
    # initialize the cv2 QRCode detector

    detector = cv2.QRCodeDetector()

    while True:
        _, img = cap.read()
        data, bbox, tmp = detector.detectAndDecode(img)
        if data:
            print(f"QRCode data:\n{data}")
            break

    validation_response = requests.get(f"http://{USER_VALIDATION_SERVICE_HOST}:{USER_VALIDATION_SERVICE_PORT}/holder/{int(id)}")
    if validation_response.text == 'Failed':
        return validation_response.text
    date = str(datetime.datetime.now().date())
    time = str(datetime.datetime.now().time())

    checkin_response = requests.post(f"http://{AREA_MANAGER_SERVICE_HOST}:{AREA_MANAGER_SERVICE_PORT}/checkin/{areaID}/{data}/{date}/{time}")
    return checkin_response

def check_out(areaID):
    cap = cv2.VideoCapture(0)
    # initialize the cv2 QRCode detector

    detector = cv2.QRCodeDetector()
    data = 1234567890
    while True:
        _, img = cap.read()
        data, bbox, tmp = detector.detectAndDecode(img)
        if data:
            print(f"QRCode data:\n{data}")
            break

    validation_response = requests.get(f"http://{USER_VALIDATION_SERVICE_HOST}:{USER_VALIDATION_SERVICE_PORT}/holder/{int(id)}")

    if validation_response.text == 'Failed':
        return validation_response.text
    date = str(datetime.datetime.now().date())
    time = str(datetime.datetime.now().time())

    checkout_response = requests.post(f"http://{AREA_MANAGER_SERVICE_HOST}:{AREA_MANAGER_SERVICE_PORT}/checkin/{areaID}/{data}/{date}/{time}")
    return checkout_response
    #AreaID, CrownpassID, EntryDate, EntryTime, ExitDate, ExitTime