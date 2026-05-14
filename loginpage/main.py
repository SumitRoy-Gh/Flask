from flask import Flask, request, redirect, url_for, session, Response

app = Flask(__name__)
app.secret_key = "your_secret_key"

# homepage login page
@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "123":

            session["username"] = username
            return redirect(url_for("welcome"))

        else:
            return Response("Invalid credentials", mimetype="text/plain")

    return '''
           <h2>Login Page</h2>

           <form method="post">

           Username:
           <input type="text" name="username"><br>

           Password:
           <input type="password" name="password"><br>

           <input type="submit" value="Login">

           </form>
           '''

# welcome page
@app.route("/welcome")
def welcome():

    if "username" in session:

        return f'''
        <h2>Welcome {session['username']}! This is the dashboard</h2>

        <a href="{url_for('logout')}">Logout</a>
        '''

    else:
        return redirect(url_for("login"))

# logout page
@app.route("/logout")
def logout():

    session.pop("username", None)

    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)