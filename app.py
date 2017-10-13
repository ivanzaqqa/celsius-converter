from flask import Flask, render_template, jsonify, request
from convcel_controller import ConvcelController
app = Flask(__name__)

@app.route('/')
def index():
	return render_template ("index.html")

@app.route('/fahrenhait')
def fahrenhait():
	return render_template("fahrenhait.html")

@app.route('/kelvin')
def kelvin():
	return render_template("kelvin.html")

@app.route('/reaumur')
def reaumur():
	return render_template("reaumur.html")

@app.route('/result')
def resultend():
	return render_template("result.html")

# Celsius Converter

#get Fahrenhait
@app.route('/fahrenhait', methods=['POST'])
def getFahrenhait():
	return ConvcelController.getFahrenhait(request)

@app.route('/kelvin', methods=['POST'])
def getKelvin():
	return ConvcelController.getKelvin(request)

@app.route('/reaumur', methods=['POST'])
def getReaumur():
	return ConvcelController.getReaumur(request)

if __name__ == '__main__':
	app.run(debug=True)