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

#url = "https://suzyshier.com/collections/sz_shop-all"

url = "https://suzyshier.com/collections/sz_bottoms_shop-all-bottoms"
url_products = "https://suzyshier.com/collections/sz_bottoms_shop-all-bottoms/products"

r = requests.get(url)
soup = BeautifulSoup(r.content, features="html.parser")
products = soup.find_all("li", class_="grid__item one-fifth medium--one-quarter small--one-half product-list__item")
title = soup.find_all("h2", class_="featured-collection__product-title")
price = soup.find_all("span")
empty = []
# for text in title:
#     print("title :%s" % text.text)
# todo take unic url of the products
def products_urls():
    count = 0
    urls = []
    for i in products:
        pr_url = soup.find_all("a", href=re.compile("sz_bottoms_shop-all-bottoms/products"))[count]["href"]
        urls.append('https://suzyshier.com'+ pr_url)
        count += 1
    urls = set(urls)
    return urls


# TODO write def for open and read at least tile from urls DONE.
# todo create dictionary and put there title DONE.
# todo
def get_data_from_url():
    count = 0
    full_dictionary= []
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

#     price = i.contents[1].find_all("span", {"class": "grid-item-price"})[0].text
#     color = i.contents[1].find_all("input", {"class": "swatch-radio js-quick-add-color"})[0]["value"]



#TODO def WEB EXCLUSIVES():