from flask import Flask
from flask import jsonify

class ConvcelController():


	def getFahrenhait(request):
		result = request.json['temperature']
		fahrenhait = result + 32
		response = {}
		response["result"] = fahrenhait
		return jsonify(response)

	def getKelvin(request):
		result = request.json['temperature']
		kelvin = result + 273.15
		response = { "Result" : kelvin }
		return jsonify(response)

	def getReaumur(request):
		result = request.json['temperature']
		reaumur = result * 0.8
		response = { "Result" : reaumur}
		return jsonify(response)