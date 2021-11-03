"""CRUD operations."""

from model import db, User, Tea, Keyword, Favorite, QuizResult, connect_to_db

def create_user(email, firstname, password):
    """Create and return a new user."""

    user = User(email=email, firstname = firstname, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def create_tea(name, description, benefit, image_url):
    """Create and return a new tea."""

    tea = Tea(name = name, 
        description = description,
        benefit = benefit,
        image_url =image_url,
    )

    db.session.add(tea)
    db.session.commit()

    return tea


def get_teas():
    """Return all teas."""

    return Tea.query.all()


def get_tea_by_id(id):
    """Return a tea by primary key."""

    return Tea.query.get(id)



if __name__ == "__main__":
    from server import app

    connect_to_db(app)



