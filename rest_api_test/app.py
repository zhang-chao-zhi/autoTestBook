# -*-coding:utf-8-*-

from flask import Flask, jsonify, abort, request

app = Flask(__name__)

articles = [
    {
        'id': 1,
        'title': u'三重门',
        'author': u'韩寒',
        'price': 20
    },
    {
        'id': 2,
        'title': u'黄金时代',
        'author': u'王小波',
        'price': 35
    }
]


@app.route('/my_app/api/v1/articles', methods=['GET'])
def get_articles():
    # 获取所有文章数据
    return jsonify({'articles': articles})


@app.route('/my_app/api/v1/articles/<int:id>', methods=['GET'])
def get_article_by_id(id):
    # 通过文章ID获取某篇文章
    for article in articles:
        if article['id'] == id:
            return jsonify({'article': article})
    abort(404)


@app.route('/my_app/api/v1/articles/', methods=['POST'])
def create_articles():
    # 创建文章
    if not request.form or not 'title' in request.form:
        abort(400)
    article = {
        'id': articles[-1]['id'] + 1,
        'title': request.form['title'],
        'author': request.form['author'],
        'price': request.form['price'],
    }
    articles.append(article)
    return jsonify({'book': article}), 200

@app.route('/my_app/api/v1/articles/<int:id>', methods=['PUT'])
def update_article_by_id(id):
    # 根据文章ID进行更新
    for article in articles:
        if article['id']==id:
            article["title"] = request.form['title']
            article["author"] = request.form['author']
            article["price"] = request.form['price']
        return jsonify({'result': "ok"})
    abort(400)


@app.route('/my_app/api/v1/articles/<int:id>', methods=['DELETE'])
def delete_article(id):
    # 删除指定文章
    for article in articles:
        if article['id'] == id:
            articles.remove(article)
            return jsonify({'result': True})
    abort(404)

    return jsonify({'result': True})
if __name__ == '__main__':
    app.run()
