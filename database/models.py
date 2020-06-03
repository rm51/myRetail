from .db import db

class TablePrice(db.Document):
	id = db.IntField(required=True, unique=True)
	price = db.FloatField(required=True)