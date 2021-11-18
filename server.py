"""Server for tea app."""

from flask import Flask, render_template, request, flash, session, redirect, jsonify, json
from model import connect_to_db
import crud
from jinja2 import StrictUndefined
import os 
import requests

mapbox = os.environ["mapbox_token"]

yelp = os.environ["yelp_token"]
yelp_url= "https://api.yelp.com/v3/businesses/search"

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route("/mapbox")
def send_mapbox_token():
    return mapbox 

@app.route("/")
def homepage():
    """View homepage."""
    
    # if logged in, then show that 
    teas = crud.get_teas()

    return render_template("homepage.html", teas=teas)


@app.route("/teas")
def all_teas():
    """View all teas."""

    teas = crud.get_teas()

    return render_template("all_teas.html", teas=teas)


@app.route("/teas/<id>")
def show_tea(id):
    """Show details on a particular tea."""

    tea = crud.get_tea_by_id(id)
    teas = crud.get_teas()


    return render_template("tea_details.html", teas=teas, tea=tea)

@app.route("/quiz_result/<id>")
def show_quiz_result(id):
    
    tea = crud.get_tea_by_id(id)    
    data = {
        'id':tea.id,
        'name': tea.name,
        'image': tea.image_url
    }
    return json.dumps(data)

@app.route("/login")
def all_users():
    """View all users."""

    users = crud.get_users()
    teas = crud.get_teas()

    return render_template("login.html", users=users, teas = teas)


@app.route("/register", methods=["POST"])
def register_user():
    """Create a new user."""
    firstname = request.form.get("firstname")
    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if user:
        flash("Cannot create an account with that email. Try again.")
        return redirect("/login")
    else:
        crud.create_user(email, firstname, password)
        flash(f"Account created! Welcome {firstname}.")
        return redirect("/")


@app.route("/users/<id>")
def show_user(id):
    """Show details on a particular user."""

    user = crud.get_user_by_id(id)

    return render_template("user_details.html", user=user)


@app.route("/login", methods=["POST"])
def process_login():
    """Process user login."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if not user or user.password != password:
        flash("The email or password you entered was incorrect.")
    else:
        # Log in user by storing the user's email in session
        session["user_email"] = user.email
        session["firstname"] = user.firstname
        session["user_id"] = user.id
        flash(f"Welcome back, {user.firstname}!")

    return redirect("/")

@app.route("/logout", methods=["POST"])
def process_logout():
    """Logout user."""
    user = session["user_email"]
    if user:
        session.pop("user_email", None)
        session.pop("firstname", None)
        return redirect("/")
    else:
        return redirect("/")
    
# @app.route("/profile")
# def profile_page(): 
        
#     teas = crud.get_teas()

#     return render_template("profile.html", teas=teas)
    
@app.route("/teaquiz")
def tea_quiz(): 
        
    teas = crud.get_teas()

    return render_template("tea_quiz.html", teas=teas)


@app.route("/favorite_action/<tea_id>", methods=["POST"])
def update_favorite(tea_id):
    """Allows user to save a tea to their profile"""
    
    #create a variable represeting user in a session 
    user = session["user_email"]
    
    # Get the tea object 
    tea = crud.get_tea_by_id(tea_id)
    user_id = session["user_id"]
    
    # If current user is logged in
    if user:
        # Get instance of user fav for selected tea
        # user_favs = crud.get_user_favorites(user_id)

        # If user has already saved the tea, remove favorite.
        ## Function from crud will return true/false
        response = crud.check_if_tea_in_favorites(tea_id)
        if response:
            #unfill the user button and remove from session. 
            crud.remove_favorite_tea(tea_id)
            return "Removed tea"
            
        # Otherwise, create new fav for user.
        else:
            user_id = session["user_id"]
            favorite = crud.add_favorite_tea(tea_id, user_id)
            return "Added tea"
    
@app.route("/check_favorites/<tea_id>")
def check_favorite_tea(tea_id):
    """Check if user saved tea to profile"""
    response = crud.check_if_tea_in_favorites(tea_id)
    if response == True: 
        return json.dumps(True)
    else: 
        return json.dumps(False)
        
@app.route("/profile")
def show_user_profile():
    user_email = session["user_email"]
    user = crud.get_user_by_email(user_email)
    teas = crud.get_teas()
    user_id = session["user_id"]

    favorite_teas = crud.get_user_favorite_teas(user_id)
    print(favorite_teas)
    
    return render_template("profile.html", user=user, favorite_teas=favorite_teas, teas=teas)

@app.route("/search")
def render_search_page():
    teas = crud.get_teas()
    
    return render_template("search.html", teas=teas)

def yelp_api_search(zipcode):

    headers = {'Authorization': 'Bearer '+ yelp}
    parameters = {'location': zipcode,
               'term': 'tea', 
               'limit': 12}
    response = requests.get(yelp_url,
                                    params=parameters,
                                    headers=headers)
    
    data = response.json()

    return data



@app.route('/process_search', methods = ["POST"])
def processing_search():
    """User submits zipcode to be search for tea cafe"""

    teas = crud.get_teas()
    zipcode = request.form.get("zipcode")
    data = yelp_api_search(zipcode) 

    business = data['businesses']    

    return render_template("tea_cafe.html", businesses=business, teas=teas)



if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
