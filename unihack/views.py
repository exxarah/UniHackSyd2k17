"""Define Views and Routes for Front End App."""

from flask import render_template
from unihack import app


@app.route('/')
@app.route('/home' )
def home():
    """Route for homepage."""
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    """404 Page Not Found."""
    return render_template('404.html'), 404



@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r
