#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/7 11:30 上午
# @Author  : Fu Yiyi
# @Site    : 
# @File    : test_edit.py
# @Software: PyCharm
from time import sleep

import pytest

from page.app import App
from utils.load_resource import LoadResource


class TestEdit:


    def setup(self):
        self.home_page = App.start()
        self.album_page = self.home_page.new_edit_session_from_plus()
        self.photo_edit_page = self.album_page.select_photo()
        sleep(5)

    @pytest.mark.parametrize("pkg_name, index", LoadResource.load_json("../resource/to_filters.json"))
    def test_photo_edit_use_filter(self, pkg_name, index):
        self.photo_edit_page.use_filter(pkg_name, index)
        assert "No filter is selected.", self.photo_edit_page.is_filter_using()

    @pytest.mark.parametrize("pkg_name, index", LoadResource.load_json("../resource/to_filters.json"))
    def test_photo_edit_use_filter_and_save(self, pkg_name, index):
        self.photo_edit_page.use_filter(pkg_name, index)
        sleep(2)
        self.photo_edit_page.save_edition()
        assert "Save failed.", self.photo_edit_page.saved_successfully()

    def teardown(self):
        sleep(5)
        App.quit()
