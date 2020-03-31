from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/mypage')
def mypage():
    return render_template('mypage.html')

@app.route('/airpods')
def airpods():
    return render_template('airpods.html')


if __name__ == '__main__':
    app.run('127.0.0.1', port=3000, debug=True)
