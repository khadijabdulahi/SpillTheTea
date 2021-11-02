""" Models for tea app. """

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user object."""

    __tablename__ = "users"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    firstname = db.Column(db.String)


    def __repr__(self):
        return f"<User id={self.id} email={self.firstname}>"


class Tea(db.Model):
    """A tea object representing different types of teas."""

    __tablename__ = "teas"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String, unique = True, nullable = False)
    image_id = db.Column(db.String, nullable = False)
    description = db.Column(db.Text, nullable = False)
    benefit = db.Column(db.Text, nullable = False)
    fav_id = db.Column(db.Integer, db.ForeignKey("Favorite.id"))

    favorite_tea = db.realationship("Favorite", backref= "teas")
    
    def __repr__(self):
        return f"<Movie id={self.id} name={self.title}>"


class Image(db.Model):
    """An image object for each tea."""

    __tablename__ = "images"

    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String)
    tea_id = db.Column(db.Integer, db.ForeignKey("tea.id"))

    tea = db.relationship("Tea", backref="favorites")
    
    def __repr__(self):
        return f"<Image id={self.id} Tea id={self.tea_id}>"


class QuizResult(db.Model):
    """A quiz result object that represents the result of a quiz taken by a user."""

    __tablename__ = "quiz_results" 

    id = db.Column(db.Integer, primary_key=True)
    qresult = db.Column(db.String)
    user_id = db.Column(db.String)
    tea_id = db.Column(db.Integer, db.ForeignKey("tea.id"))
    
    tea = db.relationship("Tea", backref="favorites")
    user = db.relationship("User", backref="favorites")

    def __repr__(self):
        return f"<QuizResult id={self.id} Quiz Result={self.qresult}>"


class Favorite(db.Model):
    """A favorite tea object."""

    __tablename__ = "favorites"

    id = db.Column(db.Integer, primary_key=True)
    tea_id = db.Column(db.Integer, db.ForeignKey("teas.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    tea = db.relationship("Tea", backref="favorites")
    user = db.relationship("User", backref="favorites")
    def __repr__(self):
        return f"<Favorite tea_id={self.tea_id} user_id={self.user_id}>"



def connect_to_db(flask_app, db_uri="postgresql:///teas", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False #what does this mean? 

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    connect_to_db(app)
