import requests
import json
from bs4 import BeautifulSoup
import re
# TODO write def for the exclusive page
# Select WEB EXCLUSIVES and parse data:
# title
# price
# discount_price
# Save data in any format (JSON for example)
#
# Save project code in gitlab/github. Add simple readme file.


url = "https://suzyshier.com/collections/sz_trend_online-exclusives"
r = requests.get(url)
soup = BeautifulSoup(r.content, features="html.parser")
products = soup.find_all("li", class_="product-list__item")

def products_urls():
    count = 0
    urls = []
    for i in products:
        pr_url = i.contents[1].find_all("a", href=True)[0]["href"]
        urls.append('http://suzyshier.com' + pr_url)
        count += 1
    return urls

def get_data_from_url():
    count = 0
    full_dictionary = []
    for i in products_urls():

        r = requests.get(i)
        soup = BeautifulSoup(r.content, features="html.parser")
        title = soup.find_all("h1", {"class": "header"})[0].text
        try:
            discount = soup.find_all("span", {"class": "product__price"})[0].text.strip()
            price= soup.find_all("span", {"class": "product__compare-at"})[0].text.strip()
            my_dic = {'title': title, 'price': price, 'discount': discount}
        except:
            price = soup.find_all("span", {"class": "product__price"})[0].text.strip()
            my_dic = {'title': title, 'price': price}
        print(my_dic)
        full_dictionary.append(my_dic)
    with open('ExclusivePage.json', 'w') as f:
        json.dump(full_dictionary, f, indent=2)
    return

get_data_from_url()


