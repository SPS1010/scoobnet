import json
from flask import Flask, jsonify

app = Flask(__name__)
DB_FILE = 'hunts.json'

def loaddb():
    try:
        with open(DB_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

@app.route('/api/hunts', methods=['GET'])
def handler():
    db = loaddb()
    hunts_list = [{"huntID": k, **v} for k, v in db.items()]
    return jsonify({"hunts": hunts_list})

handler = app
