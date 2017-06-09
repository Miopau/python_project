#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bottle import get, post, request, run, route, template, static_file
from database_script import list_activity, find_activity_from_city_zip_code, get_city
@get('/index')
def index():
    return template('website/index')

@get('/search')
def index():
    return template('website/search', list =list_activity() )

@post('/result')
def do_post():
    res = request.forms.get('var')
    print res
    if res is None:
        return template('website/result', liste = find_activity_from_city_zip_code(request.forms.get('city')))
    else:
        return template('website/result', liste = get_city(request.forms.get('var')))

@route("/website/theme/<filename>")
def style(filename):
    return static_file(filename, root='website/theme/')

@route("/website/img/<filename>")
def img(filename):
    return static_file(filename,root="website/img/")

@route("/website/bootstrap/<filename>")
def script(filename):
    return static_file(filename, root='website/bootstrap/')

@route("/website/fonts/<filename>")
def fonts(filename):
    return static_file(filename, root='website/fonts/')

run(host='localhost', port=8085)
