"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session, redirect, url_for)
from flask_login import LoginManager, current_user, logout_user, login_required
from model import connect_to_db, db, User, Movie, Rating
import crud

from jinja2 import StrictUndefined

# login_manager = LoginManager()

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')


@app.route('/movies')
def all_movies():
    """View all movies."""

    movies = crud.get_movies()

    return render_template("all_movies.html", movies=movies)


@app.route('/movies/<movie_id>')
def show_movie(movie_id):
    """Show details on a particular movie."""

    movie = crud.get_movie_by_id(movie_id)

    return render_template("movie_details.html", movie=movie)


@app. route('/users')
def all_users():
    """View all users."""

    users = crud.get_users()

    return render_template('all_users.html', users = users)

@app.route('/users/<user_id>')
def show_user(user_id):
    """Show user with ID."""

    user = crud.get_user_by_id(user_id)

    return render_template('user_details.html', user = user)


@app.route('/users', methods=['POST'])
def register_user():
    """Create a new user"""
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)

    if user:
        flash('Sorry, that email already exists. Try a different one.')
    else:
        user + crud.create_user(email, password)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully! You can now login!')
    return redirect('/')

#Create login and update the rating and create a new rating for a movie


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
 