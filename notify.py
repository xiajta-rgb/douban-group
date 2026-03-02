# -*- coding: UTF-8 -*-

import logging
import re

import requests
import city_manager
from config import NOTIFY


def meet_condition(post, start_time):
    """
    根据用户配置的城市关键词判断是否满足通知条件
    """
    if post["create_time"] <= start_time:
        return False
    
    text = f'{post["title"]}\n{post["content"]}'
    
    cities = city_manager.get_cities()
    
    for city in cities:
        city_name = city.get('name')
        keywords = city.get('keywords', [])
        exclude_keywords = city.get('exclude_keywords', [])
        rent_min = city.get('rent_min', 0)
        rent_max = city.get('rent_max', 99999)
        
        for keyword in keywords:
            if keyword in text:
                for ex_keyword in exclude_keywords:
                    if ex_keyword in text:
                        return False
                
                if post.get('rent'):
                    if post['rent'] < rent_min or post['rent'] > rent_max:
                        return False
                
                return True
    
    return False


def send_msg(text):
    """
    推送普通消息
    :param text: 消息内容
    """
    data = channel[NOTIFY["channel"]](text)
    response = requests.post(NOTIFY["url"], json=data)
    logging.info('通知内容:%s\n返回结果:%s', text, response.text)


channel = {
    "feishu": lambda content: {
        "msg_type": "interactive",
        "card": {
            "elements": [
                {
                    "tag": "div",
                    "text": {
                        "tag": "lark_md",
                        "content": content
                    }
                }
            ]
        }
    },
    "work.weixin": lambda content: {
        "msgtype": "markdown",
        "markdown": {
            "content": content
        }
    },
    "dingtalk": lambda content: {
        "msgtype": "markdown",
        "markdown": {
            "title": re.search(r'\[(.*)\]', content).group(1) if re.search(r'\[(.*)\]', content) else '豆瓣租房',
            "text": content.replace('\n', '\n\n')
        }
    }
}
