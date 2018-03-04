import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
  def setUp(self):
    self.browser = webdriver.Firefox()
  
  def tearDown(self):
    self.browser.quit()

  def test_starting_a_new_todo_list(self):
    #Diep has heard about a cool new to-do lists app
    #She goes to its homepage
    self.browser.get("http://localhost:8000")

    #She notices the page title and header mention to-do lists
    self.assertIn("To-Do", self.browser.title) 

    #She is invited to enter a to-do items straight away
    assert "Django" in self.browser.title



if __name__ == "__main__":
  unittest.main()
