import os
import json
import flask
from flask import Flask, jsonify, abort
from markupsafe import escape
from datetime import datetime
from string import ascii_uppercase
import random
from itertools import islice

app = Flask(__name__)

events_json={'tables':{'name':'PrimaryResult','columns':[{'name':'time','type':'string'},{'name':'data','type':'string'}],'rows':[]}}

#random chars in upper case
def random_chars(size, chars=ascii_uppercase):
    selection = iter(lambda: random.choice(chars), object())
    while True:
        yield ''.join(islice(selection, size))

@app.route('/events',methods=["GET"])
def get_event():
    x = (random.randint(1, 5))
    random_gen = random_chars(6000)
    current_date_time = datetime.now().isoformat()
    for i in range(x):
        events_json["tables"]["rows"].append({current_date_time:next(random_gen)}) 
    return jsonify(events_json), 200
