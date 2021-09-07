#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/5 7:43 下午
# @Author  : Fu Yiyi
# @Site    : ${SITE}
# @File    : main_page.py
# @Software: PyCharm
from selenium.webdriver.common.by import By

from page.album_page import AlbumPage
from page.common_page import CommonPage


class MainPage(CommonPage):
    _plus_btn_locator = (By.ID, "filto other 300 07")  # 私有类级别变量
    _drop_history_window = (By.ID, "Drop")  # 闪退保护弹窗

    def new_edit_session_from_plus(self):
        try:
            self.find_element_and_click(self._drop_history_window)
        except:
            pass
        self.find_element_and_click(self._plus_btn_locator)
        return AlbumPage(self.driver)

    # def content_b_use(self, content: Optional[str] = None):
    #     self.driver.find_element_by_id("use").click()
    #     if content:
    #         self.content = content
    #     return AlbumPage(self.driver, self.content)
