#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/6 11:54 上午
# @Author  : Fu Yiyi
# @Site    : 
# @File    : tb_events.py
# @Software: PyCharm

import json
import os
import urllib

import mitmproxy
from mitmproxy import http, ctx

from settings import Settings as ST


class GetData:
    events_list = []

    def request(self, flow: mitmproxy.http.HTTPFlow):
        """
        代理服务数据分析
        :param flow:
        :return:
        """

        request_data = flow.request
        self.request_url = request_data.url

        if ST.url in self.request_url:
            api = self.request_url.split('/')[3]
            ctx.log.error("Get API address after splitting ====>{}".format(api))

            request_content = str(flow.request.content).split('&')[4].split('=')[1][:-1]
            unquote_request_content = urllib.parse.unquote(request_content)
            ctx.log.info("Get encrypted data after splitting ====>{}".format(unquote_request_content))

            event_data = json.loads(unquote_request_content)

            try:
                event = event_data["#event_name"]
                ctx.log.error("Get the event name after analyzing the data ====> {}".format(event))
                self.events_list.append(event)
            except KeyError:
                ctx.log.warn("No events！")
            event_list = list(set(self.events_list))

            if not os.path.exists(ST.report_path):
                os.mkdir(ST.report_path)
                ctx.log.info(ST.report_path + 'Successfully created！')

            file = open('{}/now_event.txt'.format(ST.report_path), 'w')
            for line in event_list:
                file.write(line + '\n')
            ctx.log.warn("Current event name collection ====>{}".format(event_list))
            lost_list = list(set(ST.all_events).difference(set(event_list)))
            ctx.log.warn("Missing event name collection ====>{}".format(lost_list))
            file = open('{}/lost_event.txt'.format(ST.report_path), 'w')
            for line in lost_list:
                file.write(line + '\n')
