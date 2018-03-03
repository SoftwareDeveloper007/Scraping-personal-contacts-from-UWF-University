from urllib import *
from urllib.parse import urlparse, urljoin
from urllib.request import urlopen
import urllib.request
import requests
from io import BytesIO
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from lxml import html
from datetime import date, datetime, timedelta
from dateutil.relativedelta import *

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def scraping(first_name="", last_name="", driver=None):

    url = "http://uwf.edu/search/people/?q={}%20{}".format(first_name, last_name)
    if driver is None:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--disable-gpu')  # Last I checked this was necessary.
        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='WebDriver/chromedriver.exe')
        driver.maximize_window()

    try:
        driver.get(url)
        row = driver.find_elements_by_css_selector("tr.person-result > td")
        name = row[0].text
        position = row[1].text
        address = row[3].text
        phone_num = row[4].text
        mail = row[5].text
    except:
        name = ""
        position = ""
        address = ""
        phone_num = ""
        mail = ""

    print(name)
    print(position)
    print(address)
    print(phone_num)
    print(mail)

    return [position, address, phone_num, mail]

scraping(first_name="SUSAN", last_name="AMES")