import datetime

import requests
import json

AREA_MANAGER_SERVICE_HOST = "localhost"
AREA_MANAGER_SERVICE_PORT = "50051"

def test_checkin():
    area_id = "12testyou"
    holder_id = int(1234567898)
    date = str(datetime.datetime.now().date())
    time = str(datetime.datetime.now().time())
    response = requests.post(f"http://{AREA_MANAGER_SERVICE_HOST}:{AREA_MANAGER_SERVICE_PORT}/checkin/{area_id}/{holder_id}/{date}/{time}")

    print("code: " + str(response.status_code))
    print("headers: " + str(response.headers))
    print("content: " + str(response.text))

    assert isinstance(response.text, str)

def test_checkout():
    area_id = "12testyou"
    holder_id = int(1234567898)
    date = str(datetime.datetime.now().date())
    time = str(datetime.datetime.now().time())
    response = requests.post(f"http://{AREA_MANAGER_SERVICE_HOST}:{AREA_MANAGER_SERVICE_PORT}/checkin/{area_id}/{holder_id}/{date}/{time}")

    print("code: " + str(response.status_code))
    print("headers: " + str(response.headers))
    print("content: " + str(response.text))

    assert isinstance(response.text, str)