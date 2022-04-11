import os
import json
from random import choice, randint

import crud
import model
import server
import yaml 

os.system("dropdb teas")
os.system("createdb teas")

config = yaml.safe_load(open("config/config.yaml"))
type = config["database"]["type"]
username = config["database"]["username"]
password = os.environ[config["database"]["password"]]
host = config["database"]["host"]
port = config["database"]["port"]
database = config["database"]["database"]
db_uri = "{type}://{username}:{password}@{host}:{port}/{database}".format(type=type, username=username, password=password, host=host, port=port, database=database)
print("server main", db_uri)
server.app.config.update(
    SQLACHEMY_DATABASE_URI=db_uri
)

model.connect_to_db(server.app)
model.db.create_all()

# Load tea data from JSON file
with open("data/teas.json") as f:
    tea_data = json.loads(f.read())

# Create teas, store them in list so that we can use them
teas_in_db = []
for tea in tea_data:
    name, description, benefit, image_url = (
        tea["name"],
        tea["description"],
        tea["benefit"],
        tea["image_url"],
    )

    db_tea = crud.create_tea(name, description, benefit, image_url)
    teas_in_db.append(db_tea)
    
for n in range(10):
    firstname = (f"Test {n}")
    email = (f"user{n}@test.com" )
    password = "test"

    user = crud.create_user(email, firstname, password)