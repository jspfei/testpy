#!/usr/bin/python
# -*- coding: utf-8 -*-

import json, urllib
from urllib import urlencode


# ----------------------------------
# 中国彩票开奖结果调用示例代码 － 聚合数据
# 在线接口文档：http://www.juhe.cn/docs/53
# ----------------------------------

def main():
    # 配置您申请的APPKey
    appkey = "*********************"

    # 1.彩票开奖结果查询
    request1(appkey, "GET")

    # 彩票开奖结果查询
def request1(appkey, m="GET"):
    url = "http://v.juhe.cn/lottery/query"

    params = {
        "key": appkey,  # 应用APPKEY(应用详细页查询)
        "lotteryid": "2",  # 彩票ID
        "date": "2015-08-01",  # 指定开奖日期2014-08-01，不指定默返回最近开奖结果
        "dtype": "json",  # 返回数据的格式,xml或json，默认json

    }
    params = urlencode(params)


    if m == "GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print res["result"]
        else:
            print "%s:%s" % (res["error_code"], res["reason"])
    else:
        print "request api error"

