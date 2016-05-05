# -*- coding: utf-8 -*-

from . import main
from flask import  render_template


@main.route('/', methods=['GET', 'POST'])
@main.route('/index', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@main.route('/blogs', methods=['GET', 'POST'])
def blog_list():
    return render_template('blog.html')


@main.route('/blog/<id>', methods=['GET', 'POST'])
def get_blog(id):
    return render_template('blog.html')