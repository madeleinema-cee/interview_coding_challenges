from flask import jsonify, request
from api import app
from api.helpers.db import Database
from api.helpers.get_menu_data import GetMenuData
from api.helpers.sql_queries import section, item, modifiers, section_item, item_modifiers, get_queries, delete
from api.helpers.utils import validate_params_exist


db = Database()


@app.route('/', methods=['GET'])
def home():
    return '<h1>Menu Builder API</h1>'


@app.route('/api/menu', methods=['GET'])
def get_menu():
    get_menu_data = GetMenuData()
    menu = get_menu_data.parse_menu_data()
    return jsonify(menu)


@app.route('/api/menu/create', methods=['GET', 'POST'])
def create_entity():
    if 'entity' in request.args:
        entity = request.args['entity']

        if entity == 'section':
            required_params = ['name', 'description']
            if validate_params_exist(request, required_params):
                name = request.args['name']
                description = request.args['description']
                query = section['insert'].format(name, description)
                print(query)
                db.execute(query)
            else:
                return 'Make sure all required params are entered! Required Params: {}'.format(required_params)

        elif entity == 'item':
            required_params = ['name', 'price', 'description']
            if validate_params_exist(request, required_params):
                name = request.args['name']
                price = request.args['price']
                description = request.args['description']
                query = item['insert'].format(name, price, description)
                db.execute(query)
            else:
                return 'Make sure all required params are entered! Required Params: {}'.format(required_params)

        elif entity == 'modifiers':
            if validate_params_exist(request, ['description']):
                description = request.args['description']
                query = modifiers['insert'].format(description)
                db.execute(query)
            else:
                return 'Make sure all required params are entered! Required Params: {}'.format('description')

        elif entity == 'section_item':
            required_params = ['section_id', 'item_id']
            if validate_params_exist(request, required_params):
                section_id = request.args['section_id']
                item_id = request.args['item_id']
                query = section_item['insert'].format(section_id, item_id)
                db.execute(query)
            else:
                return 'Make sure all required params are entered! Required Params: {}'.format(required_params)

        elif entity == 'item_modifiers':
            required_params = ['item_id', 'modifier_id']
            if validate_params_exist(request, required_params):
                modifier_id = request.args['modifier_id']
                item_id = request.args['item_id']
                query = item_modifiers['insert'].format(item_id, modifier_id)
                db.execute(query)
            else:
                return 'Make sure all required params are entered! Required Params: {}'.format(required_params)
        else:
            return f'Table {entity} does not exist!'

        return f'{entity} was successfully created!'

    else:
        return f'Please specify table for inserting!'


@app.route('/api/menu/get', methods=['GET'])
def get_entity():
    valid_entities = ['section', 'item', 'modifiers', 'section_item', 'item_modifiers']
    if 'entity' in request.args:
        entity = request.args['entity']
        if entity in valid_entities:
            query = get_queries['get'].format(entity)
            response = db.fetchall(query)
            return jsonify(response)
        else:
            return f'Entity does not exist. Choose valid entity from {valid_entities}'
    else:
        return 'Entity parameter necessary!'


@app.route('/api/menu/get/<int:id>', methods=['GET'])
def get_entity_by_id(id):
    valid_entities = ['section', 'item', 'modifiers', 'section_item', 'item_modifiers']
    if 'entity' in request.args:
        entity = request.args['entity']
        if entity in valid_entities:
            query = get_queries['get_by_id'].format(entity, id)
            response = db.fetchall(query)
            return jsonify(response)
        else:
            return f'Entity does not exist. Choose valid entity from {valid_entities}'

    else:
        return 'Entity parameter necessary!'


@app.route('/api/menu/update/<int:id>', methods=['GET', 'PUT'])
def update_entity(id):
    if 'entity' in request.args:
        entity = request.args['entity']

        if entity == 'section':
            required_params = ['name', 'description']
            if validate_parnameams_exist(request, required_params):
                name = request.args['name']
                description = request.args['description']
                query = section['update'].format(name, description, id)
                db.execute(query)
            else:
                return 'Make sure all required params are entered! Required Params: {}'.format(required_params)

        elif entity == 'item':
            required_params = ['name', 'price', 'description']
            if validate_params_exist(request, required_params):
                name = request.args['name']
                price = request.args['price']
                description = request.args['description']
                query = item['update'].format(name, price, description, id)
                db.execute(query)
            else:
                return 'Make sure all required params are entered! Required Params: {}'.format(required_params)

        elif entity == 'modifiers':
            if validate_params_exist(request, ['description']):
                description = request.args['modifiers']
                query = modifiers['update'].format(description, id)
                db.execute(query)
            else:
                return 'Make sure all required params are entered! Required Params: {}'.format('description')

        elif entity == 'section_item':
            required_params = ['section_id', 'item_id']
            if validate_params_exist(request, required_params):
                section_id = request.args['section_id']
                item_id = request.args['item_id']
                query = section_item['update'].format(section_id, item_id, id)
                db.execute(query)
            else:
                return 'Make sure all required params are entered! Required Params: {}'.format(required_params)

        elif entity == 'item_modifiers':
            required_params = ['item_id', 'modifier_id']
            if validate_params_exist(request, required_params):
                item_id = request.args['item_id']
                modifier_id = request.args['modifier_id']
                query = item_modifiers['update'].format(item_id, modifier_id, id)

                db.execute(query)
            else:
                return 'Make sure all required params are entered! Required Params: {}'.format(required_params)

        else:
            return f'Entity does not exist!'

        return f'{entity} was updated successfully!'
    else:
        f'Entity parameter necessary'


@app.route('/api/menu/delete/<int:id>', methods=['GET', 'DELETE'])
def delete_entity(id):
    valid_entities = ['section', 'item', 'modifiers', 'section_item', 'item_modifiers']
    if 'entity' in request.args:
        entity = request.args['entity']
        if entity in valid_entities:
            query = delete['delete'].format(entity, id)
            db.execute(query)
            return f'''The {entity} is successfully deleted'''
        else:
            return f'Entity does not exist. Choose valid entity from {valid_entities}'
    else:
        return 'Entity parameter necessary!'
