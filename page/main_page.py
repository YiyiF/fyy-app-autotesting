#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/5 7:43 下午
# @Author  : Fu Yiyi
# @Site    : ${SITE}
# @File    : main_page.py
# @Software: PyCharm
from selenium.webdriver.remote.webdriver import WebDriver

from page.album_page import AlbumPage


class MainPage(object):
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # def content_b_use(self, content: Optional[str] = None):
    #     self.driver.find_element_by_id("use").click()
    #     if content:
    #         self.content = content
    #     return AlbumPage(self.driver, self.content)

    def new_edit_session_from_plus(self):
        self.driver.find_element_by_name("filto other 300 07").click()
        return AlbumPage(self.driver)
