myRetail RESTful Service
It assumes python, mongodb and pip are already installed. To install the dependencies pip install -r requirements.txt

To run the server:

From the target directory - flask run

To get the product using postman: http://localhost:5000/api/products/<product_id>

To update the price using postman: http://localhost:5000/api/products/13860428 body = {"new_price": 0.96}

To run tests: In the test directory pytest update_product.py
 
<img src="https://github.com/rm51/myRetail/blob/master/tests.png">
