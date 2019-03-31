import unittest
from project import db
from project.api.models import User
from project.tests.base import BaseTestCase



def add_user(email, password):
    user = User(email=email, password=password)
    db.session.add(user)
    db.session.commit()
    return user

class TestUserModel(BaseTestCase):

    def test_add_user(self):
        user = add_user('test@test.com', 'test')
        self.assertTrue(user.id)
        self.assertEqual(user.email, 'test@test.com')
        self.assertTrue(user.password)

    def test_to_json(self):
        user = add_user('test@test.com', 'randompass')
        self.assertTrue(isinstance(user.to_json(), dict))

    def test_passwords_are_random(self):
        user_one = add_user('test@test.com', 'randompass')
        user_two = add_user('test@test2.com', 'randompass')
        self.assertNotEqual(user_one.password, user_two.password)

    def test_encode_auth_token(self):
        user = add_user('test@test.com', 'test')
        auth_token = user.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, bytes))

    def test_decode_auth_token(self):
        user = add_user('test@test.com', 'test')
        auth_token = user.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, bytes))
        self.assertEqual(User.decode_auth_token(auth_token), user.id)


if __name__ == '__main__':
    unittest.main()