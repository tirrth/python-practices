from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import requests
from bs4 import BeautifulSoup

text = 'python'
url = 'https://google.com/search?q=' + text + '&source=lnms&tbm=isch'

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get(url)

# Will keep scrolling down the webpage until it cannot scroll no more
# last_height = driver.execute_script('return document.body.scrollHeight')
# while True:
#     driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
#     time.sleep(2)
#     new_height = driver.execute_script('return document.body.scrollHeight')
#     try:
#         driver.find_element_by_xpath(
#             '//*[@id="islmp"]/div/div/div/div/div[5]/input').click()
#         time.sleep(2)
#     except:
#         pass
#     if new_height == last_height:
#         break
#     last_height = new_height

imagePageActionLinks = []
for i in range(1, 10):
    try:
        source = driver.find_element_by_xpath(
            '//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]')
        action = ActionChains(driver)
        action.context_click(source).perform()
        # print(source.get_attribute("href"))
        imagePageActionLinks.append(source.get_attribute("href"))
    except:
        pass

user_agent = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
}  # write: 'my user agent' in browser to get your browser user agent details

ActualImages = []
for page_url in imagePageActionLinks:
    try:
        res = requests.get(page_url, headers=user_agent)
        soup = BeautifulSoup(res.text, 'html.parser')
        result = soup.find('img', {'class': 'n3VNCb'})
        link = result['src']
        ActualImages.append(link)
    except KeyError:
        continue

print(ActualImages)
