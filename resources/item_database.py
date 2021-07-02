from flask_restful import Resource, reqparse
import sqlite3
from flask_jwt import jwt_required
from models.item_model import ItemModel
from flask_sqlalchemy import SQLAlchemy
from d import db


class Item(Resource):

    requested = reqparse.RequestParser()
    requested.add_argument('price', type=float, required=True,
                           help="sorry only float accepted and need to input something")
    requested.add_argument('store_id', type=str, required=True,
                           help="sorry every thing need a store_id")


    def get(self, name):
        item = ItemModel.find_by_name(name)
        return item.json()


    def post(self, name):
        if ItemModel.find_by_name(name):
            return {"message": "sorry"}
        data = Item.requested.parse_args()
        item = ItemModel(name,data['price'],data['store_id'])
        item.save_to_db()
        return item.json()


    def put(self, name):
        data = Item.requested.parse_args()
        item = ItemModel.find_by_name(name)
        if item:
           item.price=data['price']
        else:
            item=ItemModel(name,data['price'],data['store_id'])


        item.save_to_db()
        return item.json()


    def delete(self, name):
        item=ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {"m":"delted successfully"}



class Itemlist(Resource):

    def get(self):
        return {"item":[x for x in ItemModel.query.all()]}
