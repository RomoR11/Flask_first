from flask import Flask

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
    with open('image_mars.html', mode='r', encoding='utf-8') as html_file:
        data = html_file.read()
    return data


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
