from flask import Flask
from flask_restx import Api

import data
from config import Config
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from setup_db import db

from views.director import director_ns
from views.genre import genre_ns
from views.movie import movie_ns


def create_app(config: Config):
    """
    создание основного объекта application
    """
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()
    register_extensions(application)
    return application


def register_extensions(app):
    """
    подключение конфигурации приложения
    """
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    create_data(app, db)


def create_data(app, db):
    """
    наполнение таблиц данными
    """
    with app.app_context():
        db.create_all()

        for movie in data.movies:
            new_movie = Movie(
                id=movie["pk"],
                title=movie["title"],
                description=movie["description"],
                trailer=movie["trailer"],
                year=movie["year"],
                rating=movie["rating"],
                genre_id=movie["genre_id"],
                director_id=movie["director_id"],
            )
            with db.session.begin():
                db.session.add(new_movie)

        for director in data.directors:
            new_director = Director(
                id=director["pk"],
                name=director["name"],
            )
            with db.session.begin():
                db.session.add(new_director)

        for genre in data.genres:
            new_genre = Genre(
                id=genre["pk"],
                name=genre["name"],
            )
            with db.session.begin():
                db.session.add(new_genre)


if __name__ == '__main__':
    config = Config()
    app = create_app(config)
    register_extensions(app)
    create_data(app, db)
    app.debug = True
    app.run(host="localhost", port=10001)
