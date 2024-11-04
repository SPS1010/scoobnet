import openai
import os
import json
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_KEY")

def loadhuntdata():
    with open("hunts.json", "r") as file:
        huntdata = json.load(file)
    huntinfo = "\n".join(
        f"Hunt ID: {hunt['hunt_id']}, Name: {hunt['huntName']}, "
        f"Owner: {hunt['huntOwner']}, Active: {hunt['huntActive']}, "
        f"Description: {hunt['huntDesc']}, Banner: {hunt['huntBanner']}"
        for hunt in huntdata
    )
    return huntinfo
  
SYS_PROMPT = f"Respond according to the following data:\n\n{loadhuntdata()}"

@app.route('/message', methods=['POST'])
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
