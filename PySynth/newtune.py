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
	mypink = 'b'
	mywhite = 'a#'
	myblack = 'a'
	mygray = 'a'
	myorange = ''


	mydestEstR = 0
	mydestEstG = 0
	mydestEstB = 0
	myprom = 0
	mymediana = 0
	mymoda = 0
	notelength = 0


	if list[0] > 0.1:
		myblue = 'g#'
	else:
		myblue = 'g'

	if list[1] > 0.1:
		mygreen = 'f'
	else:
		mygreen = 'e'

	if list[2] > 0.1:
		myviolet = 'a#'
	else:
		myviolet = 'b'

	if list[3] > 0.1:
		myred = 'c#'
	else:
		myred = 'c'


	if list[8] > 0.1:
		myorange = 'd'
	else:
		myorange = 'd#'

	rand = randint(1,3)
	listcolors=[]
	newresult =[]



	for x in range(0,9):
		listcolors.append(list[x])

	average = sum(listcolors)/len(listcolors)

	if average > 0.5:
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
