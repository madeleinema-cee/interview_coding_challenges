import sqlite3


class Db:
    def __init__(self, database):
        self.conn = sqlite3.connect(database)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def execute(self, query):
        self.cursor.execute(query)
        self.conn.commit()

    def fetchall(self, query):
        self.cursor.execute(query)
        self.conn.commit()
        result = [dict(row) for row in self.cursor.fetchall()]
        return result

    def close(self):
        self.conn.close()

    def main(self):
        self.create_user_table()
        self.create_title_table()
        self.create_user_title_table()
        self.create_company_table()
        self.create_industry_table()
        self.create_company_industry_table()
        # self.insert_data_from_csv()

    def create_user_table(self):
        query = """
        create table user
        (id integer primary key, user_id)
        """
        self.execute(query)

    def create_title_table(self):
        query = """
        create table title
        (id integer primary key, title)
        """
        self.execute(query)

    def create_user_title_table(self):
        query = """
        create table user_title
        (id integer primary key, user_id integer, title_id integer , location, company_id integer, description, start_date, end_date,
        foreign key (user_id) references user (id),
        foreign key (title_id) references title (id),
        foreign key (company_id) references company (id))
        """
        self.execute(query)

    def create_company_table(self):
        query = """
        create table company
        (id integer primary key, company)
        """
        self.execute(query)

    def create_industry_table(self):
        query = """
        create table location
        (id integer primary key, location)
        """
        self.execute(query)

    def create_company_industry_table(self):
        query = """
        create table company_industry
        (id integer primary key, company_id, industry_id,
         foreign key (company_id) references company (id),
         foreign key (industry_id) references industry (id))
        """
        self.execute(query)

    def insert_user_data_from_csv(self):
        pass


db = Db('raw_position.db')
db.main()
