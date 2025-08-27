from flask import Blueprint, render_template, redirect, request
from traitlets import link
from .extensions import db
from .models import Link 

main = Blueprint('main', __name__)

@main.route('/<short_url>')
def redirect_short_url(short_url):
    url = Link.query.filter_by(short_url=short_url).first_or_404()
    url.views += 1
    db.session.commit()
    return redirect(url.original_url)

@main.route('/create_short_url', methods=['POST'])
def create_short_url():
    original_url = request.form['original_url']
    url = Link(original_url=original_url)
    db.session.add(url)
    db.session.commit()
    return render_template('url_success.html', new_url=url.short_url, original_url=url.original_url)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/analytics')
def analytics():
    return ""

@main.errorhandler(404)
def not_found(e):
    return "<h1>404 - Page Not Found</h1>", 404


