# -*- coding: utf-8 -*-

print("\n         ~(Celsius Converter)~\n")

print("                  By")
print("                 Ivan")
print("                Muzaqqa\n")

print("\n        ~{Celsius to Fahrenhait}~")
def GetFahrenhait(celsius):
	fahrenhait = celsius + 32
	sentence = ("      From {}°C to Fahrenhait is {}°F.\n").format(celsius, fahrenhait)
	print(sentence)

def fah():
	fahparam = int(input("\n       Input Celsius Temperature: "))
	GetFahrenhait(fahparam)

fah()

print("\n          ~{Celsius to Kelvin}~")

def GetKelvin(celsius):
	kelvin = celsius + 273.15
	sentence2 = ("      From {}°C to Kelvin is {} K.").format(celsius, kelvin)
	print(sentence2)

def kel():
	kelparam = int(input("\n       Input Celsius Temperature: "))
	GetKelvin(kelparam)

kel()

print("\n          ~{Celsius to Reaumur}~")

def GetReaumur(celsius):
	reaumur = celsius + 0.8
	sentence3 =("      From {}°C to Reaumur is {}°R.").format(celsius, reaumur)
	print(sentence3)

def rea():
	paramrea = int(input("\n       Input Celsius Temperature: "))
	GetReaumur(paramrea)

rea()