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

    return render_template("homepage.html")


@app.route("/teas")
def all_teas():
    """View all teas."""

    teas = crud.get_teas()

    return render_template("all_teas.html", teas=teas)


@app.route("/teas/<id>")
def show_tea(id):
    """Show details on a particular tea."""

    tea = crud.get_tea_by_id(id)

    return render_template("tea_details.html", tea=tea)



if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
