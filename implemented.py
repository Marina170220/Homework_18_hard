from dao.movie import MovieDAO
from dao.director import DirectorDAO
from dao.genre import GenreDAO
from service.movie import MovieService
from service.director import DirectorService
from service.genre import GenreService
from setup_db import db

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao=movie_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao=director_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao=genre_dao)

