from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time


channels = [
    'UC8butISFwT-Wl7EV0hUK0BQ',
    'UCh9nVJoWXmFb7sLApWGcLPQ',
    'UC4JX40jDee_tINbkjycV4Sg'
]

url_youtube = 'https://www.youtube.com/channel/'


driver = webdriver.Chrome(ChromeDriverManager().install())
for channel in channels:
    driver.get(f'{url_youtube}{channel}')
    driver.find_element_by_xpath(
        '//div[contains(@class, "style-scope ytd-grid-video-renderer")]').click()
    time.sleep(10)
