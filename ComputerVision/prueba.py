from processImage import SoulTempo

st = SoulTempo("tiger.jpg")

segments = st.segmentate()

print(segments)
