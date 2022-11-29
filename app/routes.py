from app import app
from flask import render_template

@app.route('/')
@app.route('/home')
def home():
    title = "My Favorite Basketball Players"
    return render_template('index.html', header=title)

@app.route('/list')
def list():
    athletes = ['Michael Jordan', 'Lebron James', 'Kobe Bryant', 'Steph Curry', 'Tracy McGrady' ]
    return render_template('list.html', names=athletes)