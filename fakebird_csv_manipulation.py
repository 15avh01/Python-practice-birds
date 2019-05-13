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
from scipy import stats

with open("InBoth.csv", "w") as newfile:
    mystring = ("Seen by Computer and Human" + "\n")
    newfile.write(mystring)
    writer = csv.writer(newfile, delimiter = ",")

    f = open("longer_range_output_latest_version.csv", encoding='utf-8-sig')
    csv_f = csv.reader(f)
    #open first file

    birdlist = []
    timelistlong = []
    timelist = []
    radiuslist = []
    anglelist = []
    speedlist = []
    area = []
    #set up empty lists to fill with data

    for column in csv_f:
        timelistlong.append(float(column[0]))
        radiuslist.append(float(column[3]))
        anglelist.append(float(column[10]))
        speedlist.append(float(column[9]))
        #creates list with data for each column

    area = [x/1000 for x in radiuslist]
    area = [x**2 for x in area]
    area = [x*math.pi for x in area]
    #calculates estimated area of birds from radii. Divide by 1000 bc they were originally multiplied by 1000

    areadict = {}
    timearea = []
    timearea = list(zip(timelistlong,area))
    for x,y in timearea:
        areadict.setdefault(x, []).append(y)

    avgareadict = {}
    for k,v in areadict.items():
        avgareadict[k] = sum(v)/ float(len(v))
#creates a dictionary of values of average areas of birds seen in each frame key

    angledict = {}
    timeangle = []
    timeangle = list(zip(timelistlong,anglelist))
    for x,y in timeangle:
        angledict.setdefault(x, []).append(y)

    avgangledict = {}
    for k,v in angledict.items():
        avgangledict[k] = sum(v)/ float(len(v))

    speeddict = {}
    timespeed = []
    timespeed = list(zip(timelistlong,speedlist))
    for x,y in timespeed:
        speeddict.setdefault(x, []).append(y)

    avgspeeddict = {}
    for k,v in speeddict.items():
        avgspeeddict[k] = sum(v)/ float(len(v))

    for x in timelistlong:
        if x not in timelist:
            timelist.append(x)

    ff = open("4-28-18_T1.csv")
    csv_ff = csv.reader(ff)
    entranceframe = []
    exitframe = []

    for column in csv_ff:
        entranceframe.append(column[3])
        exitframe.append(column[6])
    #creates lists for second file
    entranceframe = entranceframe[1:]
    exitframe = exitframe[1:]
    #removes header
    entranceframe = [float(x) for x in entranceframe]
    exitframe = [float(x) for x in exitframe]
    #converts items in list from strings to floats
    timelist2 = list((entranceframe[i], exitframe[i]) for i in range(0,len(entranceframe)))

    computeronly = []
    humanonly = []
    inbotharea = []
    inboth = []
    inbothangle = []
    inbothspeed = []
    countedz = []
    test = []
    test2 = []

    for z in timelist:
        if z not in timelist2:
            for x,y in timelist2:
                if (x - 15)<= z <=(y + 15):
                    if z not in countedz:
                        countedz.append(z)
                    if x not in inboth:
                        inboth.append(x)
                        writer.writerow([x])
                        inbotharea.append(avgareadict[z])
                        inbothangle.append(avgangledict[z])
                        inbothspeed.append(avgspeeddict[z])
        else:
            inboth.append(x)
            inbotharea.append(avgareadict[z])
            inbothangle.append(avgangledict[z])
            inbothspeed.append(avgspeeddict[z])

    for z in timelist:
        if z not in countedz:
            computeronly.append(z)

#compares items in timelist with each in timelist2
#if the value is in 2, writes it to "inboth"
#If they are within distance of range, they are counted as "in both"
#If the values are not equal or within a distance of range
#they are written to file and list computeronly

    inbothbirddict = {}
    added = []
    count = 1
    for x,y in timelist2:
        frames = []
        for z in timelist:
            if (x - 15)<= z <=(y + 15):
                frames.append(z)
        if x in inboth and x not in added:
            added.append(x)
            inbothbirddict.setdefault(count, []).append(frames)
            count += 1
