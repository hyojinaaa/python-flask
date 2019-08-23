from main import db


class Movie(db.Model):
    __tablename__ = 'Movie'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    year = db.Column(db.Integer)
    description = db.Column(db.String())
    actors = db.relationship('Role', back_populates='movie')


class Actor(db.Model):
    __tablename__ = 'Actor'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    birthdate = db.Column(db.String(30))
    movies = db.relationship('Role', back_populates='actor')

    def __str__(self):
        return self.name


class Role(db.Model):
    __tablename__ = 'Role'

    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('Movie.id'), nullable=False)
    actor_id = db.Column(db.Integer, db.ForeignKey('Actor.id'), nullable=False)
    role = db.Column(db.String(80), nullable=False)
    actor = db.relationship('Actor', back_populates='movies')
    movie = db.relationship('Movie', back_populates='actors')
