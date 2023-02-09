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

@app.route("/promotion_image")
def promote_img():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.2.1/dist/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
                    <h1> Жди нас, Марс! </h1>          
                    <img src='{url_for('static', filename='img/MARS.png')}'>
                    <div class="alert alert-dark" role="alert">
                        Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-success" role="alert">
                        Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-secondary" role="alert">
                        Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-danger" role="alert">
                        И начнем с Марса!
                    </div>
                    <div class="alert alert-warning" role="alert">
                        Присоединяйся!
                    </div>
                  </body>
                </html>
    """

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
