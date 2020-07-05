from application import app
from flask import request, render_template, url_for
import requests


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/generation', methods=['GET', 'POST'])
def generation():
    func1=requests.get('http://app2:5001/animal')
    animal=func1.text
    func2=requests.post('http://app2:5001/noise')
    noise=func2.text
    return render_template('generation.html', title='generate', animal=animal, noise=noise)
