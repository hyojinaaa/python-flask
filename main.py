# need db to import models
from forms import Select_Movie
import models
from flask import Flask, render_template, abort, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'correcthorsebatterystaple'


db = SQLAlchemy(app)

WTF_CSRF_ENABLED = True
WTF_CSRF_SECRET_KEY = 'sup3r_secr3t_passw3rd'


@app.route('/')
def home():
    # return ('<h1 style="color:red";>Hello World</h1>')
    return render_template('home.html', page_title='IT WORKS!')

# list all the movies
@app.route('/all_movies')
def all_movies():
    movies = models.Movie.query.all()
    return render_template('all_movies.html', page_title="ALL MOVIES", movies=movies)

# details of one movie
@app.route('/movie/<int:id>')
def movie(id):
    movie = models.Movie.query.filter_by(id=id).first()
    title = movie.title
    return render_template('movie.html', page_title=title, movie=movie)


@app.route('/choose_movie', methods=['GET', 'POST'])
def choose_movie():
    form = Select_Movie()
    movies = models.Movie.query.all()
    form.movies.choices = [(movie.id, movie.title) for movie in movies]
    if request.method == 'POST':
        if form.validate_on_submit():
            return redirect(url_for('movie', id=form.moviename.data))
        else:
            abort(404)
    return render_template('movies.html', title='Select A Movie', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
