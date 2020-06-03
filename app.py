import os
import flask
import requests
import simplejson as json
from flask import Flask, request, jsonify
from database.db import initialize_db
from flask_pymongo import PyMongo
from pymongo import MongoClient
from flask_restful import Api
from resources.routes import initialize_routes

app = flask.Flask(__name__)
api = Api(app)


app.config["MONGO_URI"] = "mongodb://localhost:27017/local"
app.config['MONGO_DBNAME'] = 'price'

#initialize_db(app)
initialize_routes(api)

app.run()
		



