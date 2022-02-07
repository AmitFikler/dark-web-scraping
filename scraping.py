import requests
from bs4 import BeautifulSoup

proxies = {
    "socks5h": "socks5h://127.0.0.1:9050",
    "http": "http://127.0.0.1:8118",
}

website_config = {
    "paste_selector": "#list > .row",
    "title_selector": "h4",
    "author_selector": ".col-sm-6",
    "date_selector": ".col-sm-6",
    "full_content_selector": ".btn-success",
    "content_selector": "li",
    "pagination_selector": ".pagination>li"
}

# ---------- GET LANDING PAGE FOR WEBSITE WITH URL ---------- #


def get_landing_page(url):
    """
    url: Website url str
    return: Landing html page for url
    """
    try:
        response = requests.get(url, proxies=proxies)
        page_clean_html = BeautifulSoup(response.text, 'html.parser')
        return page_clean_html
    except:
        print(f"Error with getting {url} page code")

# ---------- SET TO PASTES LIST ---------- #


def get_pastes_list_from_html(html_code, paste_selector):
    """
    :html_code: Web site html code
    :paste_selector: CSS selector to find paste
    :return: pastes into objects list
    """
    pastes = html_code.select(paste_selector)  # Get all pastes containers
    pastes_list = []
    # Run throw all pastes containters and get parsed obj from each. Insert into list
    for paste in pastes:
        parsed_obj = from_paste_to_object(
            paste, website_config["title_selector"], website_config["author_selector"], website_config["full_content_selector"])
        if parsed_obj:
            # print(f"\n\n parsed_obj: \n\n {parsed_obj}")
            pastes_list.append(parsed_obj)
    print(f"pastes_list :{pastes_list }\n")
    return pastes_list

# ---------- GET PASTE AND RETURN AS OBJ ---------- #


def from_paste_to_object(paste, title_selector, author_selector, full_content_selector):
    """
    :paste: Div element
    :title_selector: Title CSS Selector
    :author_selector: Author CSS Selector
    :full_content_selector: Full content CSS Selector
    :return: Paste obj with {Title: ? , Author: ?, Date: ?, Content: ?} or None
    """
    try:
        details_line_list = paste.select(author_selector)[0].text.split(" ")
        full_paste_url = paste.select(full_content_selector)[0].attrs["href"]
        # Fixed obj {Title: ? , Author: ?, Date: ?, Content: ?}
        return {
            "Title": paste.find_all(title_selector)[0].text.strip(),
            "Author": details_line_list[2],
            "Content": get_paste_content(full_paste_url, website_config["content_selector"]),
            "Date": " ".join(details_line_list[4:8]),
        }
    except:
        return

# ---------- GET PASTE CONTENT ---------- #


def get_paste_content(full_paste_url, content_selector):
    """
    :full_paste_url: Dark web url leading to full page
    :content_selector: Content CSS selector
    :return: content str
    """
    # Request full paste html code
    response = requests.get(full_paste_url, proxies=proxies)
    full_paste_html = BeautifulSoup(response.text, 'html.parser')
    # Get content list
    all_content = full_paste_html.find_all(content_selector)
    content = ""
    for li in all_content:
        content += f"{li.text}. "  # Add to one string
    return content.strip()

# ---------- GET NUMBER OF PAGES ---------- #


def get_number_of_pages(html_code, pagination_selector):
    """
    :html_code: Web page code
    :pagination_selector: Pagination CSS selector
    :return: last page number
    """
    pagination_elem = html_code.select(
        pagination_selector)  # Get pagination elem
    return pagination_elem[len(pagination_elem) - 2].text

# ---------- MAIN ---------- #


def find_all_data_from_pages():
    """
    :return: List with all pastes from all pages
    """
    html_page = get_landing_page(
        "http://strongerw2ise74v3duebgsvug4mehyhlpa7f6kfwnas7zofs3kov7yd.onion/all")
    # Get pages number and empty list
    number_of_pages = int(get_number_of_pages(
        html_page, website_config["pagination_selector"]))
    all_data = []
    page = 1

    # Run throw all pages from 1 to last
    while page < number_of_pages + 1:
        print(f"page: {page}")
        # Get html for page
        html_page = get_landing_page(
            f"http://strongerw2ise74v3duebgsvug4mehyhlpa7f6kfwnas7zofs3kov7yd.onion/all?page={page}")
        # Get pastes objects list and append to general list
        all_data.extend(get_pastes_list_from_html(
            html_page, website_config["paste_selector"]))
        page += 1
    print(all_data)
    return all_data
