#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/5 8:04 下午
# @Author  : Fu Yiyi
# @Site    : ${SITE}
# @File    : edit_page.py
# @Software: PyCharm
from appium.webdriver.common.touch_action import TouchAction

from page.common_page import CommonPage


class PhotoEditPage(CommonPage):

    def use_filter(self, pkg_name: str, index: str):
        # 展开pkg_name包
        self.driver.find_element_by_accessibility_id(pkg_name).click()
        # 使用index内容
        x_index = self.driver.find_element_by_id(index).get_attribute("x")
        TouchAction(self.driver).tap(x_index, y_index = 671).perform()
        return PhotoEditPage

    def is_filter_using(self):
        # 二级调节项btn：filto_edit_300_36
        # setting_sheet = self.driver.find_element_by_accessibility_id("filto_edit_300_36")
        visibility_of_selected = self.driver.find_element_by_xpath(
            "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther").get_attribute("visible")
        return visibility_of_selected
