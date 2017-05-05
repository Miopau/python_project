#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bottle import get, post, request, run, route, template, static_file


@get('/index')
def index():
    return template('website/index')

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
