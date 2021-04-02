#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import os


class Book:

    """
    Scrap un livre
    """

    def __init__(self, url_book):
        """ docstring """
        self.html = requests.get(url_book)
        self.soupe = BeautifulSoup(self.html.content, "html.parser")
        self.url = url_book
        self.category = self.get_category()
        self.titles = self.get_title()
        self.description = self.get_product_description()
        self.upc = self.get_universal_product_code()
        self.price_including_tax = self.get_price_including_tax()
        self.price_excluding_tax = self.get_price_excluding_tax()
        self.tax = self.get_tax()
        self.Number_avialable = self.get_number_available()
        self.review_rating = self.get_review_rating()
        self.image_url = self.get_image_url()
        self.local_image_path = self.download_picture()
        # self.image_directory = self.picture_directory()

    def get_universal_product_code(self):
        """ get UPC of a book """

        upc = self.soupe.find_all("td")[0].text
        return upc

    def get_title(self):
        """ get the title of a book """

        title = self.soupe.find("h1").text
        return title

    def get_price_including_tax(self):
        """ get the price with the tax of a book """

        price_including_tax = self.soupe.find_all("td")[3].text
        return price_including_tax

    def get_price_excluding_tax(self):
        """ get the price of a book excludinf tax """

        price_excluding_tax = self.soupe.find_all("td")[2].text
        return price_excluding_tax

    def get_tax(self):
        """ get the price of the tax of a book """

        tax = self.soupe.find_all("td")[4].text
        return tax

    def get_number_available(self):
        """ get the number of a book in stock """

        number_available = self.soupe.find_all("td")[5].text
        return number_available

    def get_product_description(self):
        """ give the description of the story for a book """

        product_description = self.soupe.find_all("p")[3].text
        return product_description

    def get_category(self):
        """ give the category of a book """

        category = self.soupe.find_all("li")[2].text.strip()
        return category

    def get_review_rating(self):
        """ give the number of star for a book """

        review_rating = self.soupe.find_all("td")[6].text
        return review_rating

    def get_image_url(self):
        """ give the picture url of a book """

        image_book = self.soupe.find("img").get("src")
        url_image = image_book.replace("../../", "http://books.toscrape.com/")
        return url_image

    '''
    def picture_directory(self, cat_image):
        """ create pictures directory for one category """

        try:
            os.mkdir(cat_image)
        except:
            pass
        try:
            os.chdir(cat_image)
        except:
            pass
    '''

    def download_picture(self):
        """ download pictures in directory """

        cat_image = self.category
        # self.picture_directory(cat_image)
        picture_title = self.upc
        url_image = self.image_url
        lien_image = requests.get(url_image)
        with open(f"{cat_image}_{picture_title}.jpg", "wb") as dl_image:
            dl_image.write(lien_image.content)

        local = os.getcwd()
        # os.chdir("../")
        return local

    def get_data_in_dictionnarie(self):
        """ get all data of one book in a dictionnarie """

        book_data = {}
        book_data["Book_Url"] = self.url
        book_data["Category"] = self.category
        book_data["Titles"] = self.titles
        book_data["Description"] = self.description
        book_data["UPC"] = self.upc
        book_data["Price_including_tax"] = self.price_including_tax
        book_data["Price_excluding_tax"] = self.price_excluding_tax
        book_data["Tax "] = self.tax
        book_data["Number_available"] = self.Number_avialable
        book_data["Review_rating"] = self.review_rating
        book_data["Image_url"] = self.image_url
        book_data["local_Image_path"] = self.local_image_path

        return book_data

    def get_bob():
        print("bob il est là")


def main():
    """ doc """

    url_book1 = (
        "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    )

    livre1 = Book(url_book1)

    return livre1.get_data_in_dictionnarie()


if __name__ == "__main__":
    main()

print(main())
