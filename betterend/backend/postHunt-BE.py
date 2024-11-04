import json
import random
import string
from flask import Flask,request,jsonify

app=Flask(__name__)
DB_FILE='hunts.json'
def genid():return ''.join(random.choices(string.digits,k=10))
def loaddb():
 try:
  with open(DB_FILE,'r') as file:return json.load(file)
 except FileNotFoundError:return {}

def savedb(data):
 with open(DB_FILE,'w') as file:json.dump(data,file,indent=4)

@app.route('/create-post',methods=['POST'])
def postPost():
 data=request.json
 hunt_id=genid()
 new_post={
  "huntName":data.get("huntName","Unnamed Hunt"),
  "huntOwner":data.get("huntOwner","Anonymous"),
  "huntActive":data.get("huntActive","true"),
  "huntDesc":data.get("huntDesc",""),
  "huntBanner":data.get("huntBanner","")}
 db=loaddb();db[hunt_id]=new_post;savedb(db)
 return jsonify({"message":"Post created","hunt-id":hunt_id}),201

if __name__=='__main__':
 app.run(debug=True)
