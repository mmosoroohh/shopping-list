from app import app, user
import unittest


User = user.User


class TestList(unittest.TestCase):

    def setUp(self):
        self.user_list = []
        self.new_user = User('arnold osoro', 'arnoldmaengwe@gmail.com', '254')
        self.current_user = dict(email=self.new_user.email, type_of_list=self.new_user.type_of_list, shopping_of_list=self.new_user.shopping_of_list)
        self.user_list.append(self.new_user)


def tearDown(self):
    pass

def register(self):
    tester = app.test_client(self)
    return tester.post('/register', data=dict(name='arnold osoro', email='arnoldmaengwe@gmail.com', password='254'), follow_redirects=True)

def login(self):
    tester = app.test_client(self)
    return tester.post('/login', data=dict(email='arnoldmaengwe@gmail.com', password='254', follow_redirects=True))

def add_list(self):
    tester = app.test_client(self)
    return tester.post('/add_list', data=dict(title='Grocery', item='tomatoes, onions, sukuma wiki'))


if __name__ == '__main__':
    unittest.main()