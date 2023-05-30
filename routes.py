"""
Routes and views for the bottle application.
"""

from bottle import route, view, template
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
def feedback():
    return dict(
        title='Contact',
        message='Your contact page.',
        year=datetime.now().year,
        error = "", 
        errorCheck ={"", ""}
        )

@route('/article')
@view('article')
def article():
    return dict(
        title='Contact',
        message='Your contact page.',
        year=datetime.now().year, 
        titleArticle = '',
        article = '',
        urlArticle = '',
        name = '',
        email = '',
        phone = '',
        state = 0, 
        error = ''
    )
