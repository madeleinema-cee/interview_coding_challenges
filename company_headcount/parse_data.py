import sqlite3


class Db:
    def __init__(self, database):
        self.conn = sqlite3.connect(database)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def execute(self, query, project):
        self.cursor.execute(query, project)
        self.conn.commit()

    def fetchall(self, query):
        self.cursor.execute(query)
        self.conn.commit()
        result = [dict(row) for row in self.cursor.fetchall()]
        return result

    def close(self):
        self.conn.close()

    def create_tables(self):
        query = """
        create table headcount
        (id integer primary key, company, month, headcount)
        """
        self.cursor.execute(query)

    def insert_data_from_csv(self):
        companies = []
        with open('sample_headcount.csv', 'r') as file:
            next(file)
            for line in file:
                line = line.strip().split(',')
                month = line[1]
                company = line[0]
                headcount = line[2]
                companies.append(company)
                query = f'insert into headcount(company, month, headcount) values (?, ?, ?)'
                project = (company, month, headcount)
                self.execute(query=query, project=project)


#
# db = Data('company_headcount/db.sqlite3')
# db.create_tables()
# db.insert_data_from_csv()
