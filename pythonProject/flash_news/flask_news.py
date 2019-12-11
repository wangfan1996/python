from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import NewsForm
from datetime import datetime
import random
from flask import request


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/flask_news'
app.config["SECRET_KEY"] = '123456'
db = SQLAlchemy(app)


class News(db.Model):
    __table_name = 'news'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.String(200), nullable=False)
    types = db.Column(db.String(10), nullable=False)
    image = db.Column(db.String(300))
    author = db.Column(db.String(20))
    view_count = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    is_valid = db.Column(db.Boolean)

    def __repr__(self):
        return '<News %s %r>' % (self.id, self.title)


@app.route('/')
def index():
    # 新闻首页
    news_list = News.query.filter(News.is_valid == 1)
    return render_template('index.html', news_list=news_list)


@app.route('/cat/<name>')
def cat(name):
    # 新闻类别 查询类别为name的数据
    news_list = News.query.filter(News.types == name)
    return render_template('cat.html', name=name, news_list=news_list)


@app.route('/detail/<int:pk>')
def detail(pk):
    # 新闻详情
    new_obj = News.query.get(pk)
    return render_template('detail.html', pk=pk, new_obj=new_obj)


@app.route('/admin/')
@app.route('/admin/<int:page>')
def admin(page=None):
    if page is None:
        page = 1
    news_list = News.query.filter(News.is_valid == 1).paginate(page=page, per_page=3)
    return render_template('admin/index.html', news_list=news_list)


@app.route('/update/<int:pk>')
def update(pk):
    new_obj = News.query.get(pk)
    return render_template('admin/update.html', pk=pk, new_obj=new_obj)


@app.route('/add/', methods=['GET', 'POST'])
def add():
    # pip install Flask-WTF
    form = NewsForm()
    if request.method == 'POST':
        new_obj = News(
            title=form.title.data,
            content=form.content.data,
            types=form.types.data,
            image=form.image.data,
            author=random.sample(['张三', '李四', '王五', '路人甲'], 1)[0],
            created_at=datetime.now(),
            is_valid=int(form.is_valid.data),
            view_count=random.randint(0, 100)
        )
        db.session.add(new_obj)
        db.session.commit()
        return redirect(url_for('admin'))

    return render_template('admin/add.html', form=form)


@app.route('/delete/<int:pk>', methods=['POST'])
def delete(pk):
    new_obj = News.query.get(pk)
    if not new_obj:
        return 'no'

    new_obj.is_valid = 0
    db.session.add(new_obj)
    db.session.commit()
    return 'yes'


if __name__ == '__main__':
    app.run(debug=True)

# 创建表
# 进入python命令行
# from flask_news import db
# db.create_all()
# 参考链接 http://www.pythondoc.com/flask-sqlalchemy/quickstart.html
