from processImage import SoulTempo

st = SoulTempo("vieja.jpg", "leonvillapun@gmail.com")
st.frombase64()
segmentData = st.segmentate()

st.tobase64()

st.toJSON()
#for i in range(0, len(segmentData)):
    #print(segmentData[i])
