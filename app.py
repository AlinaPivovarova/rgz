from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route('/')
def glavnaya():
    return render_template('index.html')