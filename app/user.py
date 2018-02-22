import uuid

class User():
    """ Class User adds new users and also adds type of shopping list. """
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.type_of_list = []
        self.shopping_list = []



class type_of_list():
    """ Adds type of shopping list. """
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.id = uuid.uuid4
    

class shopping_list(object):
    """ Adds the shopping list. """
    def __init__(self, name, type_of_list, item, list):
        self.name = name
        self.type_of_list = type_of_list
        self.item = item
        self.list = list

