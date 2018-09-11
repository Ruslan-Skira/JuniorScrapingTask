import requests
import json
from bs4 import BeautifulSoup
import re

# TODO Junior Scraping Test Task
# Task: parse data from the site https://suzyshier.com/
# Parsing algorithm:
# Open https://suzyshier.com/collections/sz_shop-all
# Select BOTTOMS category and parse all closes followed data:
# title (< h2 class="featured-collection__product-title" >)
# price (< span class="grid-item-price" >)
# color
# sizes
# specs
# description
# Select WEB EXCLUSIVES and parse data:
# title
# price
# discount_price
# Save data in any format (JSON for example)
#
# Save project code in gitlab/github. Add simple readme file.

url = "https://suzyshier.com/collections/sz_bottoms_shop-all-bottoms?view_all=true"
url_products = "https://suzyshier.com/collections/sz_bottoms_shop-all-bottoms/products"

r = requests.get(url)
soup = BeautifulSoup(r.content, features="html.parser")
products = soup.find_all("li", class_="grid__item one-fifth medium--one-quarter small--one-half product-list__item")

# todo take unic url of the products
def products_urls():
    count = 0
    urls = []
    for i in products:
        pr_url = i.contents[1].find_all("a", href=True)[0]["href"]
        urls.append('http://suzyshier.com' + pr_url)
        count += 1
    print(len(urls))
    return urls


# TODO write def for open and read at least tile from urls DONE.
# todo create dictionary and put there title DONE.
def get_data_from_url():
    count = 0
    full_dictionary = []
    for i in products_urls():

        r = requests.get(i)
        soup = BeautifulSoup(r.content, features="html.parser")
        title = soup.find_all("h1", {"class": "header"})[0].text
        price = soup.find_all("span", {"class": "product__price"})[0].text.strip()

        color = soup.find_all("label", {"class": 'product__radio'})[0]["title"]
        # dictionary of all sizes
        sizes = soup.find_all("input", {"class": "product__radio"})
        list_sizes = ""
        for k in sizes:
            list_sizes += k["value"]+","
        count += 1

        my_dic = {'title': title, 'price': price, 'color': color, "sizes": list_sizes}
        print(my_dic)
        full_dictionary.append(my_dic)


    with open('firstBottomPage.json', 'w') as f:
        json.dump(full_dictionary, f, indent=2)
    return

get_data_from_url()

