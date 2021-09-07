#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/5 7:23 下午
# @Author  : Fu Yiyi
# @Site    : 
# @File    : app.py
# @Software: PyCharm
import os

from appium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from page.main_page import MainPage


class App:
    driver: WebDriver

    @staticmethod
    def connect_device():
        info_cmd = "tidevice list"
        device_info = os.popen(info_cmd, 'r').readlines()[0]

        device_info = device_info.strip('\n')
        real_device_udid, real_device_name = device_info.split(" ", 1)
        return real_device_udid, real_device_name

    @classmethod
    def start(cls):
        caps = {}
        caps["platformName"] = "ios"
        caps["automationName"] = "XCUITest"

        caps["xcodeOrgId"] = "9N556RRA53"
        caps["xcodeSigningId"] = "iPhone Developer"

        real_device_udid, real_device_name = cls.connect_device()
        caps["deviceName"] = real_device_name
        caps["udid"] = real_device_udid

        # caps[
        #     "app"] = "/Users/yiyi/Library/Developer/Xcode/DerivedData/UICatalog-ezitcgxttljbnudcmmaglmooqhtj/Build/Products/Debug-iphoneos/UICatalog.app"
        caps["appName"] = "Filto"
        caps["bundleId"] = "com.pinsotech.filto"

        caps["printPageSourceOnFindFailure"] = True  # 找元素失败时打印pageSource

        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        cls.driver.implicitly_wait(5)

        return MainPage(cls.driver)

    @classmethod
    def quit(cls):
        cls.driver.quit()
