# -*- coding: utf-8 -*-

from . import main


@main.route('/', methods=['GET', 'POST'])
@main.route('/index', methods=['GET', 'POST'])
def hello_world():
    return 'Hello world'