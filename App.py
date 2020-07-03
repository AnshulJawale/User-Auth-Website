from flask import Flask, redirect, url_for, render_template, request, session

#* url_for gives the url for a particular function
#todo Route the app to a url -> Define function that returns a valid html -> Run the App

app = Flask(__name__)                   #? An App with same name as filename.

@app.route("/")                         #* Url mapping
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["name"]
        return redirect(url_for("user", username=username))
    else:
        return render_template("login.html")

@app.route("/<username>")
def user(username):
    return f"<h1>{username}</h1>"

if __name__ == "__main__":
    app.run(debug=True)