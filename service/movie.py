# здесь бизнес логика, в виде классов или методов. сюда импортируются DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.

from dao.movie import MovieDAO


class MovieService:

    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_all_movies(self):
        return self.movie_dao.get_all_movies()

    def get_movies_by_director(self, dir_id):
        return self.movie_dao.get_movies_by_director(dir_id)

    def get_movies_by_genre(self, gen_id):
        return self.movie_dao.get_movies_by_genre(gen_id)

    def get_movies_by_year(self, year):
        return self.movie_dao.get_movies_by_year(year)

    def get_one_movie(self, mov_id):
        return self.movie_dao.get_one_movie(mov_id)

    def create_movie(self, data):
        return self.movie_dao.create_movie(data)

    def update_movie(self, data):
        mov_id = data.get('id')
        movie = self.get_one_movie(mov_id)

        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')
        movie.genre_id = data.get('genre_id')
        movie.director_id = data.get('director_id')

        self.movie_dao.update_movie(movie)

    def delete_movie(self, mov_id):
        return self.movie_dao.delete_movie(mov_id)
