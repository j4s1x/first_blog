from django.test import TestCase
from .models import Posts
from selenium import webdriver
import unittest
from blogs.views import index
from django.urls import resolve

class HomePageTest(TestCase):
    '''confirm home page view is correct'''
    def test_root_url_correct(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
