from flask_restx import Namespace, Resource

from dao.model.genre import GenreSchema

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = genre_dao.get_all_genres()
        if genres:
            return genres_schema.dump(genres), 200
        return "", 404


@genre_ns.route('/<int:gen_id>')
class GenreView(Resource):
    def get(self, gen_id: int):
        try:
            genre = genre_dao.get_one_genre(gen_id)
            return genre_schema.dump(genre), 200
        except Exception:
            return "", 404

