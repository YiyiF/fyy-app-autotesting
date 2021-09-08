#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/6 6:14 下午
# @Author  : Fu Yiyi
# @Site    : 
# @File    : check_events.py
# @Software: PyCharm

# cmd：mitmdump -p 8889 -s fyy-app-autotesting/catchevents/check_events.py

# 埋点上传url
import all_events
from tb_events import GetData
from settings import Settings as ST

ST.url = 'http://kksdk.tapque.com/data_debug'
# 报告生成路径
ST.report_path = 'report'
# 所有事件名称
ST.all_events = all_events.get_all_events("resource/综合查询_2021-09-06 10_54.xlsx")
addons = [
    GetData()
]
