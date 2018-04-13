"""

  SoulTempo
  Authors: Luis Alfredo León, Armando Canto, Luis Shafik, Ricardo Legaspi

"""

#Import libraries
import numpy as np
import cv2
import matplotlib
import random
import math

#Define class Segment
class Segment:
    #Initialize class
    def __init__(self, image, rConcentration, gConcentration, bConcentration):
        #Read the image
        self.image = image
        self.rConcentration = None
        self.gConcentration = None
        self.bConcentration = None
    #End constructor

    #Method that saves the image of the segment
    def saveimg(self, name):
        cv2.imwrite(name, self.image)
    #End saveimg

    def countcolors(self):
        rConcentration = 0
        gConcentration = 0
        bConcentration = 0
        #Iterate through the pixel matrix
        for i in range(0,len(self.image) - 1):
            for j in range(0, len(self.image[0] - 1)):
                

#End of class Segment

#Define Class SoulTempo
class SoulTempo:

    #Method to segmentate the image into random pieces.
    def segmentate(self):
        segments = []
        numsegments = random.randint(1, 5) #Generate the number of segments
        #math.sqrt(len(image).astype(int))
        print(len(self.image))
        print(numsegments)
        increment = int(len(self.image) / numsegments)
        print(increment)
        act = 0

        imageSeg = np.zeros((increment,len(self.image[0]),3), np.uint8)

        for i in range(0,numsegments):
            seg = Segment(imageSeg, 0 , 0, 0)
            segments.append(seg)

        #Send corresponding pixels to image
        x = 0 #Original pic indexes
        y = 0 #Original pic indexes
        for i in range(0, len(segments)):
            for a in range(0, increment - 1):
                for b in range(0, len(self.image[0]) - 1):
                    print(a,b,x,y)
                    segments[i].image[a,b] = self.image[x,y]
                    y = y + 1
                x = x + 1
                y = 0
            segments[i].saveimg("seg"+str(i)+".jpg") #Save the images
        return segments
    #End method segmentate()



    #Initialize class
    def __init__(self, impath):
        #Read the image
        self.image = cv2.imread(impath) #Replace for impath
    #End constructor


#End of class SoulTempo
