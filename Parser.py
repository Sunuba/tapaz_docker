#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from lxml import html
import xml
from time import sleep
import re
import datetime
import random


class Parser():
    def __init__(self, link, base):
        self.link = link
        self.base = base

    @staticmethod
    def get_headers():
        return {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    def create_tree(self):
        headers = self.get_headers()
        page = requests.get(self.link, headers=headers)
        return html.fromstring(page.content.decode('utf-8'))

    def get_data(self, html_code):
        tree = self.create_tree()
        return tree.xpath(html_code)
