from flask import Flask, request, redirect, render_template
import cgi


app = Flask(__name__)
app.config['DEBUG']=True
@app.route('/', methods=['POST'])

def error():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    if username == "":
        user.error = "Please input valid username"
        return render_template("index.html", user_error = user_error)

    if len(password) < 3 or len(password) > 20:
        user.error = "Password must be between 3 and 20 characters"
        return render_template("index.html", user_error = user_error)
    
    if password == "":
        user.error = "Passwords must match"
        return render_template("index.html", user_error = user_error)

    if password == "":
        user.error = "Password must contain at least 1 character"
        return render_template("index.html", user_error = user_error)

    else:
        render_template ('welcome.html', username = username)


        #6-20 if statements 
        #else:
            #render_template ('welcome.html'username=username)



