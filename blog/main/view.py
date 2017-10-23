# -*- coding: utf-8 -*-
"""
    Flaskr
    ~~~~~~

    A microblog example application written as Flask tutorial with
    Flask and sqlite3.

    :copyright: (c) 2015 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""
from functools import wraps

from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash, jsonify, current_app

from blog.db import DbBoke
from blog.main import api
from blog.model import Boke


def login_check(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = request.headers.get('token')
        if not token:
            return jsonify({'code': 0, 'message': '需要验证'})

        phone_number = current_app.redis.get('token:%s' % token)
        if not phone_number or token != current_app.redis.hget('user:%s' % phone_number, 'token'):
            return jsonify({'code': 2, 'message': '验证信息错误'})

        return f(*args, **kwargs)

    return decorator

@api.before_request
def init_session():
    g.db_boke = DbBoke()


@api.teardown_request
def close_session(exception):
    g.db_boke.db_session.close()


@api.route('/')
def show_entries():
    entries = g.db_boke.getAll()
    return render_template('show_entries.html', entries=entries)


@api.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db_boke.add(Boke(title=request.form['title'], text=request.form['text']))
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


@api.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != api.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != api.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@api.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))
