from flask import Flask, render_template

app = Flask(__name__)

name = "OSOKINA MARRIA"
roles = [
    {"title": "Модель", "slug": "model"},
    {"title": "Студент-режиссер", "slug": "director"},
    {"title": "Младший продюсер", "slug": "producer"},
    {"title": "St. Petersburg", "slug": "st-petersburg"}
]

@app.route('/')
def index():
    return render_template('index.html', name=name, roles=roles)

@app.route('/portfolio/<category_slug>')
def portfolio_page(category_slug):
    current_role = next((role for role in roles if role['slug'] == category_slug), None)
    
    if current_role:
        return render_template('portfolio_detail.html', name=name, category=current_role)
    else:
        return "Категория не найдена", 404

if __name__ == '__main__':
    app.run(debug=True)