from flask import Flask, render_template
from app.graph import get_graph_data

app = Flask(__name__)

@app.route('/plot')
def plot():
	return render_template('plot.html', data=get_graph_data())

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')
