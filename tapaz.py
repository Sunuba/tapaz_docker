#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Parser import Parser
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqla import Product, Base
import random
from time import sleep
import datetime


engine = create_engine('mysql+pymysql://tapaz:password@mysql/tapaz')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()



def save_data():
    parser = Parser('https://tap.az/all', base='https://tap.az')
    product_name = '//div[contains(@class, "endless-products")]/div[@class="products-i"]/a[@class="products-link"]/div[@class="products-name"]/text()'
    product_price = '//div[contains(@class, "endless-products")]/div[@class="products-i"]/a[@class="products-link"]/div[@class="products-top"]/div[@class="products-price-container"]/div[@class="products-price"]/span[@class="price-val"]/text()'
    currencies = '//div[contains(@class, "endless-products")]/div[@class="products-i"]/a[@class="products-link"]/div[@class="products-top"]/div[@class="products-price-container"]/div[@class="products-price"]/span[@class="price-cur"]/text()'
    product_code = '//div[contains(@class, "endless-products")]/div[@class="products-i"]/div[@class="products-bookmarking"]/a/@href'

    product_names = parser.get_data(product_name)
    prices = parser.get_data(product_price)
    valyuta = parser.get_data(currencies)
    codes = parser.get_data(product_code)
    
    for a in range(0, len(product_names)):
        product = session.query(Product).filter(Product.code.in_([codes[a].replace('bookmark', '')])).all()
        if not product:
            new_product = Product()
            new_product.name = product_names[a]
            new_product.price = prices[a].replace(' ', '')
            new_product.valyuta = valyuta[a]
            new_product.code = codes[a].replace('bookmark', '')
            session.add(new_product)
            session.commit()
            print(product_names[a], prices[a].replace(' ', ''), valyuta[a], codes[a].replace('bookmark', ''))
        else:
            pass
            today = datetime.datetime.now()
            print(product_names[a], ' exists in the database.', now.strftime("%Y-%m-%d %H:%M:%S"))


while True:
    sleep_time = random.randint(31, 48)
    print('Script will wait ' + str(sleep_time))
    try:
        save_data()
        sleep(sleep_time)
    except Exception as e:
        pass
