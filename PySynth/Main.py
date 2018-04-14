from newtune import AudioMaker
from processImage import SoulTempo
import json
import sys

with open('pruebaIn.json') as jsonfile:
    data = json.load(jsonfile) #sys.argv[1]

st = SoulTempo(data['base64img'], data['mail'])
st.frombase64() #Generate image as opencv readable

#Now we make the Audio

am = AudioMaker(data['base64img'], data['mail'], st)
am.makeAudio(am.segments)
am.tobase64()

# Generate some data to send to PHP
result = am.toJSON()

# Send it to stdout (to PHP)
print (json.dumps(result))
