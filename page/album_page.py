#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/5 7:58 下午
# @Author  : Fu Yiyi
# @Site    : ${SITE}
# @File    : album_page.py
# @Software: PyCharm

from selenium.webdriver.remote.webdriver import WebDriver

from page.edit_page import PhotoEditPage


class AlbumPage(object):
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_photo(self):
        self.driver.find_element_by_xpath("//*[XCUIElementTypeCell[1]/XCUIElementTypeOther[2]]")
        return PhotoEditPage(self.driver)

    def is_album_shown(self):
        return self.driver.find_element_by_id("MEDIA").get_attribute("visible")