#creates dictionary of individual birds seen by both human and computer
#and all frames the computer "saw" them in

    computeronlybirddict = {}
    bird = []
    counted =  []
    computeronlyarea = []
    avgarea = []
    avgangle = []
    computeronlyangle = []
    avgspeed = []
    computeronlyspeed = []
    birdnumber = 0
    n = 0
    for x in computeronly:
        bird = []
        if x not in counted:
            if n <= ((len(computeronly)) - 2):
                while abs(computeronly[n] - computeronly[n+1]) <= 6:
                    if computeronly[n] not in bird:
                        bird.append(computeronly[n])
                        counted.append(computeronly[n])
                    if computeronly[n+1] not in bird:
                        bird.append(computeronly[n+1])
                        counted.append(computeronly[n+1])
                    n += 1
                else:
                    if x not in bird:
                        bird.append(x)
                    if len(bird) == 0:
                        pass
                    else:
                        birdnumber += 1
                        birdarealist= []
                        birdarea = []
                        for b in bird:
                            birdarealist.append(areadict[b])
                            if b not in computeronlybirddict:
                                computeronlybirddict.setdefault(birdnumber, bird)
                        for sublist in birdarealist:
                            for a in sublist:
                                birdarea.append(a)
                        avgarea = (sum(birdarea)/len(birdarea))
                        computeronlyarea.append(avgarea)
#                        x = birdarea
#                        bins = np.linspace(0,15000, 100)
#                        fig = plt.figure()
#                        ax = plt.subplot(211)
#                        plt.hist([x], bins, color = ["grey"])
#                        axes = plt.gca()
#                        axes.set_ylim(0,40)
#                        axes.set_xlim(0,15000)
#                        plt.xlabel("Apparent Size of Bird (pixels^2)")
#                        plt.ylabel("Frequency")
#                        c = computeronlybirddict[birdnumber]
#                        plt.title("Computer-Only Bird #%03d Area (First Frame %08d)" % (birdnumber, c[0]))
#                        ax.text(12000,30, "Bins = 100", bbox = {"pad":10, "facecolor":"white"})
#                        plt.grid(True)
#                        plt.savefig("computeronly bird #%03d Frame %08d Area.png" %(birdnumber, c[0]))
##                        plt.show()

                        birdanglelist= []
                        birdangle = []
                        for b in bird:
                            birdanglelist.append(angledict[b])
                        for sublist in birdanglelist:
                            for a in sublist:
                                birdangle.append(a)
                        avgangle = (sum(birdangle)/len(birdangle))
                        computeronlyangle.append(avgangle)
#                        x = birdangle
#                        bins = np.linspace(-180,180, 50)
#                        fig = plt.figure()
#                        ax = plt.subplot(211)
#                        plt.hist([x], bins, color = ["grey"])
#                        axes = plt.gca()
#                        axes.set_ylim(0,120)
#                        axes.set_xlim(-180,180)
#                        plt.xlabel("Apparent Angle of Motion (Degrees)")
#                        plt.ylabel("Frequency")
#                        c = computeronlybirddict[birdnumber]
#                        plt.title("Computer-Only Bird #%03d Angle (First Frame %08d)" % (birdnumber, c[0]))
#                        ax.text(100,95, "Bins = 50", bbox = {"pad":10, "facecolor":"white"})
#                        plt.grid(True)
##                        plt.savefig("computeronly bird #%03d Frame %08d Angle.png" %(birdnumber, c[0]))
#                        plt.show()
#
                        birdspeedlist= []
                        birdspeed = []
                        for b in bird:
                            birdspeedlist.append(speeddict[b])
                        for sublist in birdspeedlist:
                            for a in sublist:
                                birdspeed.append(a)
                        avgspeed = (sum(birdspeed)/len(birdspeed))
                        computeronlyspeed.append(avgspeed)
                        x = birdspeed
                        bins = np.linspace(0,400, 50)
                        fig = plt.figure()
                        ax = plt.subplot(211)
                        plt.hist([x], bins, color = ["grey"])
                        axes = plt.gca()
                        axes.set_ylim(0,35)
                        axes.set_xlim(0,400)
                        plt.xlabel("Apparent Speed of Bird (pixels/second)")
                        plt.ylabel("Frequency")
                        c = computeronlybirddict[birdnumber]
                        plt.title("Computer-Only Bird #%03d Speed (First Frame %08d)" % (birdnumber, c[0]))
                        ax.text(275,25, "Bins = 50", bbox = {"pad":10, "facecolor":"white"})
                        plt.grid(True)
