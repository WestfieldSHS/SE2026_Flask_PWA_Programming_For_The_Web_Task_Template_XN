from flask import Flask, render_template, request
import database_manager as dbHandler

app = Flask(__name__)

@app.route('/index.html', methods=['GET'])     # Only GET - just viewing
@app.route('/', methods=['POST', 'GET'])       # Both GET and POST - can handle forms
def index():
    # 1. Fetch shark data using database manager
    data = dbHandler.listShark()
    
    # 2. Pass it into the template under the variable name 'content'
    return render_template('index.html', content=data)

@app.route('/add.html', methods=['POST', 'GET']) #methods=['GET'] -> show form when user visit /add.html
                                                 #methods=['POST'] -> process data when user submits the form 
#Decorator tells Flask: "This function handles requesrs to 'add.html"
def add():
    """Handle the contact form page.
    
    GET request: Display empty form
    POST request: Process form submission and display confirmation
    """
    if request.method == 'POST':
        #check which HTTP method was used
        """HTTP method is a command sent by a client to perform particular action on a specific resource
        GET, PUT, POST, DELETE, PATCH, HEAD, CONNECT, OPTIONS, TRACE"""
        email = request.form['email']
        name = request.form['name']
        #form submitted - extract data

        dbHandler.insertContact(email, name)
        #insert into database

        return render_template('/add.html', is_done=True) 
        # is_done=True tells Jinja2 to show success message
    else:
        #GET request - display empty form
        return render_template('/add.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

