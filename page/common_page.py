#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/5 10:00 下午
# @Author  : Fu Yiyi
# @Site    : 
# @File    : common_page.py
# @Software: PyCharm
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CommonPage:
    _black_list = [
        (By.ID, "Allow"),    # 系统权限弹窗，如通知权限
        (By.ID, "Tips")
    ]

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, locator):
        try:
            return self.driver.find_element(*locator)
        except:
            self.handle_exception()
            return self.driver.find_element(*locator)

    def find_element_and_click(self, locator):
        try:
            self.find_element(locator).click()
        except:
            self.handle_exception()
            self.find_element(locator).click()

    def handle_exception(self):
        print(":Exception")
        self.driver.implicitly_wait(0)  # 进入异常判断，则不进行强制等待
        for locator in self._black_list:
            print(locator)
            # Method A:
            elements = self.driver.find_elements(
                *locator)  # use find_elements rather than find_element to avoid exception
            if len(elements) >= 1:
                elements[0].click()
            else:
                print("%s not found" % str(locator))

            # Method B: No need to loop for findind every locator
            # page_source = self.driver.page_source
            # if "Allow" in page_source:
            #     self.find_element_and_click(*locator)
            # elif "Tips" in page_source:
            #     pass

        self.driver.implicitly_wait(5)
