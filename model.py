""" Models for tea app. """

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user object representing a user who created an account."""

    __tablename__ = "users"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, nullable = False, unique=True)
    password = db.Column(db.String, nullable = False)
    firstname = db.Column(db.String, nullable = False)

    def __repr__(self):
        return f"<User id= {self.id} firstname= {self.firstname}>"



class Tea(db.Model):
    """A tea object representing different types of teas."""

    __tablename__ = "teas"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String, nullable = False, unique = True)
    description = db.Column(db.Text, nullable = False)
    benefit = db.Column(db.Text, nullable = False)
    image_url = db.Column(db.String, nullable = False)
    
    def __repr__(self):
        return f"<Tea id= {self.id} name= {self.name}>"



class Favorite(db.Model):
    """A favorite tea object representing teas that user 'favorites'."""

    __tablename__ = "favorites"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    tea_id = db.Column(db.Integer, db.ForeignKey("teas.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    tea = db.relationship("Tea", backref="favorites")
    user = db.relationship("User", backref="favorites")
   
    def __repr__(self):
        return f"<Favorite tea_id={self.tea_id} user_id={self.user_id}>"
    


def connect_to_db(flask_app, db_uri="postgresql:///teas", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")
    
    
    
def test_data():
    """Create some sample data."""

    User.query.delete()
    Tea.query.delete()

    test_user = User(id=150,
            email="user@test.com",
            password="testing",
            firstname="testuser")
    
    chai_tea = Tea(id=70, 
                    name="chaitea", 
                    description="Chai tea is a sweet and spicy tea renowned for its fragrant aroma.", 
                    benefit="help boost heart health, reduce blood sugar levels, aid digestion and help with weight loss", 
                    image_url="data:image/jpeg;base64,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")
    lemon_tea = Tea(id=80,
                    name="lemontea",
                    description="Lemon Tea is a refreshing tea where lemon juice is added in black or green tea.",
                    benefit=" soothes the throat, prevents cough and congestion",
                    image_url="data:image/jpeg;base64,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"
                    )
    
    db.session.add_all([test_user, 
                        chai_tea, 
                        lemon_tea])
    db.session.commit()



if __name__ == "__main__":
    from server import app

    connect_to_db(app)
    db.create_all()

