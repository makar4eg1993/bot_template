import pymysql
from db.config import host, port, user, password, db_name


class Connection:

    def __init__(self):
        self.con = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            db=db_name,
            autocommit=True,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cur = self.con.cursor()
        print(self.cur)

    def _connect(self):
        self.cur = self.con.cursor()
        print(self.cur)

    def _select(self, sql, args=None):
        self.cur.execute(sql, args)
        self.sel = self.cur.fetchone()
        self.cur.close()
        self.con.close()
        return self.sel

    def _selectAll(self, sql, args=None):
        self.cur.execute(sql, args)
        self.sel = self.cur.fetchall()
        print(self.sel)

        self.cur.close()
        print('закрыл курсор')
        self.con.close()
        return self.sel

    def _insert(self, sql, args=None):
        self.ins = self.cur.executemany(sql, args)
        return self.ins

    def _update(self, sql, args=None):
        self.upd = self.cur.executemany(sql, args)
        return self.upd

    def _delete(self, sql, args=None):
        self.delete = self.cur.executemany(sql, args)
        return self.delete

# test = Connection()
# print(test._selectAll(sql='SELECT * FROM `users` WHERE 1'))
