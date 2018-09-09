import requests
import json
from bs4 import BeautifulSoup

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

#todo def Bootom_category
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
count = 0
# for i in products:
#     title = i.contents[1].find_all("h2", {"class": "featured-collection__product-title"})[0].text
#     price = i.contents[1].find_all("span", {"class": "grid-item-price"})[0].text
#     color = i.contents[1].find_all("input", {"class": "swatch-radio js-quick-add-color"})[0]["value"]
    #sizes = ""
    #specs
    #description
#todo rewrite this for the pages exactly product so you can take all information cycle

    #print("title:" + title+ "\n price:" + price + "\n color:" + color )
    # print(color)
    count += 1
print(count)
# for t in price:
#     print("price: %s" % t.text)

#https://suzyshier.com/collections/sz_bottoms_shop-all-bottoms
#products/0711-24708571-striped-pants-with-multicolored-taping
#TODO you have second page make the def url

#TODO def WEB EXCLUSIVES():