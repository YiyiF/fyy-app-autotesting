#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/5 7:58 下午
# @Author  : Fu Yiyi
# @Site    : ${SITE}
# @File    : album_page.py
# @Software: PyCharm
from selenium.webdriver.common.by import By

from page.common_page import CommonPage
from page.edit_page import PhotoEditPage


class AlbumPage(CommonPage):

    def select_photo(self):
        self.driver.find_element_by_xpath("//*[XCUIElementTypeCollectionView/XCUIElementTypeCell["
                                          "1]/XCUIElementTypeOther[2]]").click()
        return PhotoEditPage(self.driver)

    def is_album_shown(self):
        return self.find_element(By.ID, "MEDIA").get_attribute("visible")
