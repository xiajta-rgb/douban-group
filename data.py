# -*- coding: UTF-8 -*-

import json
import os
from datetime import datetime
import city_manager

DATA_FILE = 'posts.json'


def load_posts():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return []


def load_posts_by_city(city=None):
    posts = load_posts()
    if not city:
        return posts
    return [p for p in posts if p.get('city') == city]


def detect_city(post):
    """根据帖子标题和内容自动检测城市"""
    cities = city_manager.get_cities()
    if not cities:
        return None
        
    text = ""
    if post.get('title'):
        text += post['title'] + " "
    if post.get('content'):
        text += post['content']
    
    for city_config in cities:
        keywords = city_config.get('keywords', [])
        for keyword in keywords:
            if keyword in text:
                return city_config['name']
    return None


def save_post(post):
    posts = load_posts()
    url = post.get('url')
    
    city = detect_city(post)
    if city:
        post['city'] = city
    
    for i, p in enumerate(posts):
        if p.get('url') == url:
            posts[i] = post
            break
    else:
        posts.insert(0, post)
    
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(posts, f, ensure_ascii=False, indent=2, default=str)
    
    return city


def get_cities():
    return city_manager.get_cities()
