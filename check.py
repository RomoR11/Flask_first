from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


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


@app.route('/training/<prof>')
def profession(prof):
    return render_template('profession.html', prof=prof)


@app.route('/list_prof/<marker>')
def list_prof(marker):
    professions = ['Пилот', 'Штурман', 'Врач', 'Повар', 'Инженер-механник', 'Строитель', 'Ученый', 'Айтишник']
    params = {'list': professions, 'mk': marker}
    return render_template('list_prof.html', **params)


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def selection():
    if request.method == 'GET':
        return render_template('astronaut_selection.html')
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['education'])
        print(request.form['sex'])
        print(request.form['about'])
        print(request.form['file'])
        print(request.form['agreement'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
