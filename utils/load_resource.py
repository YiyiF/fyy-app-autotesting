#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/7 5:56 下午
# @Author  : Fu Yiyi
# @Site    : 
# @File    : load_resource.py
# @Software: PyCharm
import json


class LoadResource:

    @staticmethod
    def load_json(path):
        json_data = json.load(open(path, "r"))
        dict_tuple = zip(json_data.keys(), json_data.values())
        loaded_data = []
        for i in dict_tuple:
            loaded_data.append(i)
        return loaded_data
