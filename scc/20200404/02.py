from flask import Flask, render_template, jsonify, request
app = Flask(__name__)
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta


# HTML 을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')


# API 역할을 하는 부분
@app.route('/reviews', methods=['POST'])
def write_review():
    title_receive = request.form['title_give']
    author_receive = request.form['author_give']
    review_receive = request.form['review_give']

    # DB 에 삽입할 review 만들기
    review = {
        'title' : title_receive,
        'author' : author_receive,
        'review' : review_receive
    }
    # reviews 에 저장하기
    db.reviews.insert_one(review)
    return jsonify({'result': 'success', 'msg': '이 요청은 POST!'})


@app.route('/reviews', methods=['GET'])
def read_reviews():
    return jsonify({'result': 'success', 'msg': '이 요청은 GET!'})


if __name__ == '__main__':
    app.run('127.0.0.1', port=3000, debug=True)
