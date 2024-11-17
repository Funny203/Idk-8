from flask import Flask, render_template, url_for
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/random_fact")
def random_fact():
    facts_list=[
        'Большинство людей, страдающих технологической зависимостью, испытывают сильный стресс, когда они находятся вне зоны покрытия сети или не могут использовать свои устройства.',
        'Согласно исследованию, проведенному в 2018 году, более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов.',
        'Изучение технологической зависимости является одной из наиболее актуальных областей научных исследований в настоящее время.',
        'Согласно исследованию, проведенному в 2019 году, более 60% людей отвечают на рабочие сообщения в своих смартфонах в течение 15 минут после того, как они вышли с работы.',
        'Один из способов борьбы с технологической зависимостью - это поиск занятий, которые приносят удовольствие и улучшают настроение.',
        'Илон Маск утверждает, что социальные сети созданы для того, чтобы удерживать нас внутри платформы, чтобы мы тратили как можно больше времени на просмотр контента.',
        'Илон Маск также выступает за регулирование социальных сетей и защиту личных данных пользователей. Он утверждает, что социальные сети собирают огромное количество информации о нас, которую потом можно использовать для манипулирования нашими мыслями и поведением.',
        'Социальные сети имеют как позитивные, так и негативные стороны, и мы должны быть более осознанными в использовании этих платформ.'
    ]

    return f'<p>{random.choice(facts_list)}</p>'

app.run(debug=True)

@app.route('/random img')
def random_img():
    img_list=[
        'https://dk-energetik.shl.muzkult.ru/media/2020/06/09/1254754890/plakat3.jpg',
        'https://avatars.mds.yandex.net/i?id=58c3a1d373970dc733569643a5921590_l-5906867-images-thumbs&n=13',
        'https://edu.tatar.ru/upload/storage/org3391/files/%D0%9F%D1%80%D0%B8%D0%B7%D0%BD%D0%B0%D0%BA%D0%B8%20%D0%BA%D0%BE%D0%BC%D0%BF%D1%8C%D1%8E%D1%82%D0%B5%D1%80%D0%BD%D0%BE%D0%B9%20%D0%B7%D0%B0%D0%B2%D0%B8%D1%81%D0%B8%D0%BC%D1%81%D1%82%D0%B8.jpg'
    ]
    return f'<img src="{random.choice(img_list)}" width="500" height="500"'