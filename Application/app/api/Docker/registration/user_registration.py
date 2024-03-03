from flask import Flask
from pymongo import MongoClient
import simplejson as json

app = Flask(__name__)

def connect():
    conn_str = 'mongodb+srv://big-data:database5@cluster0.tfurl.mongodb.net/'
    client = MongoClient(conn_str)
    return client


@app.route('/area/<area>', methods=['POST'])
def register_area(area):
    client = connect()
    db = client.get_database("Area_Database")
    collection = db.Areas
    already_exists = False
    #check username also location and name details to ensure they arent already used
    area = json.loads(area)
    print("area", area)
    area=dict(area)
    print("area", area)
    x = collection.find({"Postcode": area["postcode"],
        "County": area["county"],
        "City": area["city"],
        "Street": area["street"],
        "Num": area["areaNum"],})
    for doc in x:
        return "This area is already registered"

    x = collection.find({"UserName": area["userName"]})
    for doc in x:
        return "Username exists"

    new_area = {
        "_id": str(area["areaID"]),
        "Password": area["password"],
        "AreaName": area["areaName"],
        "UserName": area["userName"],
        "Postcode": area["postcode"],
        "County": area["county"],
        "City": area["city"],
        "Street": area["street"],
        "Num": area["areaNum"],
        "EntryLvl": area["entryLvl"],
        "CurrentNum": area["currentNum"],
        "MaxNum": area["maxNum"]
    }

    collection.insert_one(new_area)
    x = collection.find({"_id":str(area["areaID"])})
    print(x)
    for doc in x:
        return "Registration Complete"
    return "Unknown Error"

@app.route('/staff/<staff>', methods=['POST'])
def register_staff(staff):
    client = connect()
    db = client.get_database("Staff_Database")
    collection = db.Staff

    staff = json.loads(staff)
    # check username doesnt exist for area
    x = collection.find({"UserName" : staff["username"]})
    for doc in x:
        return "Username exists"

    new_staff = {
        "_id": str(staff["staffID"]),
        "areaid": str(staff["areaID"]),
        "UserName": staff["username"],
        "Password": staff["password"]
    }

    collection.insert_one(new_staff)
    x = collection.find({"_id": str(staff["staffID"])})
    print(x)
    for doc in x:
        return "Registration Complete"
    return "Unknown Error"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=50052)