"""Server for tea app."""

from flask import Flask, render_template, request, flash, session, redirect, jsonify, json
from model import connect_to_db
import crud
from jinja2 import StrictUndefined
import os 
import requests

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

mapbox = os.environ["mapbox_token"]

yelp = os.environ["yelp_token"]
yelp_url= "https://api.yelp.com/v3/businesses/search"


@app.route("/mapbox")
def send_mapbox_token():
    "Sends hidden token."
    
    return mapbox 


@app.route("/search")
def render_search_page():
    "Displays search page to search for tea cafes."
    
    teas = crud.get_teas()
    
    return render_template("search.html", teas=teas)


def yelp_api_search(zipcode):
    "Queries Yelp API, displays information on tea cafes."
    
    #create a dictionary to send information along with our request to authenticate ourselves 
    headers = {'Authorization': 'Bearer '+ yelp}
    #defines the parameters for our search 
    parameters = {'location': zipcode,
               'term': 'tea', 
               'limit': 12}
    response = requests.get(yelp_url,
                                    params=parameters,
                                    headers=headers)
    #convert the JSON string to a dictionary and store the result into a variable 
    data = response.json()

    return data


@app.route('/process_search', methods = ["POST"])
def processing_search():
    """User submits zipcode to search for tea cafe"""

    teas = crud.get_teas()
    #store information from form in a variable called zipcode 
    zipcode = request.form.get("zipcode")
    #pass zipcode into yelp_api_search function to query for cafes
    data = yelp_api_search(zipcode) 
    business = data['businesses']  

    return render_template("tea_cafe.html", businesses=business, teas=teas)


@app.route("/")
def homepage():
    """View homepage."""
    
    teas = crud.get_teas()

    return render_template("homepage.html", teas=teas)


@app.route("/login")
def display_login():
    """View user login and registration."""

    users = crud.get_users()
    teas = crud.get_teas()

    return render_template("login.html", users=users, teas=teas)


@app.route("/login", methods=["POST"])
def process_login():
    """Processes user login."""
    
    # Returns email entered in login form 
    email = request.form.get("email")
    # Returns password entered in login form
    password = request.form.get("password")
    user = crud.get_user_by_email(email)
    if not user or user.password != password:
        flash("The email or password you entered was incorrect.")
    else:
        session["user_email"] = user.email
        session["firstname"] = user.firstname
        session["user_id"] = user.id
        flash(f"Welcome back, {user.firstname}!")

    return redirect("/")


@app.route("/register", methods=["POST"])
def register_user():
    """Creates a new user."""
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


@app.route("/profile")
def show_user_profile():
    "Displays users profile page."
    user_email = session["user_email"]
    user = crud.get_user_by_email(user_email)
    teas = crud.get_teas()
    user_id = session["user_id"]

    favorite_teas = crud.get_user_favorite_teas(user_id)
    print(favorite_teas)
    
    return render_template("profile.html", user=user, favorite_teas=favorite_teas, teas=teas)


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
        # If user has already saved the tea, remove favorite.
        # Function from crud will return true/false
        response = crud.check_if_tea_in_favorites(tea_id)
        if response:
            # unfill the fav button and remove from session. 
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
    
        
@app.route("/quiz_result/<id>")
def show_quiz_result(id):
    
    tea = crud.get_tea_by_id(id)    
    data = {
        'id':tea.id,
        'name': tea.name,
        'image': tea.image_url
    }
    return json.dumps(data)

    
@app.route("/teaquiz")
def tea_quiz(): 
        
    teas = crud.get_teas()

    return render_template("tea_quiz.html", teas=teas)


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
