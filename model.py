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
    
    
    
class Keyword(db.Model):
    """A keyword object referencing to specfic benefit or preference of a tea."""

    __tablename__ = "keywords"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    keyword = db.Column(db.String, nullable = False)
    tea_id = db.Column(db.Integer, db.ForeignKey("teas.id"), nullable = False)

    tea = db.relationship("Tea", backref="keywords")
    
    def __repr__(self):
        return f"<Keyword id={self.id}  keyword={self.keyword}>"


class QuizResult(db.Model):
    """A quiz result object that represents the result of a quiz taken by a user."""

    __tablename__ = "quiz_results" 

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    qresult = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    tea_id = db.Column(db.Integer, db.ForeignKey("teas.id"), nullable = False)
    
    tea = db.relationship("Tea", backref="quiz_results")
    user = db.relationship("User", backref="quiz_results")

    def __repr__(self):
        return f"<QuizResult id={self.id} Quiz Result={self.qresult}>"


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
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False #what does this mean? 

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")



if __name__ == "__main__":
    from server import app

    connect_to_db(app)
    db.create_all()

