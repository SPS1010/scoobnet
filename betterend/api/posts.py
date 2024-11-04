import json
from flask import Flask, jsonify

app = Flask(__name__)
PDB_FILE = 'posts.json'

def loaddb():
    try:
        with open(PDB_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

@app.route('/api/posts', methods=['GET'])
def handler():
    db = loaddb()
    posts_list = list(db.values())
    return jsonify(posts_list)

handler = app
