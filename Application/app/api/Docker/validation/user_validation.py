from flask import Flask
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection

app = Flask(__name__)

def connect():
    conn_str = 'mongodb+srv://big-data:database5@cluster0.tfurl.mongodb.net/'
    client = MongoClient(conn_str)
    return client


@app.route('/holder/<id>', methods=['GET'])
def get_holder(id: int):
    client = connect()
    db = Database(client, 'Crownpass_Holder')
    col = Collection(db, 'Crownpass_Holder')

    holder =list(col.find({'_id': int(id)}))
    #holder = col.find({'_id': id})
    print(holder)
    if not holder:
        return "Failed"
    else:
        return "Success"

@app.route('/area/<username>/<password>', methods=['GET'])
def validate_area(username, password):
    client = connect()

    db = client.get_database("Area_Database")
    collection = db.Areas

    x = list(collection.find({"UserName": username, "Password": password}))
    print(x)
    for result in x:
        return result
    return "Failed"

@app.route('/staff/<username>/<password>', methods=['GET'])
def validate_staff(username, password):
    client = connect()

    db = client.get_database("Staff_Database")
    collection = db.Staff

    x = list(collection.find({"UserName": username, "Password": password}))
    print(x)
    for result in x:
        return result
    return "Failed"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=50053)