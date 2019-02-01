#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 14:44:44 2018

@author: alyseheaston
"""

import csv
import math

with open("FirstOnly.csv", "w") as newfile:
    mystring = ("In First List Only" + "\n")
    newfile.write(mystring)

    f = open("fakebirds1.csv")
    csv_f = csv.reader(f)
    #open first file

    birdlist = []
    timelist = []
    radiuslist = []
    #set up empty lists to fill with data

    for column in csv_f:
        timelist.append(column[1])
        radiuslist.append(column[2])
        #creates list with data for each column
    timelist = timelist[1:]
    #removes header

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
    zipped = (zip(timelist,area))
    for x,i in zipped:
        mydict.setdefault(x, []).append(i)
#creates a dictionary to pair times in first list with areas, allowing for multiple values per key
    firstonly = []
    secondonly = []

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
                    else:
                        pass
        else:
            pass
#compares items in timelist with each in timelist2
#if the value is in 2, it passes it
#If they are within 0.05 of each other, they are counted as equal are passed
#If the values are not equal or within 0.05, they are written to file and list

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
