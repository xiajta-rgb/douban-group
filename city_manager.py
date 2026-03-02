# -*- coding: UTF-8 -*-

import json
import os

CONFIG_FILE = 'city_config.json'


def load_city_config():
    if not os.path.exists(CONFIG_FILE):
        return {"cities": []}
    try:
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return {"cities": []}


def save_city_config(config):
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False, indent=2)


def get_cities():
    config = load_city_config()
    return config.get('cities', [])


def get_keywords_for_city(city_name):
    """获取城市的匹配关键词"""
    cities = get_cities()
    for city in cities:
        if city.get('name') == city_name:
            return city.get('keywords', [])
    return []


def get_exclude_keywords_for_city(city_name):
    """获取城市的排除关键词"""
    cities = get_cities()
    for city in cities:
        if city.get('name') == city_name:
            return city.get('exclude_keywords', [])
    return []


def get_all_keywords():
    """获取所有城市的关键词"""
    cities = get_cities()
    keywords = []
    for city in cities:
        keywords.extend(city.get('keywords', []))
    return list(set(keywords))


def add_city(city):
    config = load_city_config()
    config['cities'].append(city)
    save_city_config(config)


def update_city(city_name, city_data):
    config = load_city_config()
    for i, city in enumerate(config['cities']):
        if city['name'] == city_name:
            config['cities'][i] = city_data
            break
    save_city_config(config)


def delete_city(city_name):
    config = load_city_config()
    config['cities'] = [c for c in config['cities'] if c['name'] != city_name]
    save_city_config(config)
