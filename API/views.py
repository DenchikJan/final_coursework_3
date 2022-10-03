# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify
from json import JSONDecodeError
from utils import Posts, Comments
import logging

api_logger = logging.getLogger()

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("logs/api.log")

console_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.DEBUG)

formatter_one = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

console_handler.setFormatter(formatter_one)
file_handler.setFormatter(formatter_one)

api_logger.addHandler(console_handler)
api_logger.addHandler(file_handler)

api_blueprint = Blueprint('api_blueprint', __name__, template_folder='templates')

file_posts = 'data/posts.json'
file_comments = 'data/comments.json'

try:
    class_posts = Posts(file_posts)
    class_comments = Comments(file_comments)
except FileNotFoundError:
    @api_blueprint.route('/posts')
    def error():
        return f'<a>Файл не найден</a>'
except JSONDecodeError:
    @api_blueprint.route('/posts')
    def error():
        return f'<a>Файл не удается преобразовать</a>'


@api_blueprint.route('/posts')
def posts_all_api():
    """Выводит json всех постов"""
    api_logger.info("Запрос /api/posts")
    posts = class_posts.get_posts_all()
    return jsonify(posts)


@api_blueprint.route('/posts/<int:pk>')
def post_by_pk(pk):
    """Выводит json поста по id"""
    post = class_posts.get_post_by_pk(pk)
    api_logger.info(f"Запрос /api/posts/{pk}")
    return jsonify(post)


@api_blueprint.route('/comments/<int:pk>')
def comments_by_post_id(post_id):
    """Выводит json коментариые к посту по id"""
    comments = class_comments.get_comments_by_post_id(post_id, class_posts.unique_post_id)
    api_logger.info(f"Запрос /api/comments/{post_id}")
    return jsonify(comments)
