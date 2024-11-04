from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os
import json

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY")

def loadhuntdata():
    hunt_file = os.path.join(os.path.dirname(__file__), 'hunts.json')
    if os.path.exists(hunt_file):
        with open(hunt_file, 'r') as file:
            huntdata = json.load(file)
        huntinfo = "\n".join(
            f"Hunt ID: {hunt['huntID']}, Name: {hunt['huntName']}, "
            f"Owner: {hunt['huntOwner']}, Active: {hunt['huntActive']}, "
            f"Description: {hunt['huntDesc']}, Banner: {hunt['huntBanner']}"
            for hunt in huntdata['hunts']
        )
    else:
        huntinfo = "No hunt data available."
    return huntinfo

SYS_PROMPT = f"Respond according to the following data:\n\n{loadhuntdata()}"

@app.route('/api/message', methods=['POST'])
def message():
    data = request.json
    user_message = data.get("message", "")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": SYS_PROMPT},
                {"role": "user", "content": user_message}
            ]
        )
        reply = response['choices'][0]['message']['content']
        return jsonify({"AI": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
