from flask import Flask
from flask import request
from flask import render_template


def page_not_found(e):
    return render_template('404.html'), 404


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.register_error_handler(404, page_not_found)
    return app

app = create_app()


# Routing
@app.route('/')
def index():
    return 'index'


@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'


# GET/POST/DELETE
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "Handle Login"
    else:
        return "show login page"


@app.get('/blogs')
def blogs_get():
    return "show All Blogs"


# @app.post('/home')
# def blogs_post():
#     return "Show Blog with BlogID"


# Error handling

# @app.errorhandler(404)
# def page_not_found(e):
#     # note that we set the 404 status explicitly
#     return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    # note that we set the 500 status explicitly
    return render_template('500.html'), 500
