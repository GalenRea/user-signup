
from flask import Flask, request, redirect, render_template
import cgi
import os

#template_dir = os.path.join(os.path.dirname(__file__), 'templates')
#jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route ('/', methods=['GET'])
def display_signup_form():
    #username = request.args['username']
    #password = request.args['password']
    #verify = request.args['verify']
    #email = request.args['email']
    return render_template("index.html")
    

    #username_error=''
    #password_error=''
    #verify_error=''
    #email_error=''

@app.route ('/', methods=['POST'])
def validate():
    username_error=''
    password_error=''
    verify_error=''
    email_error=''
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    if username == "":
        username_error='Enter a valid username'

    if len(password) < 3 or len(password) > 20:
        password_error = "Password must be between 3 and 20 characters"
    
    if password != verify:
       verify_error = "Passwords must match"
    
    for letter in password:
        if letter.isalpha() == False:
            password_error = "Passwords must contain alphanumeric characters only"
    
    if email == "":
        email_error = "Please enter a valid email"

    for letter in email:
        if letter == ' ':
            email_error = "Email may not contain spaces"
            
    if email.count('@', 0, 40) != 1: 
        email_error = "Email may only contain '@' once"
    
    if email.count('.', 0, 40) != 1: 
        email_error = "Email may only contain one period"

    if len(email) < 3 or len(email) > 20:
        email_error = "Email must be between 3 and 20 characters"

    if password_error != '' or username_error != '' or verify_error != '' or email_error != '':
        return render_template("index.html", username_error = username_error, password_error = password_error, 
        verify_error = verify_error, email_error = email_error)

    else:
        return redirect('/welcome?username=' + username)
    

@app.route ('/welcome/', methods=['GET', 'POST'])
def welcome():
    username = request.args.get('username')
    
    return render_template('welcome.html', username = username)




#@app.route('/signup')
#app.config['DEBUG']=True



#def error():
    

app.run()