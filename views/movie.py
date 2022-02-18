from flask import request
from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        dir_id = request.args.get('director_id')
        gen_id = request.args.get('genre_id')
        year = request.args.get('year')
        if dir_id:
            movies = movie_service.get_movies_by_director(dir_id)
        elif gen_id:
            movies = movie_service.get_movies_by_genre(gen_id)
        elif year:
            movies = movie_service.get_movies_by_year(year)
        else:
            movies = movie_service.get_all_movies()
        if movies:
            return movies_schema.dump(movies), 200
        return "", 404

    def post(self):
        req_json = request.json
        movie_service.create_movie(req_json)

        return "", 201


@movie_ns.route('/<int:mov_id>')
class MovieView(Resource):
    def get(self, mov_id: int):
        try:
            movie = movie_service.get_one_movie(mov_id)
            return movie_schema.dump(movie), 200
        except Exception:
            return "", 404

    def put(self, mov_id: int):
        req_json = request.json
        req_json['id'] = mov_id
        movie = movie_service.update_movie(req_json)
        if movie:
            return "", 200
        return "", 404

    def delete(self, mov_id: int):
        movie_service.delete_movie(mov_id)
        return "", 204

