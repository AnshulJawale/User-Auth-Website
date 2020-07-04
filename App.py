from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
import sqlalchemy

#* session --> Used for dynamic pages
#* flash --> Used for flashing messages

#todo Route the app to a url -> Define function that returns a valid html -> Run the App

# App configurations
app = Flask(__name__)                   #? An App with same name as filename.
app.secret_key = "Anshul123"            #! Returns an error if secret key does not exist for a session
app.permanent_session_lifetime = timedelta(hours=5)   #? Ends session after 5 dayss

# App URLS
@app.route("/")                         #* Url mapping
def HomePage():
    return render_template("base.html")

@app.route("/login", methods=["GET", "POST"])
def LoginPage():
    if request.method == "POST":
        user = request.form["name"]
        email = request.form["email"]
        if len(user) <= 3:
            flash("Your username needs to have more than 3 characters")
            return redirect(url_for("LoginPage"))
        else:
            session.permanent = True
            session["user"] = user
            session["email"] = email
            flash("Login Successful")
            return redirect(url_for("IndexPage"))
    else:
        if "user" in session:
            flash("Already Logged in")
            return redirect(url_for("IndexPage"))
        else:
            return render_template("login.html")

@app.route("/logout")
def LogoutPage():
    session.pop("user", None)                           #? Ends the session
    session.pop("email", None)
    flash("You have been Logged Out. Log back in", "info")
    return redirect(url_for("LoginPage"))

@app.route("/user")
def IndexPage():
    if "user" in session:
        user = session["user"]
        return render_template("index.html", user=user)
    else:
        flash("Login to continue")
        return redirect(url_for("LoginPage"))
    
# Running the server
if __name__ == "__main__":
    app.run(debug=True)

