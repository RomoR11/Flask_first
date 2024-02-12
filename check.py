from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index_2():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def prom():
    z = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
         'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    return '<br>'.join(z)


@app.route('/image_mars')
def image_mars():
    return render_template('image_mars.html')


@app.route('/promotion_image')
def promotion_image():
    return render_template('promotion_image.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
