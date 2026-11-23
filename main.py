from flask import Flask, render_template, request
import database_manager as dbHandler
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    featured_sharks = dbHandler.listShark()[:3]
    return render_template('home.html', featured=featured_sharks)

@app.route('/explore', methods=['GET', 'POST'])
@app.route('/index.html', methods=['GET', 'POST'])
def index():
    # Check if a conservation_status filter was passed in the URL
    conservation_status = request.args.get("conservation_status")

    if conservation_status and conservation_status != "All":
        data = dbHandler.listSpeciesByConservationStatus(conservation_status)
    else:
        # 1. Fetch shark data using database manager
        data = dbHandler.listShark()

    # 2. Pass it into the template under the variable name 'content'
    return render_template('index.html', content=data)

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