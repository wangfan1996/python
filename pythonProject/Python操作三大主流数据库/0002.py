from flask import Flask
app = Flask(__name__)


@app.route('/<int:age>')
def hello_word(age):
    return '%d' % age


@app.route('/version/<float:rev>')
def revison(rev):
    return 'version: %f' % rev


if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug=True)

