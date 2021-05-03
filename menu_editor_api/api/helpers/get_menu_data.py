from api.helpers.db import Database


class GetMenuData:
    def __init__(self):
        self.db = Database()

    def retrieve_menu_data(self):
        query = '''SELECT s.id, s.name as section_name, i.id as item_id, i.name as item_name, price, 
        i.description, m.id as modifier_id, m.description as modifier from item i
        join section_item si on si.item_id = i.id
        join section s on si.section_id = s.id
        join item_modifiers im on im.item_id = i.id
        JOIN modifiers m on im.modifier_id = m.id'''
        
        results = self.db.fetchall(query)
        return results

    def parse_menu_data(self):
        menu = {}

        for result in self.retrieve_menu_data():
            menu_id = result['id']

            if menu_id not in menu:
                menu[menu_id] = {
                    'id': menu_id,
                    'title': result['section_name'],
                    'items': [
                        {
                            'id': result['item_id'],
                            'title': result['item_name'],
                            'modifiers': [
                                {
                                    'id': result['modifier_id'],
                                    'title': result['modifier']
                                }
                            ]
                        }
                    ]
                }

            else:
                item_ids = []
                for item in menu[menu_id]['items']:
                    item_id = item['id']
                    item_ids.append(item_id)
                if result['item_id'] not in item_ids:
                    parsed_item = {
                        'id': result['item_id'],
                        'title': result['item_name'],
                        'modifiers': [
                            {
                                'id': result['modifier_id'],
                                'title': result['modifier']
                            }
                        ]
                    }
                    menu[menu_id]['items'].append(parsed_item)

                else:

                    for item in menu[menu_id]['items']:
                        modifier_ids = []
                        for modifier in item['modifiers']:
                            modifier_id = modifier['id']
                            modifier_ids.append(modifier_id)
                        print(modifier_ids)
                        if result['modifier_id'] not in modifier_ids:
                            parsed_modifier = {
                                'id': result['modifier_id'],
                                'title': result['modifier']
                            }
                            item['modifiers'].append(parsed_modifier)

        return list(menu.values())




