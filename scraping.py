from bs4 import BeautifulSoup
import requests

# scraping


def scraping_date(url):
    try:
        proxies = {"socks5h": "socks5h://127.0.0.1:9050",
                   "http": "http://127.0.0.1:8118"}
        r = requests.get(url, proxies=proxies)
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup
    except:
        print("Error: Cannot connect to the website")

# find content of post


def find_content(url):
    try:
        soup = scraping_date(url)
        li = soup.find_all('li')
        content = ""
        for i in li:
            content += " " + i.text
        return clean_text(content)
    except:
        print("Error: Cannot find content")

# convert html to data object


def html_to_data(post):
    try:
        dataObj = {
            "Title": clean_text(post.find('h4').text),
            "Content": find_content(post.find('a').get('href')),
            "Author":  post.find('div', {"class": 'col-sm-6'}).text.split(' ')[2],
            "Date": " ".join(post.find('div', {"class": 'col-sm-6'}).text.split(' ')[4:8])
        }
        return dataObj
    except:
        return

# Find all post of one page


def find_all_post(soup):
    try:
        data = []
        section = soup.find('section', id='list')
        posts = section.findChildren('div', {"class": 'row'})
        for post in posts:
            if html_to_data(post):
                data.append(html_to_data(post))
        return data
    except:
        print("Error: Cannot find all posts")

# cleaning text from special characters


def clean_text(text):
    try:
        return text.strip('\n').strip('\t')
    except:
        return


# get all data from all pages
def find_all_data_from_pages():
    all_data = []
    data = scraping_date(
        "http://strongerw2ise74v3duebgsvug4mehyhlpa7f6kfwnas7zofs3kov7yd.onion/all")
    all_data.extend(find_all_post(data))  # add all post of first page
    pagination = data.find('ul', {"class": 'pagination'})
    pages = pagination.find_all('li')
    for page in pages[1:len(pages) - 1]:
        if page.find('a'):
            link = page.find('a').get('href')
            data = scraping_date(link)
            all_data.extend(find_all_post(data))
    return all_data
