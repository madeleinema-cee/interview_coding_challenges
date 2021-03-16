from helpers.db import Db


class RetrieveCompanyData:
    """Contains all the functions to retrieve the data for
    the django project
    Attributes:
        db (Db): headcount Db instance
        query (str): query instance
    """

    def __init__(self):
        self.db = Db('company_headcount/headcount.db')
        self.query = None

    def main(self):
        """Method to call function sequentially
        Returns:
            self.parse_months(data) (arr): an array of months return by self.parse_months function
            self.parse_company_data(data)（dict): an dict of companies and their monthly headcounts
            returned by self.parse_company_data function
        """
        data = self.retrieve_data()
        return self.parse_months(data), self.parse_company_data(data)

    def retrieve_data(self):
        """Retrieves company data to be preserved
        Returns:
            company data
        """
        self.query = """
        select c.company, h.month, h.headcount from headcount h
        join company_headcount ch on ch.headcount_id = h.id
        join company c on ch.company_id = c.id"""

        results = self.db.fetchall(self.query)
        return results

    def parse_months(self, data):
        """Parse company data
        Arguments:
            data (arr): a array of dictionaries
        Returns:
            months data
        """
        months = []
        for row in data:
            if row['month'] not in months:
                months.append(row['month'])
        return months

    def parse_company_data(self, data):
        """Parse company data
        Arguments:
            data (arr): a array of dictionaries
        Returns:
            company and headcount data
        """
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


