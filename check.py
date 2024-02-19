from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField, FileField, RadioField, SelectMultipleField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'egor-moshennik'
professions = ['Пилот', 'Штурман', 'Врач', 'Повар', 'Инженер-механник', 'Строитель', 'Ученый', 'Айтишник']


class LoginForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    email = StringField('Адрес почты', validators=[DataRequired()])
    education = SelectField('Какое у вас образование?', choices=[('Начальное общее', 'Начальное общее'),
                                                                 ('Основное общее', 'Основное общее'),
                                                                 ('Среднее общее', 'Среднее общее'),
                                                                 ('Среднее профессиональное', 'Среднее профессиональное'),
                                                                 ('Высшее', 'Высшее')])
    prof = SelectMultipleField('Какие у вас профессии?', choices=[(i, i) for i in professions])
    sex = RadioField('Выберите пол', choices=[('м', 'Мужской'), ('ж', 'Женский')])
    about = StringField('Почему вы хотите принять участие в миссии?', validators=[DataRequired()])
    file = FileField('Приложите фотографию')
    agreement = BooleanField('Готовы ли остаться на Марсе?', validators=[DataRequired()])
    submit = SubmitField('Отправить')


@app.route('/login', methods=['POST', 'GET'])
@app.route('/answer')
@app.route('/auto_answer')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        info = {'name': form.name.data, 'surname': form.surname.data, 'email': form.email.data,
                'education': form.education.data, 'prof': form.prof.data, 'sex': form.sex.data,
                'agreement': form.agreement.data}
        return render_template('answer.html', info=info)
    return render_template('boost_selection.html', form=form)


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
    global professions
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
