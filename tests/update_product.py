import unittest
import requests
import json
from random import random

class GetProductTest(unittest.TestCase):


	def test_get_product(self):
		url = 'http://localhost:5000/api/products/54456119'
		
		response = requests.get(
			url)
		response_body = response.json()
		response_body_json = json.loads(response_body)
		print ("response_body ", response_body)
		print("response body cuerrent price ", response_body_json["title"])

		assert response.status_code == 200
		assert response_body_json["current_price"]["currency_code"] == "USD"
		assert response_body_json["title"] == "Creamy Peanut Butter 40oz - Good &#38; Gather&#8482;"

	def test_update_product(self):
		url = 'http://localhost:5000/api/products/13860428'
		new_price = random()
		payload = {"new_price": new_price}
		print ("payload ", payload)
		payload_json = json.dumps(payload)
		print("payload_json ", payload_json)
		headers = {'Content-Type': 'application/json' } 
		response = requests.put('http://localhost:5000/api/products/13860428', json=payload)
			
		get_product_response = requests.get(url)
		get_product_response_body = get_product_response.json()
		get_product_response_body_json = json.loads(get_product_response_body)

		assert get_product_response_body_json["current_price"]["value"] == new_price
		assert response.status_code == 200

		

if __name__ == "__main__":
	unittest.main()
