import argparse
import csv

from db import Db


class GenerateDatabase:
    """Contains all queries to create headcount database
    and insert data
    Arguments:
        db.path (str): database path
        db (Db): Db instance
        input_file (str):csv path
    """

    def __init__(self, input_file):
        self.db_path = 'company_headcount/headcount.db'
        self.db = Db(self.db_path)
        self.input_file = input_file

    def main(self):
        """Function to call class methods sequentially
        """
        self.create_company_table()
        self.create_headcount_table()
        self.create_company_headcount_table()
        self.insert_data_from_csv()
        self.insert_data_to_connect_table()

    def create_company_table(self):
        """Create company table
        """
        query = """
        create table company
        (id integer primary key, company)
        """
        self.db.execute(query)

    def create_headcount_table(self):
        """Create headcount table
        """
        query = """
        create table headcount
        (id integer primary key, month, headcount)
        """
        self.db.execute(query)

    def create_company_headcount_table(self):
        """Create company_headcount connection table
                """
        query = """
        create table company_headcount 
        (id integer PRIMARY key, company_id, headcount_id, 
        FOREIGN key (company_id) REFERENCES company(id),
        FOREIGN key (headcount_id) REFERENCES headcount(id))
        """
        self.db.execute(query)

    def insert_company(self, company):
        """Insert data to company table
        Arguments:
            company (str): company name
        """
        query = f'''
        insert into company (company)
        values ('{company}')
        '''
        self.db.execute(query)

    def insert_headcount(self, month, headcount):
        """Insert data to comapny table
        Arguments:
            headcount (str): company headcount
        """
        query = f'''
        insert into headcount (month, headcount)
        values ('{month}', '{headcount}')
        '''
        self.db.execute(query)

    def insert_company_headcount(self, company, headcount):
        """Insert data to company_headcount table
        Arguments:
            company (str): company name
            headcount (str): company headcount
        """
        query = f'''
        insert into company_headcount(company_id, headcount_id) VALUES
        ((select id from company where company is "{company}"),
        (select id from headcount where headcount is "{headcount}"))
        '''
        self.db.execute(query)

    def insert_data_from_csv(self):
        """Method to read csv file and call insert data functions
        """
        companies = []
        with open(self.input_file, 'r') as file:
            next(file)
            reader = csv.reader(file)

            for line in reader:
                company = line[0]
                month = line[1]
                headcount = line[2]

                self.insert_headcount(month, headcount)

                if company not in companies:
                    companies.append(company)
                    self.insert_company(company)

    def insert_data_to_connect_table(self):
        """Method to read csv file and call insert data to company_headcount function
        """
        with open(self.input_file, 'r') as file:
            next(file)
            for line in file:
                line = line.strip().split(',')
                company = line[0]
                headcount = line[2]

                self.insert_company_headcount(company, headcount)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', type=str)
    args = parser.parse_args()
    g = GenerateDatabase(args.input_file)
    g.main()
