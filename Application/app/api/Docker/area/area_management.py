from concurrent import futures
from uuid import uuid4
from flask import Flask
from pymongo import MongoClient
import simplejson as json

app = Flask(__name__)

def connect():
    conn_str = 'mongodb+srv://big-data:database5@cluster0.tfurl.mongodb.net/'
    client = MongoClient(conn_str)
    return client

@app.route('/checkin/<areaid>/<holderid>/<date>/<time>', methods=['POST'])
def check_in_crownpass(areaid, holderid, date,time):
    client = connect()

    db = client.get_database("Area_Database")
    collection = db.Areas

    x = collection.find({"_id": areaid})

    for doc in x:
        if doc['MaxNum'] != doc['CurrentNum']:
            ans = meet_requirements(holderid, doc['EntryLvl'])
            if not ans:
                return "Does not meet requirements"
            newNum = int(doc['CurrentNum']) + 1
            collection.update_one({"_id": areaid}, {"$set": { "CurrentNum" : str(newNum)}})
            x = collection.find({"_id": areaid})
            for doc in x:
                print(doc)
        else:
            return "Too many Customers"

    db = client.get_database("Area_Entry_Database")
    collection = db["Area Entry"]
    entry_id = str(uuid4())
    entry = {
        "_id" : entry_id,
        "Areaid" : areaid,
        "Holderid" : holderid,
        "EntryDate" : str(date),
        "EntryTime" : str(time),
        "ExitDate" : "",
        "ExitTime" : "",
    }
    collection.insert_one(entry)
    x = collection.find({"_id": str(entry_id)})
    for doc in x:
        return "Check in complete"
    return "Error"

@app.route('/checkout/<areaid>/<holderid>/<date>/<time>', methods=['POST'])
def check_out_crownpass(areaid, holderid, date, time):
    client = connect()

    db = client.get_database("Area_Entry_Database")
    collection = db["Area Entry"]

    collection.update_one({"Areaid" : areaid, "Holderid": holderid}, {"$set" : {"ExitDate" : str(date), "ExitTime" : str(time)}})

    x = collection.find({"_id": str(holderid)})
    for doc in x:
        print(doc)

    db = client.get_database("Area_Database")
    collection = db.Areas

    x = collection.find({"_id": areaid})
    for doc in x:
        newNum = int(doc['CurrentNum']) - 1
        collection.update_one({"_id": areaid}, {"$set": {"CurrentNum": str(newNum)}})
        return "Check out complete"
    return "Unknown Error"


def meet_requirements(id, lvl):
    client = connect()

    db = client.get_database("Crownpass_Holder")
    collection = db.Crownpass_Holder

    x = collection.find({"_id": int(id)})
    for doc in x:
        print(doc)
        if doc['infection'] >= lvl:
            return True
    return False

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=50051)