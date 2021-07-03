from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_jwt import JWT, jwt_required
from firstapi.finalapi3 import autentication, identity
from resources.userresources import Userregister
from resources.item_database import Item, Itemlist


from resources.model_resourcde import Modell,Storelist
from models.store_model import StoreModel



app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///database1.db"
app.secret_key = "shi"
db.init_app(app)



jwt = JWT(app, autentication, identity)


items = []
api.add_resource(Itemlist, "/items")
api.add_resource(Item, "/item/<string:name>")
api.add_resource(Userregister, "/register")
api.add_resource(Modell,"/store/<string:name>")
api.add_resource(Storelist,"/stores")


if __name__ == "__main__":
    app.run(port=1000)
    


