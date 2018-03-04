from selenium import webdriver
browser = webdriver.Firefox()
try:
  browser.get("http://localhost:8000")
except:
  pass
print(browser.title, 7777)

assert "Django" in browser.title
