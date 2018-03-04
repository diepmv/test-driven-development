from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page
# Create your tests here.

class HomePageTest(TestCase):
  def test_home_page_is_about_toto_lists(self):
    request = HttpRequest()

    response = home_page(request)
    print(response.content)
    self.assertTrue(response.content.startswith(b"<html>"))
    self.assertIn(b'<title>To-Do Lists</title>', response.content)
    self.assertTrue(response.content.endswith(b"</html>"))
