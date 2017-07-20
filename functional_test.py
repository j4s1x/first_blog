from selenium import webdriver
import time
import unittest
class NewVisitorTest(unittest.TestCase):
    '''set up and tear down test'''

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

#user logs on to page
    def test_user_online(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('The Blog Title', self.browser.title)
        self.fail('Test Complete')
#user sees list of blog titles and part of the content

#user can click individual article

#user goes selected article page and correct page is displayed

#user can read and leave comments if they want

#user can also view archive page
if __name__ == '__main__':
    unittest.main()
