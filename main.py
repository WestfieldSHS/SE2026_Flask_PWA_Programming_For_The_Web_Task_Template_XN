from flask import Flask, render_template, request
import database_manager as dbHandler
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/explore', methods=['GET', 'POST'])
@app.route('/index.html', methods=['GET', 'POST'])
def index():
    category = request.args.get("category", "all")
    conservation_status = request.args.get("conservation_status", "All")
    search_query = request.args.get("q", "").strip()

    data = dbHandler.getSpecies(category, conservation_status, search_query)

    return render_template(
        'index.html',
        content=data,
        active_category=category,
        active_status=conservation_status,
        search_query=search_query
    )

@app.route('/add.html', methods=['POST', 'GET'])
def add():
    """Handle the contact form page."""
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']

        try:
            dbHandler.insertContact(email, name)
            return render_template('add.html', is_done=True)

        except sqlite3.IntegrityError:
            error_message = "This email address is already subscribed. Please use a different email."
            return render_template('add.html', error=error_message, email=email, name=name)

    else:
        return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)