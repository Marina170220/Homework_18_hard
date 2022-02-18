from dao.genre import GenreDAO

class GenreService:

    def __init__(self, genre_dao: GenreDAO):
        self.genre_dao = genre_dao

    def get_all_genres(self):
        return self.genre_dao.get_all_genres()

    def get_one_genre(self, gen_id):
        return self.genre_dao.get_one_genre(gen_id)
