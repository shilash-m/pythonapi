from flask_restful import Resource,reqparse
import sqlite3
from models.finalapi2 import UserModel
from d import db


class Userregister(Resource):
    requested = reqparse.RequestParser()
    requested.add_argument("username", type=str, required=True, help="soort")
    requested.add_argument("password", type=str, required=True, help="soort")

    def post(self):
        data= Userregister.requested.parse_args()

        if UserModel.finding_name(data['username']):
            return {"message":"already this name exists"}

        else:
            userr=UserModel(data['username'],data['password'])
            userr.save_to_db()

            return{"message0":"created successfully"}
