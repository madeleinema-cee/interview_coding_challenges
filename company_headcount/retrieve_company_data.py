from helpers.db import Db


class RetrieveCompanyData:
    def __init__(self):
        self.db = Db('company_headcount/headcount.db')

    def main(self):
        data = self.retrieve_data()
        return self.parse_months(data), self.parse_company_data(data)

    def retrieve_data(self):
        self.query = """
        select c.company, h.month, h.headcount from headcount h
        join company_headcount ch on ch.headcount_id = h.id
        join company c on ch.company_id = c.id"""

        results = self.db.fetchall(self.query)
        return results

    def parse_months(self, data):
        months = []
        for row in data:
            if row['month'] not in months:
                months.append(row['month'])
        return months

    def parse_company_data(self, data):
        company_data = {}
        for row in data:
            company = row['company'].capitalize()
            if company not in company_data:
                company_data[company] = {
                    'headcount': [row['headcount']]
                }
            else:
                if row['headcount'] not in company_data[company]['headcount']:
                    company_data[company]['headcount'].append(row['headcount'])
        return company_data


