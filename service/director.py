from dao.director import DirectorDAO

class DirectorService:

    def __init__(self, director_dao: DirectorDAO):
        self.director_dao = director_dao

    def get_all_directors(self):
        return self.director_dao.get_all_directors()

    def get_one_director(self, dir_id):
        return self.director_dao.get_one_director(dir_id)

