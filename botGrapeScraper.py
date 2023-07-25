from bs4 import BeautifulSoup
from selenium import webdriver

soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())