import os
from uuid import uuid4
import requests
from flask import Flask

USER_REGISTRATION_SERVICE_HOST = "localhost"
USER_REGISTRATION_SERVICE_PORT = "50052"

USER_VALIDATION_SERVICE_HOST = "localhost"
USER_VALIDATION_SERVICE_PORT = "50053"


app = Flask(__name__)

class AreaAccount:
    def __init__(self):
        self.areaID = ''
        self.password = ''
        self.areaName = ''
        self.userName = ''
        self.postcode = ''
        self.county = ''
        self.city = ''
        self.street = ''
        self.areaNum = ''
        self.entryLvl = ''
        self.staff = []
        self.currentNum = ''
        self.maxNum = ''


    def register(self, area_details):
        self.areaID = str(uuid4())
        self.password = area_details['password']
        self.areaName = area_details['areaName']
        self.userName = area_details['username']
        self.postcode = area_details['postcode']
        self.county = area_details['county']
        self.city = area_details['city']
        self.street = area_details['street']
        self.areaNum = area_details['areaNum']
        self.entryLvl = area_details['entryLvl']
        self.currentNum = '0'
        self.maxNum = area_details['maxNum']
        #jsonStr = json.dumps(self.__dict__)
        new_area = json.dumps(
            {"areaID": self.areaID, "password": self.password, "areaName": self.areaName,
             "userName": self.userName, "postcode": self.postcode, "county": self.county,
             "city": self.city, "street": self.street, "areaNum": self.areaNum, "entryLvl": self.entryLvl, "maxNum": self.maxNum,
             "currentNum": 0})

        response = requests.post(
            f'http://{USER_REGISTRATION_SERVICE_HOST}:{USER_REGISTRATION_SERVICE_PORT}/area/{new_area}')

        print("code: " + str(response.status_code))
        print("headers: " + str(response.headers))
        print("content: " + str(response.text))
        return str(response.text)

    def login(self, user, area_passw):
        #username = "towny9"
        #password = "123testing!2"
        validation_response = requests.get(
            f"http://{USER_VALIDATION_SERVICE_HOST}:{USER_VALIDATION_SERVICE_PORT}/area/{user}/{area_passw}")

        print("code: " + str(validation_response.status_code))
        print("headers: " + str(validation_response.headers))
        print("content: " + str(validation_response.text))

        #possibly response.text
        if isinstance(validation_response, str):
            return validation_response
        else:
            self.areaID = validation_response['_id']
            self.password = validation_response['Password']
            self.areaName = validation_response['AreaName']
            self.userName = validation_response['UserName']
            self.postcode = validation_response['Postcode']
            self.county = validation_response['County']
            self.city = validation_response['City']
            self.street = validation_response['Street']
            self.areaNum = validation_response['Num']
            self.entryLvl = validation_response['EntryLvl']
            self.currentNum = validation_response['CurrentNum']
            self.maxNum = validation_response['MaxNum']
            return self


    def get_staff(self):
        pass

    def get_customers(self):
        pass