#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/5 7:23 下午
# @Author  : Fu Yiyi
# @Site    : 
# @File    : app.py
# @Software: PyCharm
from appium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from page.main_page import MainPage


class App:

    driver: WebDriver
    @classmethod
    def start(cls):
        caps = {}
        caps["platformName"] = "ios"
        caps["automationName"] = "XCUITest"

        caps["xcodeOrgId"] = "9N556RRA53"
        caps["xcodeSigningId"] = "iPhone Developer"

        caps["deviceName"] = "11的iPhone"
        caps["udid"] = "00008101-000565A43C82001E"
        # caps[
        #     "app"] = "/Users/yiyi/Library/Developer/Xcode/DerivedData/UICatalog-ezitcgxttljbnudcmmaglmooqhtj/Build/Products/Debug-iphoneos/UICatalog.app"
        caps["appName"] = "Filto"
        caps["bundleId"] = "com.pinsotech.filto"

        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        cls.driver.implicitly_wait(5)

        return MainPage(cls.driver)

    @classmethod
    def quit(cls):
        cls.driver.quit()

