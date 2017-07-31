from flask import Flask, render_template
app = Flask(__name__)

@app.route('/main')
def main():
    return render_template('index.html')
    
"""https://code.tutsplus.com/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972"""

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run()