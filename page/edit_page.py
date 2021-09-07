#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/5 8:04 下午
# @Author  : Fu Yiyi
# @Site    : ${SITE}
# @File    : edit_page.py
# @Software: PyCharm
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page.common_page import CommonPage


class PhotoEditPage(CommonPage):

    def use_filter(self, pkg_name: str, index: int):
        # 展开pkg_name包
        self.driver.find_element_by_accessibility_id(pkg_name).click()
        # 使用index内容
        cell_index_locator = \
            "//*[XCUIElementTypeCollectionView/XCUIElementTypeCell[" + str(index) + \
            "]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage] "
        self.driver.find_element_by_xpath(cell_index_locator).click()

        return PhotoEditPage

    def save_edition(self):
        self.find_element_and_click((By.ID, "filto321 2"))
        return PhotoEditPage

    def saved_successfully(self):
        if len(self.driver.find_elements_by_id("filto edit 300 82")) == 1:
            return True
        else:
            return False

    def is_filter_using(self):
        # 二级调节项btn：filto_edit_300_36
        if len(self.driver.find_elements_by_accessibility_id("filto_edit_300_36")) == 1:
            return True
        else:
            return False
