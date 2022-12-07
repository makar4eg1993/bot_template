from db.model.model import Connection


class Users(Connection):
    def get_all_users(self):
        return self._selectAll(sql='SELECT * FROM `users` WHERE 1')

