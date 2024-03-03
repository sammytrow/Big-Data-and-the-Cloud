import json
from flask import Flask
import datetime
import requests

app = Flask(__name__)

USER_REGISTRATION_SERVICE_HOST = "localhost"
USER_REGISTRATION_SERVICE_PORT = "50052"

USER_VALIDATION_SERVICE_HOST = "localhost"
USER_VALIDATION_SERVICE_PORT = "50053"

class StaffAccount:
    def __init__(self):
        self.areaID = ''
        self.staffID = ''
        self.username = ''
        self.password = ''

    def register(self, staff_details, area_id):
        self.areaID = str(area_id)
        self.staffID = str(uuid4())
        self.username = staff_details['username']
        self.password = staff_details['password']

        new_staff = json.dumps({"staffID": self.staffID, "areaID": self.areaI, "username": self.username, "password": self.password})
        response = requests.post(
            f"http://{USER_REGISTRATION_SERVICE_HOST}:{USER_REGISTRATION_SERVICE_PORT}/staff/{new_staff}")

        print("code: " + str(response.status_code))
        print("headers: " + str(response.headers))
        print("content: " + str(response.text))

        return str(response.text)

    def login(self, user, passw):
        #username = "staff2"
        #password = "staff2pass!"
        validation_response = requests.get(
            f"http://{USER_VALIDATION_SERVICE_HOST}:{USER_VALIDATION_SERVICE_PORT}/staff/{user}/{passw}")

        print("code: " + str(validation_response.status_code))
        print("headers: " + str(validation_response.headers))
        print("content: " + str(validation_response.text))
        if isinstance(validation_response, str):
            return validation_response
        else:
            self.areaID = validation_response['_id']
            self.staffID = validation_response['areaid']
            self.username = validation_response['UserName']
            self.password = validation_response['Password']
            return self