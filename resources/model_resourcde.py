from flask_restful import Resource, reqparse
import sqlite3
from flask_jwt import jwt_required
from models.item_model import ItemModel
from flask_sqlalchemy import SQLAlchemy
from d import db
from models.store_model import StoreModel


class Modell(Resource):


    def get(self, name):
        item = StoreModel.find_by_name(name)
        return item.json()


    def post(self, name):
        if StoreModel.find_by_name(name):
            return {"message": "sorry no store available in this name"}
        #data = Modell.requested.parse_args()
        item = StoreModel(name)
        item.save_to_db()
        return item.json()


    def put(self, name):
#        data = Modell.requested.parse_args()
        item = StoreModel.find_by_name(name)



        item.save_to_db()
        return item.json()


    def delete(self, name):
        item=StoreModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {"m":"delted successfully"}



class Storelist(Resource):

    def get(self):
        return {"item":[x for x in StoreModel.query.all()]}