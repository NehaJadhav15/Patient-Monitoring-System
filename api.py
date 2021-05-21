
import flask
from flask import jsonify
import json
import requests
import urllib
from urllib import request
data1=urllib.request.urlopen(" https://api.thingspeak.com/channels/1370583/feeds.json?api_key=66XCGCEBQ2YCUDF8&results=2");
my_json=data1.read().decode('utf-8')
data=json.loads(my_json);
final_data=json.dumps(data)
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def home():
   return data

app.run()
