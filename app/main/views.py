# -*- coding: utf-8 -*-

from . import main
from flask import request, render_template, jsonify, current_app
from app.models import Keywords, Blog, Topic



@main.route('/', methods=['GET', 'POST'])
@main.route('/index', methods=['GET', 'POST'])
def home():
    """
        The same strategy is used for the lookup than for the
        shortening. Here a None reply will imply either an
        error or a wrong code.
    """
    page = request.args.get('page', 1, type=int)
    pagination = Blog.query.order_by(Blog.create_time.desc()).paginate(page,
                            per_page=current_app.config['BLOG_LIST_PER_PAGE'], error_out=False)
    blogs = pagination.items

    return render_template('home.html', blogs=blogs, pagination=pagination, pageNum=pagination.pages)


@main.route('/blogs', methods=['GET'])
def blog_list():

    page = request.args.get('page', 1, type=int)
    pagination = Blog.query.order_by(Blog.create_time.desc()).paginate(page,
                            per_page=current_app.config['BLOG_LIST_PER_PAGE'], error_out=False)
    blogs = pagination.items

    return render_template('blog.html', blogs=blogs, pagination=pagination, pageNum=pagination.pages)


@main.route('/blogs/search', methods=['GET', 'POST'])
def search_blog_by_title():

    return render_template('home.html')


@main.route('/blog/add', methods=['GET', 'POST'])
def add_blog():

    if request.method == 'GET':
        return render_template('add_blog.html')

    blog = Blog()

    title = request.form.get('title', '', type=str)
    topic_id = request.form.get('topic_id', -1, type=int)

    topic = Topic.query.get(topic_id)
    content = request.form.get('content', '', type=str)
    brief = request.form.get('brief', '', type=str)

    blog.title = title
    blog.brief = brief
    blog.content = content
    blog.topic = topic

    blog.save()

    return jsonify({'status':200, 'blog':blog.to_json()})


@main.route('/blog/edit/<id>', methods=['GET', 'POST'])
def edit_blog(id):

    blog_id = request.form.get('blog_id', -1, type=int)

    if request.method == 'GET':

        blog = Blog.query.get(blog_id)
        return render_template('edit_blog.html', blog=blog)

    blog = Blog.query.get(blog_id)

    title = request.form.get('title', '', type=str)
    topic_id = request.form.get('topic_id', -1, type=int)

    topic = Topic.query.get(topic_id)
    content = request.form.get('content', '', type=str)
    brief = request.form.get('brief', '', type=str)

    blog.title = title
    blog.brief = brief
    blog.content = content
    blog.topic = topic

    blog.update()

    return jsonify({'status':200, 'blog':blog.to_json()})



@main.route('/blog/<id>', methods=['GET', 'POST'])
def get_blog(id):

    blog_id = request.form.get('blog_id', -1, type=int)

    blog = Blog.query.get(blog_id)

    return render_template('blog.html', blog=blog)


@main.route('/blog/topic', methods=['GET'])
def topic_list():

    return render_template('')


@main.route('/blog/topic/<id>', methods=['GET'])
def get_topic(id):

    return render_template('')


@main.route('/blog/topic/list', methods=['GET'])
def keyword_list():
    return render_template('')


@main.route('/blog/keyword', methods=['GET'])
def get_keyword():
    return render_template('')