from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

options = Options()

service = Service("/snap/bin/geckodriver")
browser = webdriver.Firefox(service=service, options=options)

browser.get("http://localhost:8000")
assert "The install worked successfully! Congratulations!" in browser.title
