from asyncio import constants
from turtle import pos
from bs4 import BeautifulSoup
import requests


def scraping_date(url):
    try:
        proxies = {"socks5h": "socks5h://127.0.0.1:9050",
                   "http": "http://127.0.0.1:8118"}
        r = requests.get(url, proxies=proxies)
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup
    except:
        print("Error: Cannot connect to the website")


def html_to_data(post):
    try:
        dataObj = {
            "heading": post.find('h4').text.strip('\n').strip('\t'),
            "Author":  post.find('div', {"class": 'col-sm-6'}).text.split(' ')[2],
            "Date": " ".join(post.find('div', {"class": 'col-sm-6'}).text.split(' ')[4:8])
        }
        return dataObj
    except:
        return


def find_all_post(soup):
    try:
        data = []
        section = soup.find('section', id='list')
        posts = section.findChildren('div', {"class": 'row'})
        print(posts[3].find('div', {"class": 'col-sm-6'}).text.split(' ')[2])
        for post in posts:
            if html_to_data(post):
                data.append(html_to_data(post))
        return data
    except:
        print("Error: Cannot find all posts")


data = scraping_date(
    "http://strongerw2ise74v3duebgsvug4mehyhlpa7f6kfwnas7zofs3kov7yd.onion/all")

print(find_all_post(data))
