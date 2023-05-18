"""
Routes and views for the bottle application.
"""

from bottle import route, view
from datetime import datetime
import json


@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )

@route('/feedbackR')
@route('/feedbackPY')
@view('feedbackV')
def home():
    
    return dict(
        title='Contact',
        message='Your contact page.',
        year=datetime.now().year,
        feedbackD = {}
        )

@route('/article')
@view('article')
def feedback():
    return dict(
        title='Contact',
        message='Your contact page.',
        year=datetime.now().year
    )

