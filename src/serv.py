#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bottle import get, post, request, run, route, template, static_file
from query import list_activity, find_activity_from_city_zip_code, get_city

@get('/index')
def index():
    """
        function than return the home page template
        :return: index.tpl
    """
    return template('website/index')

@get('/search')
def index():
    """
        function than return the search page template and the list of available activity
        :return: search.tpl and activity list
    """
    return template('website/search', activity =list_activity() )

@post('/result')
def do_post():
    """
        function than return the result page template and the form result.
        :return: result.tpl and activity list or city list
    """
    result = request.forms.get('activity')
    if result is None:
        return template('website/result', listeResult = find_activity_from_city_zip_code(request.forms.get('city')))
    else:
        return template('website/result', listeResult = get_city(request.forms.get('activities')))

@route("/website/theme/<filename>")
def style(filename):
    """
        function than return css path files 
    """
    return static_file(filename, root='website/theme/')

@route("/website/img/<filename>")
def img(filename):
    """
        function than return image path files 
    """
    return static_file(filename,root="website/img/")

@route("/website/bootstrap/<filename>")
def script(filename):
    """
        function than return bootstrap path files 
    """
    return static_file(filename, root='website/bootstrap/')

@route("/website/fonts/<filename>")
def fonts(filename):
    """
        function than return fonts path files 
    """
    return static_file(filename, root='website/fonts/')

run(host='localhost', port=8085)
