import json
import random
import string
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)
PDB_FILE = 'posts.json'

def genid():
    return ''.join(random.choices(string.digits, k=10))

def loaddb():
    try:
        with open(PDB_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def savedb(data):
    with open(PDB_FILE, 'w') as file:
        json.dump(data, file, indent=4)

@app.route('/create-post', methods=['POST'])
def postPost():
    data = request.json
    post_id = genid()
    timestamp = datetime.now().isoformat()
    
    new_post = {
        "username": data.get("username", "Anonymous"),
        "postText": data.get("postText", ""),
        "timestamp": timestamp
    }
    
    db = loaddb()
    db[post_id] = new_post
    savedb(db)
    
    return jsonify({"message": "Post created", "post-id": post_id}), 201

if __name__ == '__main__':
    app.run(debug=True)
