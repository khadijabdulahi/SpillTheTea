"""Server for tea app."""

from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


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
    
@app.route("/profile")
def profile_page(): 
        
    teas = crud.get_teas()

    return render_template("profile.html", teas=teas)
    
@app.route("/teaquiz")
def tea_quiz(): 
        
    teas = crud.get_teas()

    return render_template("tea_quiz.html", teas=teas)



if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
