from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route('/index')
def norm():
    return "И на Марсе будут яблони цвести!"


@app.route("/promotion")
def reklama():
    return "<p>Человечество вырастает из детства.</p> <p>Человечеству мала одна планета.</p> <p>Мы сделаем обитаемыми безжизненные пока планеты.</p> <p>И начнем с Марса!</p> <p>Присоединяйся!</p>"

@app.route("/image_mars")
def img():
    return f"""
    <h1> Жди нас Марс! </h1>
    <img src='{url_for('static', filename='img/MARS.png')}'>
    <p> Вот какая она красная планета</p>
    """
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
