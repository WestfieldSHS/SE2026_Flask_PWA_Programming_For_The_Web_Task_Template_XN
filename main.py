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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
