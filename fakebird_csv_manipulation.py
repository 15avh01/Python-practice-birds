#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 14:44:44 2018

@author: alyseheaston
"""

import csv
import math
import numpy as np
import matplotlib.pyplot as plt


with open("FirstOnly.csv", "w") as newfile:
    mystring = ("In First List Only" + "\n")
    newfile.write(mystring)

    f = open("fakebirds1.csv")
    csv_f = csv.reader(f)
    #open first file

    birdlist = []
    timelist = []
    radiuslist = []
    anglelist = []
    contrastlist = []
    speedlist = []
    #set up empty lists to fill with data

    for column in csv_f:
        timelist.append(column[1])
        radiuslist.append(column[2])
        anglelist.append(column[3])
        contrastlist.append(column[4])
        speedlist.append(column[5])
        #creates list with data for each column
    timelist = timelist[1:]
    anglelist = anglelist[1:]
    contrastlist = contrastlist[1:]
    speedlist = speedlist[1:]
    #removes header

    anglelist = [float(x) for x in anglelist]
    contrastlist = [float(x) for x in contrastlist]
    speedlist = [float(x) for x in speedlist]

    radiuslist = radiuslist[1:]
    radiuslist = [float(x) for x in radiuslist]
    #converts list to floats so operations can be performed 
    area = [x**2 for x in radiuslist]
    area = [x*math.pi for x in area]
    #calculates estimated area of birds from radii

    ff = open("fakebirds2.csv")
    csv_ff = csv.reader(ff)
    timelist2 = []

    for column in csv_ff:
        timelist2.append(column[1])
    #creates lists for second file
    timelist2 = timelist2[1:]
    #removes header

    timelist = [float(x) for x in timelist]
    timelist2 = [float(x) for x in timelist2]
    #converts items in both lists from strings to floats

    mydict = {}
    zipped1 = (zip(timelist,area))
    for x,i in zipped1:
        mydict.setdefault(x, []).append(i)
#creates a dictionary to pair times in first list with areas, allowing for multiple values per key
    angledict = {}
    zipped2 = (zip(timelist, anglelist))
    for x,i in zipped2:
        angledict.setdefault(x,[]).append(i)
    contrastdict = {}
    zipped3 = (zip(timelist, contrastlist))
    for x, i in zipped3:
        contrastdict.setdefault(x,[]).append(i)
    speeddict = {}
    zipped4 = (zip(timelist, speedlist))
    for x, i in zipped4:
        speeddict.setdefault(x,[]).append(i)

    firstonly = []
    secondonly = []
    firstonlyarea = []
    inbotharea = []
    inboth = []
    firstonlyangle = []
    inbothangle = []
    firstonlycontrast = []
    inbothcontrast = []
    firstonlyspeed = []
    inbothspeed = []

    for x in timelist:
        if x not in timelist2:
            for i in range(0,len(timelist2)):
                if abs(x - timelist[i]) <= 0.05:
                    pass
                else:
                    if x not in firstonly:
                        writer = csv.writer(newfile)
                        writer.writerow([x])
                        firstonly.append(x)
                        firstonlyarea.append(mydict[x])
                        firstonlyangle.append(angledict[x])
                        firstonlycontrast.append(contrastdict[x])
                        firstonlyspeed.append(speeddict[x])
                    else:
                        pass
        else:
            inboth.append(x)
            inbotharea.append(mydict[x])
            inbothangle.append(angledict[x])
            inbothcontrast.append(contrastdict[x])
            inbothspeed.append(speeddict[x])
#compares items in timelist with each in timelist2
#if the value is in 2, it passes it
#If they are within 0.05 of each other, they are counted as equal are passed
#If the values are not equal or within 0.05, they are written to file and list

firstonlyarea = np.array(firstonlyarea)
firstonlyangle = np.array(firstonlyangle)
firstonlycontrast = np.array(firstonlycontrast)
firstonlyspeed = np.array(firstonlyspeed)
inbotharea = np.array(inbotharea)
inbothangle = np.array(inbothangle)
inbothcontrast = np.array(inbothcontrast)
inbothspeed = np.array(inbothspeed)
#creates arrays to graph


with open("SecondOnly.csv", "w") as secondfile:
    mystring = ("In Second List Only" + "\n")
    secondfile.write(mystring)
with open ("SecondOnly.csv", "a") as secondfile:
    for x in timelist2:
        if x not in timelist:
            for i in range(0,len(timelist2)):
                if abs(x - timelist2[i]) <= 0.05:
                    pass
                else:
                    if x not in secondonly:
                        writer = csv.writer(secondfile)
                        writer.writerow([x])
                        secondonly.append(x)
                    else:
                        pass
        else:
            pass
#comparable to list comparison done above but reversed
#EXCEPT length in range is matched to shortest list

with open("Areas.csv", "w") as thirdfile:
    mystring = ("Areas" + "\n")
    thirdfile.write(mystring)
with open("Areas.csv", "a") as thirdfile:
    for x in area:
        writer = csv.writer(thirdfile)
        writer.writerow([x])

x = firstonlyarea
y = inbotharea
bins = np.linspace(0, 4000, 50)
#start, stop, number of bins (all of same width)
fig = plt.figure()
ax = plt.subplot(111)
#111 gives 1x1 dimensions, 1 figure
plt.hist([x, y], bins, label = ["Seen Only by Computer", "Seen by Computer and Human"], color = ["grey", "black"])
axes = plt.gca()
axes.set_ylim([0,10])
axes.set_xlim([0,4000])
plt.xlabel("Size of Bird (pixels^2)")
plt.ylabel("Count")
plt.title("Bird Count by Size")
ax.text(3200,7, "Bins = 50", bbox = {"pad":10, "facecolor":"white"})
#coordinates, text
ax.legend()
plt.grid(True)
plt.show()

x = firstonlyangle
y = inbothangle
bins = np.linspace(0, 360, 25)
#start, stop, number of bins (all of same width)
ax2 = plt.subplot(111)
plt.hist([x, y], bins, label = ["Seen Only by Computer", "Seen by Computer and Human"], color = ["0.55", "black"])
axes = plt.gca()
axes.set_ylim([0,10])
axes.set_xlim([0,360])
plt.xlabel("Apparent Angle of Motion of Bird (degrees)")
plt.ylabel("Count")
plt.title("Bird Count by Apparent Angle of Motion")
ax2.text(250,7, "Bins = 25", bbox = {"pad":10, "facecolor":"white"})
#coordinates, text, box design
ax2.legend()
plt.grid(True)
plt.show()

x = firstonlycontrast
y = inbothcontrast
bins = np.linspace(0, 255, 25)
#start, stop, number of bins (all of same width)
ax3 = plt.subplot(111)
plt.hist([x, y], bins, label = ["Seen Only by Computer", "Seen by Computer and Human"], color = ["0.55", "black"])
axes = plt.gca()
axes.set_ylim([0,10])
axes.set_xlim([0,255])
plt.xlabel("Difference in Contrast (out of 255)")
plt.ylabel("Count")
plt.title("Bird Count by Difference in Contrast Between Bird and Background")
ax3.text(200,7, "Bins = 25", bbox = {"pad":10, "facecolor":"white"})
#coordinates, text, box design
ax3.legend()
plt.grid(True)
plt.show()

x = firstonlyspeed
y = inbothspeed
bins = np.linspace(0, 350, 30)
#start, stop, number of bins (all of same width)
ax4 = plt.subplot(111)
plt.hist([x, y], bins, label = ["Seen Only by Computer", "Seen by Computer and Human"], color = ["0.55", "black"])
axes = plt.gca()
axes.set_ylim([0,10])
axes.set_xlim([0,350])
plt.xlabel("Speed of Bird (pixels/frame)")
plt.ylabel("Count")
plt.title("Bird Count by Speed")
ax4.text(250,7, "Bins = 30", bbox = {"pad":10, "facecolor":"white"})
#coordinates, text, box design
ax4.legend()
plt.grid(True)
plt.show()