"""
As a user,
I want to access a web application hosted on my local server,
So that I can verify that the application is installed and running successfully.
"""

from selenium import webdriver
import unittest
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.options = Options()
        self.service = Service("/snap/bin/geckodriver")
        self.browser = webdriver.Firefox(service=self.service, options=self.options)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get("http://localhost:8000")
        self.assertIn("To-Do", self.browser.title)
        self.fail("Test to be finished!")


if __name__ == "__main__":
    unittest.main(warnings="ignore")
