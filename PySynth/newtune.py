import pysynth as ps
from random import randint
from processImage import SoulTempo
import base64
import json

class AudioMaker:

	def stringToBase64(self, s):
		return base64.b64encode(s.encode('utf-8'))

	def base64ToString(self,b):
		return base64.b64decode.decode(b, mode='rb', encoding=None)

	#Method to convert to JSON
	def toJSON(self):
		data = {}

		imgStr = self.base64img
		audioStr = self.base64audio

		print(type(imgStr))

		print(type(audioStr))

		data['base64img'] = imgStr
		data['base64audio'] = str(audioStr)
		data['mail'] = self.mail
		json_data = json.dumps(data)

		return json_data
	#End method

	#Method to convert to base64
	def tobase64(self):
		binary_data = self.audio.read()
		self.base64audio=base64.b64encode(binary_data)
		self.audio.close()
	#End to base64

	#Method to convert from base64
	def frombase64(self):
		self.audio = None #b64decode(self.base64audio)
	#End from base64

	def createTune(self, list):
		myblue = ''
		mygreen = ''
		myviolet = ''
		myred = ''
		mypink = ''
		mywhite = ''
		myblack = ''
		mygray = 'a'
		myorange = ''


		mydestEstR = 0
		mydestEstG = 0
		mydestEstB = 0
		myprom = 0
		mymediana = 0
		mymoda = 0
		notelength = 0


		if list[0] > 0.05:
			myblue = 'g#4'
		else:
			myblue = 'g5'

		if list[1] > 0.05:
			mygreen = 'e1'
		else:
			mygreen = 'E0'

		if list[2] > 0.05:
			myviolet = 'a#5'
		else:
			myviolet = 'b5'

		if list[3] > 0.05:
			myred = 'c#3'
		else:
			myred = 'c3'

		if list[8] > 0.05:
			myorange = 'd4'
		else:
			myorange = 'd#4'

		if list[5] > 0.05:
			mywhite = 'B4'
		else:
			mywhite = 'B3'

		if list[6] > 0.05:
			myblack = 'a1'
		else:
			myblack = 'a0'

		if list[4] > 0.05:
			mypink = 'b6'
		else:
			mypink = 'b5'

		rand = randint(1,4)
		listcolors=[]
		newresult =[]



		for x in range(0,9):
			listcolors.append(list[x])

		average = sum(listcolors)/len(listcolors)
		print("avg")
		print(average)

		if average > 0.11100:
			notelength = -8
		else:
			notelength = -4


		list2= [myblue,mygreen,myviolet,myred,mypink,mywhite,myblack,mygray,myorange]
		result = sorted(zip(list2, listcolors), reverse=True)[:rand]


		for x in range(0,rand):
			self.cancion.append((result[x][0],notelength))



	#Method that iterates though the image slices to create the parts of the tune
	def makeAudio(self, dataAudio):
		for x in range(0,len(dataAudio)):
			self.createTune(dataAudio[x])

		ps.make_wav(self.cancion, fn = "song" + str(self.mail) + ".wav")
		self.audio = open("song" + str(self.mail) +".wav", mode='rb', encoding=None)
	#End method

	#Start constructor
	def __init__(self, base64img, mail, soultempo):
		self.base64img = base64img
		self.mail = mail
		self.soultempo = soultempo
		self.segments = self.soultempo.segmentate()
		self.cancion=[]

	#End constructor

#End AudioMaker
