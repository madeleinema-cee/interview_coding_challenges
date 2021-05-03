section = {
    'insert': 'insert into section (name, description) values ({}, {})',
    'update': 'update section set name = {}, description = {} where id = {}',
}

item = {
    'insert': 'insert into item (name, price, description) values ({}, {}, {})',
    'update': 'update item set name = {}, price = {},description = {} where id = {}',
}

modifiers = {
    'insert': 'insert into modifiers (description) values ({})',
    'update': 'update modifiers set description = {} where id = {}',
}

section_item = {
    'insert': 'insert into section_item (section_id, item_id) values ({}, {})',
    'update': 'update section_item set section_id = {}, item_id = {} where id = {}',
}

item_modifiers = {
    'insert': 'insert into item_modifiers (modifier_id, item_id) values ({}, {})',
    'update': 'update item_modifiers set item_id = {}, modifier_id = {} where id = {}',
}

get_queries = {
    'get': 'select * from {}',
    'get_by_id': 'select * from {} where id={} ',
}

delete = {
    'delete': 'delete from {} where id={}'
}
