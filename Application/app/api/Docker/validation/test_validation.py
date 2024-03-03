import requests

USER_VALIDATION_SERVICE_HOST = "localhost"
USER_VALIDATION_SERVICE_PORT = "50053"

def test_holder_validation():
    id = 1234567898
    response = requests.get(f"http://{USER_VALIDATION_SERVICE_HOST}:{USER_VALIDATION_SERVICE_PORT}/holder/{int(id)}")

    print("code: " + str(response.status_code))
    print("headers: " + str(response.headers))
    print("content: " + str(response.text))
    assert response.text == "Success"


def test_staff_validation():
    username = "staff2"
    password = "staff2pass!"
    response = requests.get(f"http://{USER_VALIDATION_SERVICE_HOST}:{USER_VALIDATION_SERVICE_PORT}/staff/{username}/{password}")

    print("code: " + str(response.status_code))
    print("headers: " + str(response.headers))
    print("content: " + str(response.text))
    assert "UserName" in response.text

def test_area_validation():
    username = "towny9"
    password = "123testing!2"
    response = requests.get(f"http://{USER_VALIDATION_SERVICE_HOST}:{USER_VALIDATION_SERVICE_PORT}/area/{username}/{password}")

    print("code: " + str(response.status_code))
    print("headers: " + str(response.headers))
    print("content: " + str(response.text))
    assert "AreaName" in response.text