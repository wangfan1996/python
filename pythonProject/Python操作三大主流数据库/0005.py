from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
    score = 50
    dict = {'phy': 50, 'che': 60, 'maths': 70}
    return render_template('name.html', name=name, marks=score, result=dict)


if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug=True)
