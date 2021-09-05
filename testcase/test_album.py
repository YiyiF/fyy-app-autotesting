#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/5 8:50 下午
# @Author  : Fu Yiyi
# @Site    : 
# @File    : test_album.py
# @Software: PyCharm
from time import sleep

from page.album_page import AlbumPage
from page.app import App
# from page.edit_page import PhotoEditPage


class TestAlbum:

    def setup(self):
        self.home_page = App.start()
        self.home_page.new_edit_session_from_plus()

    def test_open_album_from_plus(self):
        assert "No filter is using now.", AlbumPage.is_album_shown()

    def teardown(self):
        # sleep(5)
        App.quit()
