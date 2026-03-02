# -*- coding: UTF-8 -*-

import os
from flask import Flask, jsonify, send_from_directory, request
import data
import city_manager

app = Flask(__name__, static_folder='.', static_url_path='')


@app.route('/api/posts')
def get_posts():
    city = request.args.get('city')
    if city and city != 'all':
        posts = data.load_posts_by_city(city)
    else:
        posts = data.load_posts()
    return jsonify(posts)


@app.route('/api/cities')
def get_cities():
    return jsonify(city_manager.get_cities())


@app.route('/api/config')
def get_config():
    cities = city_manager.get_cities()
    return jsonify({
        'cities': [c['name'] for c in cities],
        'city_config': cities
    })


@app.route('/api/city/config', methods=['GET'])
def get_city_config():
    return jsonify(city_manager.load_city_config())


@app.route('/api/city/config', methods=['POST'])
def save_city_config():
    config = request.json
    city_manager.save_city_config(config)
    return jsonify({'success': True})


@app.route('/api/city', methods=['POST'])
def add_city():
    city = request.json
    city_manager.add_city(city)
    return jsonify({'success': True})


@app.route('/api/city/<city_name>', methods=['PUT'])
def update_city(city_name):
    city_data = request.json
    city_manager.update_city(city_name, city_data)
    return jsonify({'success': True})


@app.route('/api/city/<city_name>', methods=['DELETE'])
def delete_city(city_name):
    city_manager.delete_city(city_name)
    return jsonify({'success': True})


@app.route('/')
def index():
    return send_from_directory('.', 'index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
