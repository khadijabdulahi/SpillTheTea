"""CRUD operations."""

from model import db, User, Tea, Favorite, connect_to_db

def create_tea(name, description, benefit, image_url):
    """Create and return a new tea."""

    tea = Tea(name=name, 
        description=description,
        benefit=benefit,
        image_url=image_url)
    
    db.session.add(tea)
    db.session.commit()

    return tea


def get_teas():
    """Return all teas."""

    return Tea.query.all()


def get_tea_by_id(id):
    """Return a tea by primary key."""

    return Tea.query.get(id)


def create_user(email, firstname, password):
    """Create and return a new user."""

    user = User(email=email, firstname=firstname, password=password)

    db.session.add(user)
    db.session.commit()

    return user


def get_users():
    """Return all users."""

    return User.query.all()


def get_user_by_id(id):
    """Return a user by primary key."""

    return User.query.get(id)


def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()


def add_favorite_tea(tea_id, user_id):
    """Create and return a new favorite."""

    favorite = Favorite(tea_id=tea_id,
                        user_id=user_id)

    db.session.add(favorite)
    db.session.commit()

    return favorite


def get_user_favorite_teas(user_id):
    """ Returns all favorite teas a user favorited. """

    return Favorite.query.filter_by(user_id=user_id).all()


def check_if_tea_in_favorites(tea_id):
    """ Return True if a tea exists in favorites table. """
    return True if Favorite.query.filter_by(tea_id = tea_id).first() else False 
  
  
def remove_favorite_tea(tea_id):
    """ Deletes a favorite tea a user 'unfavorted'. """
    
    favorited_tea = Favorite.query.filter_by(tea_id = tea_id).one()
    db.session.delete(favorited_tea)
    db.session.commit()
    return " "


if __name__ == "__main__":
    from server import app
    print("entered crud.py main")
    connect_to_db(app)



