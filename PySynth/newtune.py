import pysynth as ps
from random import randint
from processImage import SoulTempo

st = SoulTempo("tiger.jpg")
data = st.segmentate()

cancion=[]

def createTune(list):
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
		cancion.append((result[x][0],notelength))




for x in range(0,len(data)):
	createTune(data[x])


ps.make_wav(cancion, fn = "pohaultimatum2.wav")