##                        plt.savefig("computeronly bird #%03d Frame %08d Speed.png" %(birdnumber, c[0]))
                        plt.show()
                        if computeronly[n] not in counted:
                            counted.append(computeronly[n])
                        n += 1
#separates computeronly frames into birds based on consecutive (within a range) frames
#length -2 because last can't be compared to n+1 and index values are diff from length
#creates plots of each separated bird showing all of the areas of all contours of all frames that the specific bird was visible





with open("HumanOnly.csv", "w") as secondfile:
    mystring = ("In Human List Only (Integers)" + "\n")
    secondfile.write(mystring)
with open ("HumanOnly.csv", "a") as secondfile:
    for x,y in timelist2:
        if x not in inboth and x not in humanonly:
            humanonly.append(x)

    humanonlyint = []
    humanonlyint = [round(x) for x in humanonly]
    for x in humanonlyint:
            writer = csv.writer(secondfile)
            writer.writerow([x])
#Finds birds seen by human but not both
#rounds to integers so exact frame can be extracted and checked

with open("ComputerOnlyFrames.csv", "w") as thirdfile:
    mystring = ("In Computer List Only" + "\n")
    thirdfile.write(mystring)
with open ("ComputerOnly.csv", "a") as thirdfile:
    for x in computeronly:
        writer = csv.writer(thirdfile)
        writer.writerow([x])

#x = computeronlyarea
#y = inbotharea
#bins = np.linspace(0, 4000, 25)
##start, stop, number of bins (all of same width)
#fig = plt.figure()
#ax = plt.subplot(111)
##111 gives 1x1 dimensions, 1 figure
#plt.hist([x, y], bins, label = ["Detected Only by Computer", "Detected by Computer and Human"], color = ["grey", "black"])
#axes = plt.gca()
#axes.set_ylim([0,50])
#axes.set_xlim([0,4500])
#plt.xlabel("Average Size of Bird (pixels^2)")
#plt.ylabel("Number of Birds")
#plt.title("Effect of Apparent Bird Size on Detectability")
#ax.text(3200,35, "Bins = 25", bbox = {"pad":10, "facecolor":"white"})
##coordinates, text
#ax.legend()
#plt.grid(True)
#plt.savefig("computer vs inboth area.pdf")
#plt.show()

#x = computeronlyangle
#y = inbothangle
#bins = np.linspace(-180, 180, 25)
##start, stop, number of bins (all of same width)
#ax2 = plt.subplot(111)
#plt.hist([x, y], bins, label = ["Detected Only by Computer", "Detected by Computer and Human"], color = ["0.55", "black"])
#axes = plt.gca()
#axes.set_ylim([0,200])
#axes.set_xlim([-180,180])
#plt.xlabel("Average Apparent Angle of Motion of Bird (degrees)")
#plt.ylabel("Number of Birds")
#plt.title("Effect of Apparent Angle of Motion on Detectability")
#ax2.text(100,120, "Bins = 25", bbox = {"pad":10, "facecolor":"white"})
##coordinates, text, box design
#ax2.legend()
#plt.grid(True)
#plt.savefig("computer vs inboth angle.pdf")
#plt.show()


#x = computeronlyspeed
#y = inbothspeed
#bins = np.linspace(0, 350, 25)
##start, stop, number of bins (all of same width)
#ax4 = plt.subplot(111)
#plt.hist([x, y], bins, label = ["Detected Only by Computer", "Detected by Computer and Human"], color = ["0.55", "black"])
#axes = plt.gca()
#axes.set_ylim([0,150])
#axes.set_xlim([0,350])
#plt.xlabel("Average Speed of Bird (pixels/frame)")
#plt.ylabel("Number of Birds")
#plt.title("Effect of Apparent Bird Speed on Detectability")
#ax4.text(250,100, "Bins = 25", bbox = {"pad":10, "facecolor":"white"})
##coordinates, text, box design
#ax4.legend()
#plt.grid(True)
#plt.savefig("computer vs inboth speed.pdf")
#plt.show()

print("Area KS Test Result:")
print(stats.ks_2samp(computeronlyarea, inbotharea))
print("\n")
print("Speed KS Test Result:")
print(stats.ks_2samp(computeronlyspeed, inbothspeed))