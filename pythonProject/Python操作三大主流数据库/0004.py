from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
    str_name = 'welcome %s' % name
    return str_name


@app.route('/login', methods=['POST', 'GET'])
def login():
   if request.method == 'POST':
       user_str = request.form['nm']
       return redirect(url_for('success', name=user_str))
   else:
       user = request.args.get('nm')
       return redirect(url_for('success', name=user))


if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug=True)
