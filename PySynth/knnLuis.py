# K-Nearest Neighbors (K-NN)

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix

#Class ColorDetector
class ColorDetector:

    #Constructor
    def __init__(self):
        # Importing the dataset
        dataset = pd.read_csv('colors150.csv')
        self.X = dataset.iloc[:, [0, 1, 2]].values
        self.y = dataset.iloc[:, 3].values

        # Splitting the dataset into the Training set and Test set
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size = 0.25, random_state = 0)

        # Feature Scaling
        #self.sc = StandardScaler()
        #self.X_train = self.sc.fit_transform(self.X_train)
        #self.X_test = self.sc.transform(self.X_test)

        # Fitting K-NN to the Training set
        self.classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
        self.classifier.fit(self.X_train, self.y_train)
    #End Constructor


    #Predict a result
    def predict(self, red, blue, green):
        array = [[red,blue,green]]
        self.y_pred = self.classifier.predict(array)
        return self.y_pred
    #End method
