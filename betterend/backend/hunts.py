import json
import random
import string
from flask import Flask, request, jsonify

app = Flask(__name__)
DB_FILE = 'hunts.json'

def genid():
    return ''.join(random.choices(string.digits, k=10))

def loaddb():
    try:
        with open(DB_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def savedb(data):
    with open(DB_FILE, 'w') as file:
        json.dump(data, file, indent=4)

@app.route('/create-hunt', methods=['POST'])
def createHunt():
    data = request.json
    hunt_id = genid()
    new_hunt = {
        "huntName": data.get("huntName", "Unnamed Hunt"),
        "huntOwner": data.get("huntOwner", "Anonymous"),
        "huntActive": data.get("huntActive", True),
        "huntDesc": data.get("huntDesc", ""),
        "huntBanner": data.get("huntBanner", "")
    }
    db = loaddb()
    db[hunt_id] = new_hunt
    savedb(db)
    return jsonify({"message": "Hunt created", "hunt-id": hunt_id}), 201

@app.route('/hunts', methods=['GET'])
def getHunts():
    db = loaddb()
    hunts_list = [{"huntID": k, **v} for k, v in db.items()]
    return jsonify({"hunts": hunts_list})

if __name__ == '__main__':
    app.run(debug=True)
