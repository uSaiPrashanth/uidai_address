# Creates a simple API

from flask import Flask,request,json
from algorithm import simplify
app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def hello_world():
    data = request.json
    address = simplify(**data)
    return {
        'address':address
    }
    