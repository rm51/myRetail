from .product import ProductApi

def initialize_routes(api):
	api.add_resource(ProductApi, '/api/products/<product_id>')