from flask import Flask, render_template, request, session
from flask import flash, redirect, url_for, g

import config_flask

DATABASE = config_flask.DATABASE

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True)

