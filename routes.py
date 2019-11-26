from flask import Flask, render_template, url_for, flash, redirect
from app import app,db,bcrypt
from app.forms import RegistrationForm, LoginForm
from app.modules import Post,User

posts = [
    {
        "author": "Kastriot Blakaj",
        "title": "Flask book",
        "content": "First post",
        "date_posted": "2021"
    },
    {
        "author": "Dren Blakaj",
        "title": "Laravel book",
        "content": "Second post",
        "date_posted": "2020"
    }, {
        "author": "Dren Blakaj",
        "title": "Laravel book",
        "content": "Second post",
        "date_posted": "2020"
    }, {
        "author": "Kastriot Blakaj",
        "title": "Flask book",
        "content": "First post",
        "date_posted": "2021"
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts, title="Home")


@app.route("/about")
def about():
    return render_template("about.html", title='About', posts=posts)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Your account has been created", 'success')
        return redirect(url_for('login'))
    return render_template("register.html", title="Register", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in ', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful, Please check your Username or Password ', 'Danger')
    return render_template("login.html", title="Login", form=form)
