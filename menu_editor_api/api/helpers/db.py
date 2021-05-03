import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('api/menu.db', check_same_thread=False)
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

#     def main(self):
#         self.create_tables()
#
#     def create_tables(self):
#         section_query = """
#         create table section
#         (id integer primary key, title);
#         insert into section (title) values ('Lunch Specials'), ('Daily Specials'), ('Salads')
#         """
#         section_insert = """
#         insert into section (title) values ('Lunch Specials'), ('Daily Specials'), ('Salads')
#         """
#         self.execute(section_query)
#         self.execute(section_insert)
#
#         # item_query = """
#         # create table item(id integer primary key, name, description, price);
#         # insert into item (name, description, price) values ('Cheese Pizza', 'pizza', 5), ('Chicken Sandwich', 'sandwich', 6)
#         # """
#         # self.execute(item_query)
#         #
#         # modifiers_query = """
#         # create table modifiers
#         # (id integer primary key, title)
#         # insert into section (title) values ('Extra Spicy'), ('No spice')
#         # """
#         # self.execute(modifiers_query)
# #         create table section_item
# #         (id integer PRIMARY key, section_id, item_id,
# #         FOREIGN key (section_id) REFERENCES section(id),
# #         FOREIGN key (item_id) REFERENCES item(id))
# # create table item_modifiers(id integer PRIMARY key, item_id, modifier_id,FOREIGN key (modifier_id) REFERENCES modifiers(id),FOREIGN key (item_id) REFERENCES item(id))

