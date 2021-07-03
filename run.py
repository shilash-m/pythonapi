from finalapi1 import app
from d import db

db.init_app(app)
@app.before_first_request
def create_table():
    db.create_all()