"""

  SoulTempo
  Authors: Luis Alfredo León, Armando Canto, Luis Shafik, Ricardo Legaspi

"""


from processImage import SoulTempo

st = SoulTempo("tiger.jpg")

segmentData = st.segmentate()

#for i in range(0, len(segmentData)):
    #print(segmentData[i])
