# Creates a simple API
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

from flask import Flask,request,json
from algorithm import simplify
app = Flask(__name__)


fields = [
    'house',
    'street',
    'locality',
    'landmark',
    'village',
    'subdistrict',
    'district',
    'state',
    'pincode'
]


@app.route("/",methods=['GET','POST'])
def hello_world():
    data = request.json
    for field in fields:
        assert field in data
    address = simplify(**data)
    app.logger.info(f'[Address processed] : {address}')
    return {
        'address':address
    }
    