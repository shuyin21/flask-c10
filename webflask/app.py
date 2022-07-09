from flask import Flask, render_template, request, url_for, redirect, abort, Response
import sqlite3 as sql

app = Flask(__name__)
# hompage route

# create a function to handle db connection


#  create a function to handle db connection

def musicDbCon():
    # conn variable = sql.connectFunction(path/filename.ext)
    conn = sql.connect("Part12 Flask/webflask/c10Sqlite.db")
    # row_factory  is used to manipulate/access the db
    conn.row_factory = sql.Row
    return conn


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title='Home')


# set the routes for the songs.html
# set the routes for the songs.html

@app.route("/songs")
def songs():

    # read song data from the database
    songConn = musicDbCon()
    cursor = songConn.cursor()
    cursor.execute("SELECT * FROM songs")
    getSongs = cursor.fetchall()
    # returns the songs page in the browser when the songs text/link is clicked on the menu
    return render_template("songs.html", title="Songs", songsInDB=getSongs)
# set the routes for the contact.html

# Delete song by songID


@app.route("/<int:songID>/delete", methods=("POST",))
def delete(songID):
    songConn = musicDbCon()
    cursor = songConn.cursor()
    cursor.execute("DELETE FROM songs WHERE songID =?", (songID,))
    songConn.commit()
    songConn.close()
    return redirect(url_for("songs"))  # redirect to songs page after delete


"Create a function to get a specific song"


def getSong(recordID):
    songConn = musicDbCon()
    cursor = songConn.cursor()
    #
    aSong = cursor.execute(
        "SELECT * FROM songs WHERE songID =?", (recordID,)).fetchone()
    songConn.close()

    if aSong is None:
        abort(Response(f"No record {aSong} was found in DB"))
    return aSong


"Update a song"


@app.route("/<int:songID>/update", methods=("GET", "POST",))
def update(songID):
    aSongRecord = getSong(songID)
    if request.method == "POST":
        title = request.form["Title"]
        artist = request.form["Artist"]
        genre = request.form["Genre"]

        songConn = musicDbCon()
        cursor = songConn.cursor()
        cursor.execute("UPDATE songs SET title = ?, artist = ?, genre = ?" "WHERE songID= ?",
                       (title, artist, genre, songID),)
        songConn.commit()
        songConn.close()
        # redirect to songs page after delete
        return redirect(url_for("songs"))
    return render_template("updatesongs.html", title="Update Songs", SongRecord=aSongRecord)


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

# set the routes for the addsongs.html

@app.route("/addsongs.html", methods=["GET", "POST"])
def addsongs():

    if request.method == "POST":

        title = request.form["Title"]

        artist = request.form["Artist"]

        genre = request.form["Genre"]

        songConn = musicDbCon()

        cursor = songConn.cursor()

        songID = cursor.lastrowid

        cursor.execute(

            "INSERT INTO songs VALUES(?,?,?,?)", (songID, title, artist, genre)

        )

        songConn.commit()

        songConn.close()

        return redirect(

            url_for("songs")

        )  # redirect back to the songs page after adding a song

    return render_template("addsongs.html", title="Add Songs")


# invoke /call the main class
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3500)
