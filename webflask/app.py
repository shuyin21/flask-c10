from flask import Flask, render_template, request, url_for, redirect, abort, Response
import sqlite3 as sql

app = Flask(__name__)
# hompage route


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title='Home')


# set the routes for the songs.html
@app.route("/songs")
def songs():

    # returns the songs page in the browser whent the songs text/link is clicked on the menu
    return render_template("songs.html", title="Songs")


# set the routes for the contact.html

@app.route("/contact")
def contact():

    # returns the contact page in the browser when the Contact text/link is clicked on the menu

    return render_template("contact.html", title="Contact")

    # set the routes for the about.html


@app.route("/about")
def about():

    # returns the about page in the browser when the about text/link is clicked on the menu

    return render_template("about.html", title="About")


# set the routes for the addsongs.html

@app.route("/addsongs")
def addsongs():

    # returns the addsongs page in the browser when the addsongs text/link is clicked on the menu

    return render_template("addsongs.html", title="Add Songs")


# invoke /call the main class
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3500)
