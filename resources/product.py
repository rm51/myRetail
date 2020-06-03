import flask
import requests
import simplejson as json
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from pymongo import MongoClient


#from database.models import TablePrice
from flask_restful import Resource

app = flask.Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/local"
app.config['MONGO_DBNAME'] = 'price'

mongo = PyMongo(app)
db = mongo.db
col = mongo.db["price"]

class ProductApi(Resource):	
	
	def get(self, product_id):
		"""
		Function to get the product details including price.
		"""
	

		url = "https://redsky.target.com/v2/pdp/tcin/%s?excludes=taxonomy,price,promotion,bulk_ship,rating_and_review_reviews,rating_and_review_statistics,question_answer_statistics" %product_id
		response = requests.get(url)
		if response.status_code == 404:
			return "Product not found"

		json_response = response.json()

		prod_id = int(product_id)
		
		title = json_response["product"]["item"]["product_description"]["title"]

		if title == None:
			return "Title not found"
		document = col.find_one({'id': prod_id})
		
		if document == None:
			return "Product not found in the db"

    
		price = document.get("price")
	
		product_json = {
			"id": prod_id,
			"title": title,
			"current_price": {"value": price, "currency_code": "USD"
			}
			}
		json_dumps = json.dumps(product_json)

		return json_dumps, 200	


	def put(self, product_id):
		"""
		Function to update the product price.
		"""
	
		
		url = "https://redsky.target.com/v2/pdp/tcin/%s?excludes=taxonomy,price,promotion,bulk_ship,rating_and_review_reviews,rating_and_review_statistics,question_answer_statistics" %product_id
		response = requests.get(url)
		if response.status_code == 404:
			return "Product not found"

		json_response = response.json()

		prod_id = int(product_id)
		
		title = json_response["product"]["item"]["product_description"]["title"]
		
		if title == None:
			return "Title not found"

		
			
		data = request.get_json()
		print ("data ", data)

		updated_price = data["new_price"]
			
		col.find_one_and_update({'id': prod_id}, {'$set':{'price': updated_price}})
		return "OK"
		


# uplaod before 10am




