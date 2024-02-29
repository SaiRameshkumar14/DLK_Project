from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from __init__ import create_app, db

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home') 
def index():
    return render_template('home.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

app = create_app()
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

# Folder prject name
    # ├── __init__.py # setup your app
    # ├── main.py   # the non-auth routes for your app
    # ├── auth.py   # the auth routes for your app
    # ├── models.py # your user model
    # ├── db.sqlite # your database
    # └── templates
    #     ├── base.html     # contains common layout and links
    #     ├── index.html    # show the home page
    #     ├── login.html    # show the login form
    #     ├── profile.html  # show the profile page
    #     └── signup.html   # show the signup form 
