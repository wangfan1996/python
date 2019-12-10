from flask import Flask
from flask import redirect
from flask import url_for
app = Flask(__name__)


@app.route('/admin')
def hello_admin():
    hello_str = "Hello Admin"
    return hello_str


@app.route('/guest/<guest>')
def hello_guest(guest):
    hello_str = 'Hello %s as Guest' % guest
    return hello_str


@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))


if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug=True)
