# import the necessary libraries
import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# define the url of the webpage
url = "https://medium.com/thedevproject/top-5-python-blogs-that-you-should-follow-and-read-in-2022-1d1671dccbf2"

# make a request to the webpage 
r = requests.get(url)

# parse the response using Beautiful Soup
soup = BeautifulSoup(r.content, 'html.parser')

# extract all the html headers
headers = soup.find_all('h1', 'h2','h3', 'h4')

# create a translator object
translator = Translator()

# create two empty lists to save the translated headers
spanish_headers = []
chinese_headers = []

# loop through the headers and translate them to spanish and chinese
for header in headers:
    spanish_headers.append(translator.translate(header.text, dest='es').text)
    chinese_headers.append(translator.translate(header.text, dest='zh-cn').text)

# create two html files, one for spanish and one for chinese
with open('spanish_headers.html', 'w') as f:
    for header in spanish_headers:
        f.write('<h1>{}</h1>'.format(header))

with open('chinese_headers.html', 'w') as f:
    for header in chinese_headers:
        f.write('<h1>{}</h1>'.format(header))
