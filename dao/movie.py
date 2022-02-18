from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all_movies(self):
        return self.session.query(Movie).all()

    def get_movies_by_director(self, dir_id):
        return self.session.query(Movie).filter(Movie.director_id == dir_id).all()

    def get_movies_by_genre(self, gen_id):
        return self.session.query(Movie).filter(Movie.genre_id == gen_id).all()

    def get_movies_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year).all()

    def get_one_movie(self, mov_id):
        return self.session.query(Movie).get(mov_id)

    def create_movie(self, data):
        new_movie = Movie(**data)

        self.session.add(new_movie)
        self.session.commit()

        return new_movie

    def update_movie(self, movie):
        self.session.add(movie)
        self.session.commit()

        return movie

    def delete_movie(self, mov_id):
        movie = self.get_one_movie(mov_id)

        self.session.delete(movie)
        self.session.commit()
