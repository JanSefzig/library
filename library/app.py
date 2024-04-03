from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)


def load_data():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {'books': [], 'users': []}
    return data


def save_data(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        data = load_data()
        data['users'].append(name)
        save_data(data)
        return redirect(url_for('index'))
    return render_template('add_user.html')

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        data = load_data()
        data['books'].append({'title': title, 'author': author})
        save_data(data)
        return redirect(url_for('index'))
    return render_template('add_book.html')

@app.route('/books')
def display_books():
    data = load_data()
    return render_template('books.html', books=data['books'])

@app.route('/users')
def display_users()
