from parse_data import Db


class GetDataForPlot:
    def __init__(self):
        self.db = Db('db.sqlite3')
        self.query = 'select * from headcount'
        self.results = self.db.fetchall(self.query)

    def get_months(self):
        months = []
        for row in self.results:
            if row['month'] not in months:
                months.append(row['month'])
        return months

    def get_data(self):
        data = {}
        for row in self.results:
            company = row['company'].capitalize()
            if company not in data:
                data[company] = {
                    'headcount': [row['headcount']]
                }
            else:
                if row['headcount'] not in data[company]['headcount']:
                    data[company]['headcount'].append(row['headcount'])
        return data


