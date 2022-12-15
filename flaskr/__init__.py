from flask import Flask, \
    redirect, \
    request, \
    url_for, \
    render_template, \
    make_response, \
    session
import logging
from . import constants


def page_not_found(e):
    return render_template('404.html'), 404


def create_app(test_config=None):
    # create and configure the app
    flask_app = Flask(__name__)
    flask_app.register_error_handler(404, page_not_found)

    flask_app.logger.setLevel(logging.INFO)

    # Test Log levels
    flask_app.logger.debug("debug log info")
    flask_app.logger.info("Info log information")
    flask_app.logger.warning("Warning log info")
    flask_app.logger.error("Error log info")
    flask_app.logger.critical("Critical log info")

    # Set the secret key to some random bytes. Keep this really secret!
    flask_app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    return flask_app


app = create_app()


# Routing
@app.route('/')
def index():
    return show_home()


@app.route('/home')
def show_home():
    if is_logged_in():
        return render_template('index.html', name=session[constants.SESSION_USERNAME])
    else:
        return render_template('index.html')


# Session check user logged in
def is_logged_in():
    return constants.SESSION_USERNAME in session


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop(constants.SESSION_USERNAME, None)
    # go back to home page
    return redirect(url_for('show_home'))


# GET/POST/DELETE
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if is_logged_in():
            return redirect(url_for('show_home'))
        else:
            return show_the_login_form()

    elif request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()


def valid_login(username, password):
    return username == 'hits' and password == "pass"


def do_the_login():
    username = request.form['username']
    password = request.form['password']

    if valid_login(username, password):
        session[constants.SESSION_USERNAME] = username
        return redirect(url_for('show_profile', username=username))
    else:
        error = 'Invalid username/password'
        # the code below is executed if the request method
        # was GET or the credentials were invalid
        return show_the_login_form(error=error)


def show_the_login_form(error=None):
    return render_template('login.html', error=error)


@app.route('/profile/<username>')
def show_profile(username):
    return render_template('profile.html', name=username, )


@app.get('/blogs')
def blogs_get():
    return "show All Blogs"


# Redirect using url for

@app.route('/admin')
def hello_admin():
    return 'Hello Admin'


@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest


@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))


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
    resp = make_response(render_template('error.html'), 500)
    resp.headers['X-Something'] = 'A value'
    return resp
