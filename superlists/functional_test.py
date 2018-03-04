import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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
    header = self.browser.find_element_by_tag_name('h1')
    self.assertIn("To-Do", header.text)

    #She is invited to enter a to-do items straight away
    inputbox = self.browser.find_element_by_id('id_new_item')
    self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

    #She types "Buy peacock feathers" into a text box
    inputbox.send_keys("Buy peacock feathers")

    #When she hits enter, the page updates and now the page lists
    #"1: Buy peacock feathers" as an item in ti-do lists
    inputbox.send_keys(Keys.ENTER)
    table = self.browser.find_element_by_id('id_list_table')
    rows = table.find_elements_by_tag_name("tr")
    self.assertIn(
	"1: Buy peacock feathers",
	[row.text for row in rows]
	)

    #There is still a text box inviting her to add another item. She
    #enters "Use peacock feathers to make a fly"
    inputbox = self.browser.find_element_by_id('id_new_item')
    inputbox.send_keys("Use peacock feathers to make a fly")
    inputbox.send_keys(Keys.ENTER) 

    #The page update again, and now shows both items on her list
    table = self.browser.find_element_by_id('id_list_table')
    rows = table.find_elements_by_tag_name("tr")
    self.assertIn(
        "2: Use peacock feathers to make a fly",
        [row.text for row in rows]
        )

    self.assertIn(
        "1: Buy peacock feathers",
        [row.text for row in rows]
        )

    #Diep wonders whether the site will remember her list. Then she sees
    #that the site has generated a unique URL for her --  there is some
    #explanatory text to that effect.
    self.fail("FInish the test")


    #assert "Django" in self.browser.title



if __name__ == "__main__":
  unittest.main()
