import os
import json
from random import choice, randint

import crud
import model
import server

os.system("dropdb teas")
os.system("createdb teas")

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