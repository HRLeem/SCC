from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.dbsparta


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/order', methods=['POST'])
def insert_order():
    name_receive = request.form['name_give']
    quantity_receive = request.form['quantity_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']

    # DB에 삽입할 객체 설정
    order_now = {
        'name': name_receive
        , 'quantity': quantity_receive
        , 'address': address_receive
        , 'phone': phone_receive
    }
    # order 객체 저장
    db.order.insert_one(order_now)
    return jsonify({'result': 'success', 'msg': '주문이 완료되었습니다!'})


# 처음에 DB 읽어서 가져오는 함수 따로 빼놓기
@app.route('/take_orders', methods=['GET'])
def take_orders():
    orders = list(db.order.find({},{'_id':0}))
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('127.0.0.1', port=1199, debug=True)
