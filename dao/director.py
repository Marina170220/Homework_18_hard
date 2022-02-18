from dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all_directors(self):
        return self.session.query(Director).all()

    def get_one_director(self, dir_id):
        return self.session.query(Director).get(dir_id)


