from newtune import AudioMaker
from processImage import SoulTempo
import json
import sys

class Main:

    def processData(self):
        with open(self.jsonreq) as jsonfile:
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
        return json.dumps(result)

    def __init__(self, jsonreq):
        self.jsonreq = jsonreq
