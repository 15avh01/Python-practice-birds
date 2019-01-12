#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 14:44:44 2018

@author: alyseheaston
"""

import csv
import math

f = open("fakebirds1.csv")
csv_f = csv.reader(f)
#open first file

birdlist = []
timelist = []
radiuslist = []
#set up empty lists to fill with data

for column in csv_f:
    birdlist.append(column[0])
    timelist.append(column[1])
    radiuslist.append(column[2])
    #creates list with data for each column

radiuslist = radiuslist[1:]
radiuslist = [float(x) for x in radiuslist]
#converts list to floats so operations can be performed 

f = open("fakebirds2.csv")
csv_f = csv.reader(f)

birdlist2 = []
timelist2 = []
for column in csv_f:
    birdlist2.append(column[0])
    timelist2.append(column[1])
#creates lists for second file

settime = set(timelist)
settime2 = set(timelist2)

firstonly = settime - settime2
secondonly = settime2 - settime
#finds differences between the lists

area = [x**2 for x in radiuslist]
area = [x*math.pi for x in area]
#calculates estimated area of birds from radii


with open("exportedcsv.csv", "w") as newfile:
     mystring=("first only" + "," + "second only" + "," + "area" + "\n")
     newfile.write(mystring)

with open("exportedcsv.csv", "a") as newfile:
    string=(str(firstonly) + "\n")
    newfile.write(mystring)

with open("exportedcsv.csv", "a") as newfile:
    string=(str(secondonly) + "\n")
    newfile.write(mystring)

with open("exportedcsv.csv", "a") as newfile:
    string=(str(area) + "\n")
    newfile.write(mystring)
