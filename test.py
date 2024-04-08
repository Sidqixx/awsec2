from flask import Flask

app = Flask(__name__)

@app.route('/login')
def login():
    return 'Login endpoint'

@app.route('/home')
def home():
    return 'Home endpoint'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
