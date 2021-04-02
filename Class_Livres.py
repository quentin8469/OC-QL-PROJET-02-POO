#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


class Book:

    """
    Scrap un livre
    """

    def __init__(self, url_book, soupe):
        """ docstring """

        self.url = url_book
        self.soupe = soupe
        self.upc = self.get_universal_product_code(url_book)

    def get_universal_product_code(self):
        """ get UPC of a book """

        upc = self.soupe.find_all("td")[0].text
        return upc


def main():
    """ ddd """
    url_book = (
        "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    )
    html = requests.get(url_book)
    print("bob1")
    soupe = BeautifulSoup(html.content, "html.parser")
    print("bob2")
    livre = Book(url_book, soupe)
    print("bob3")
    livre.get_universal_product_code()
    print("bob4")
    return print(livre.get_universal_product_code())


print("bob5")


"""
if __name__ == "__main__":
    main()
"""
