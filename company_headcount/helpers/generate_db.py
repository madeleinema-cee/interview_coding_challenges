import argparse
import csv
import os

from db import Db


class GenerateDatabase:
    def __init__(self, input_file):
        self.db_path = 'company_headcount/headcount.db'
        self.db = Db(self.db_path)
        self.input_file = input_file

    def main(self):
        self.create_company_table()
        self.create_headcount_table()
        self.create_company_headcount_table()
        self.insert_data_from_csv()
        self.insert_data_to_connect_table()

    def create_company_table(self):
        query = """
        create table company
        (id integer primary key, company)
        """
        self.db.execute(query)

    def create_headcount_table(self):
        query = """
        create table headcount
        (id integer primary key, month, headcount)
        """
        self.db.execute(query)

    def create_company_headcount_table(self):
        query = """
        create table company_headcount 
        (id integer PRIMARY key, company_id, headcount_id, 
        FOREIGN key (company_id) REFERENCES company(id),
        FOREIGN key (headcount_id) REFERENCES headcount(id))
        """
        self.db.execute(query)

    def insert_headcount(self, month, headcount):
        query = f'''
        insert into headcount (month, headcount)
        values ('{month}', '{headcount}')
        '''
        self.db.execute(query)

    def insert_company(self, company):
        query = f'''
        insert into company (company)
        values ('{company}')
        '''
        self.db.execute(query)

    def insert_company_headcount(self, company, headcount):
        query = f'''
        insert into company_headcount(company_id, headcount_id) VALUES
        ((select id from company where company is "{company}"),
        (select id from headcount where headcount is "{headcount}"))
        '''
        self.db.execute(query)

    def insert_data_from_csv(self):
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