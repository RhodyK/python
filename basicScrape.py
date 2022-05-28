#!/usr/bin/python3
import requests
import re
from bs4 import BeautifulSoup

# get target URL from stdin
PAGE_URL = input('Please give me a url to target. e.g. http://target:port:' )

#scrape all of the html of webpage at url
def get_html_of(url):
    resp = requests.get(url)

    #return status code if not a valid html response
    if resp.status_code != 200:
        print(f'HTTP status code of {resp.status_code} returned, but 200 was expected. Exiting...')
        exit(1)

    return resp.content.decode()

html = get_html_of(PAGE_URL)
soup = BeautifulSoup(html, 'html.parser')
raw_text = soup.get_text()
all_words = re.findall(r'\w+', raw_text)

word_count = {}

#count up all the words on the web page
for word in all_words:
    if word not in word_count:
        word_count[word] = 1
    else:
        current_count = word_count.get(word)
        word_count[word] = current_count + 1

#sort wordlist by highest count first
top_words = sorted(word_count.items(), key=lambda item: item[1], reverse=True)

#print only the top 10 most used words
for i in range(10):
    print(top_words[i][0])

