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
from knnLuis import ColorDetector
#Define class Segment
class Segment:
    #Initialize class
    def __init__(self, image, rConcentration, gConcentration, bConcentration):
        #Read the image
        self.image = image
    #End constructor

    def __repr__(self):
        return str(self.__dict__)

    #Method that saves the image of the segment
    def saveimg(self, name):
        cv2.imwrite(name, self.image)
    #End saveimg

    #Method that calculates the color statistics in a given image section
    def countcolors(self):
        self.red = 0
        self.blue = 0
        self.green = 0
        self.violet = 0
        self.white = 0
        self.black = 0
        self.pink = 0
        self.yellow = 0
        self.gray = 0

        self.redSat = 0
        self.greenSat = 0
        self.blueSat = 0
        self.total = 0
        self.cd = ColorDetector()

        #Iterate through the pixel matrix
        for i in range(0,len(self.image) - 1):
            for j in range(0, len(self.image[0] - 1)):
                self.color = self.cd.predict(self.image[i,j,0], self.image[i,j,1], self.image[i,j,2])
                if self.color[0] == 'Red':
                    self.red = self.red + 1
                if self.color[0] == 'Blue':
                    self.blue = self.blue + 1
                if self.color[0] == 'Green':
                    self.green = self.green + 1
                if self.color[0] == 'Violet':
                    self.violet = self.violet + 1
                if self.color[0] == 'White':
                    self.white = self.white + 1
                if self.color[0] == 'Black':
                    self.black = self.black + 1
                if self.color[0] == 'Pink':
                    self.pink = self.pink + 1
                if self.color[0] == 'Yellow':
                    self.yellow = self.yellow + 1
                if self.color[0] == 'Gray':
                    self.gray = self.gray + 1
                self.total = self.total + 1

        #Normalize
        self.red = self.red / self.total
        self.blue = self.blue / self.total
        self.green = self.green / self.total
        self.violet = self.violet / self.total
        self.white = self.white / self.total
        self.black = self.black / self.total
        self.pink = self.pink / self.total
        self.yellow = self.yellow / self.total
        self.gray = self.gray / self.total

        #Average and std
        self.redStd = np.std(self.image[:,:,0])
        self.greenStd = np.std(self.image[:,:,1])
        self.blueStd = np.std(self.image[:,:,2])

        self.redAvg = np.average(self.image[:,:,0])
        self.greenAvg = np.average(self.image[:,:,1])
        self.blueAvg = np.average(self.image[:,:,2])

        self.list = [self.blue, self.green, self.violet, self.red, self.pink, self.white, self.black, self.gray, self.yellow, self.redStd, self.greenStd, self.blueStd, self.redAvg, self.greenAvg, self.blueAvg]
        return self.list
    #End countcolors()

#End of class Segment

#Define Class SoulTempo
class SoulTempo:

    #Method to segmentate the image into random pieces.
    def segmentate(self):
        self.segments = []
        numsegments = random.randint(1, int(math.sqrt(len(self.image)))) #Generate the number of segments
        print(numsegments)
        #math.sqrt(len(image).astype(int))

        increment = int(len(self.image) / numsegments)

        act = 0

        imageSeg = np.zeros((increment,len(self.image[0]),3), np.uint8)

        for i in range(0,numsegments):
            self.segments.append(Segment(imageSeg, 0 , 0, 0)) #Instantiate the segment

        #Send corresponding pixels to image
        x = 0 #Original pic indexes
        y = 0 #Original pic indexes
        for i in range(0, len(self.segments)):
            for a in range(0, increment - 1):
                for b in range(0, len(self.image[0]) - 1):
                    self.segments[i].image[a,b] = self.image[x,y]
                    y = y + 1
                x = x + 1
                y = 0
            #self.segments[i].saveimg("seg"+str(i)+".jpg") #Save the images

        colorData = []

        for i in range(0, len(self.segments)):
            colorData.append(self.segments[i].countcolors())
            #print(colorData[i])
            print("Processed section", i)

        return colorData
    #End method segmentate()



    #Initialize class
    def __init__(self, impath):
        #Read the image
        self.image = cv2.imread(impath) #Replace for impath
    #End constructor


#End of class SoulTempo
