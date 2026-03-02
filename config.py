# -*- coding: UTF-8 -*-

import datetime
import logging.config

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)-8s[%(name)s] {%(filename)s:%(lineno)d} -> %(message)s'
)

HEADERS = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/103.0.0.0 Safari/537.36',
    "Cookie": ''
}

START_TIME = datetime.datetime.combine(
    datetime.date.today(), datetime.time.min)

# 豆瓣小组列表 - 厦门租房相关小组
GROUP_LIST = [
    {"id": "603687", "name": "厦门租房", "start_time": START_TIME},
    {"id": "xiamen", "name": "厦门租房", "start_time": START_TIME},
    {"id": "627050", "name": "厦门租房", "start_time": START_TIME}
]

# 全局配置（备用）
MATCH_RULES = []
EXCLUDE_RULES = []
RENT_RANGE = (1000, 3000)
REQUEST_INTERVAL = (10, 20)
WATCH_INTERVAL = 3600
NOTIFY = {
    "channel": "feishu",
    "url": ""
}
