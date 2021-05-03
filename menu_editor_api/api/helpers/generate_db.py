from api.helpers.db import Database


class GenerateMenuDatabase:
    def __init__(self):
        self.db = Database()

    def main(self):
        self.create_section_table()
        self.create_item_table()
        self.create_modifiers_table()
        self.create_section_item_table()
        self.create_item_modifiers_table()

    def create_section_table(self):
        create_section_query = '''create table section
        (id integer primary key, name text, description text);
        '''
        self.db.execute(create_section_query)

    def create_item_table(self):
        create_item_query = '''create table item
        (id integer primary key, name text, description text, price text);
        '''
        self.db.execute(create_item_query)

    def create_modifiers_table(self):
        create_modifiers_query = '''create table modifiers
        (id integer primary key, description text);
        '''
        self.db.execute(create_modifiers_query)

    def create_section_item_table(self):
        create_section_item_query = '''create table section_item
        (id integer primary key, section_id integer, item_id integer, FOREIGN key (section_id) REFERENCES section(id),
        FOREIGN key (item_id) REFERENCES item(id));
        '''
        self.db.execute(create_section_item_query)

    def create_item_modifiers_table(self):
        create_item_modifiers_query = '''create table item_modifiers
        (id integer PRIMARY key, item_id integer, modifier_id integer, FOREIGN key (modifier_id) REFERENCES modifiers(id),
        FOREIGN key (item_id) REFERENCES item(id));
        '''
        self.db.execute(create_item_modifiers_query)


if __name__ == '__main__':
    generate_database = GenerateMenuDatabase()
    generate_database.main()

#    def main(self):
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
