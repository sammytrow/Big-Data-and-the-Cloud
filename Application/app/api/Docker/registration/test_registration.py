import requests
import json
USER_REGISTRATION_SERVICE_HOST = "localhost"
USER_REGISTRATION_SERVICE_PORT = "50052"


def test_staff_registraion():
    new_staff = json.dumps({"staffID": "121", "areaID": "12testyou", "username": "st1aff1", "password": "test_password1"})
    response = requests.post(f"http://{USER_REGISTRATION_SERVICE_HOST}:{USER_REGISTRATION_SERVICE_PORT}/staff/{new_staff}")

    print("code: " + str(response.status_code))
    print("headers: " + str(response.headers))
    print("content: " + str(response.text))

    assert isinstance(response.text, str)


def test_area_registraion():
    new_area = json.dumps({"areaID" : "12testyou", "password" : "test_password", "areaName" : "The Four Candles - JD Wetherspoon", "userName" : "4candles","postcode" : "OX4 3LR", "county" : "Oxfordshire",
                "city" : "Oxford", "street" : "Between Towns Rd", "areaNum" : "59a", "entryLvl" : "2", "maxNum" : "50", "currentNum" : 0})

    response = requests.post(f'http://{USER_REGISTRATION_SERVICE_HOST}:{USER_REGISTRATION_SERVICE_PORT}/area/{new_area}')

    print("code: " + str(response.status_code))
    print("headers: " + str(response.headers))
    print("content: " + str(response.text))

    assert isinstance(response.text, str)