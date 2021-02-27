import requests
from bs4 import BeautifulSoup
# import random

text = 'python'
url = 'https://google.com/search?q=' + text + '&gbv=2&tbm=isch'

####################################################################################################################################################################################

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
}  # write: 'my user agent' in browser to get your browser user agent details

############################################################ OR ############################################################

# A = ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
#      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
#      "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
#      )
# Agent = A[random.randrange(len(A))]
# headers = {'user-agent': Agent}

####################################################################################################################################################################################

res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')
# html.parser
# html5lib
# print(soup)
ActualImages = []  # contains the link for Large original images, type of  image
for result in soup.find_all('img', {'class': 'rg_i Q4LuWd'}):
    try:
        link = result['src']
        ActualImages.append(link)
    except KeyError:
        continue


# for result in soup.find_all('a', {'class': 'wXeWr islib nfEiy mM5pbd'}):
#     try:
#         link = result
#         ActualImages.append(link)
#         # print(link)
#         # print("#####")
#     except KeyError:
#         continue

# print("there are total", len(ActualImages), "images")
print(ActualImages)
