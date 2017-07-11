from django.test import TestCase
from .models import Posts
from selenium import webdriver
import unittest

class UserFirstVisit(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_user_index_page(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('The Blog Title', self.browser.title)
        self.fail('Test Complete!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
