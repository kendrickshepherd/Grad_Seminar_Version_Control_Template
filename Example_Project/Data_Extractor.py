#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 09:47:17 2025

@author: kendrickshepherd
"""

import sys
import matplotlib
from matplotlib import pyplot as plt

# Convert Timestamp into Date
class DateTime:
    
    def __init__(self):
        self.year = 0
        self.month = 0
        self.day = 0
        
        # military time (24 hrs)
        self.hour = 0
        self.minute = 0
        self.no_time = True

# Load information from your CSV file
def LoadCSVData(filename, has_headers = True):
    
    # ensure that the input file is a CSV file
    if(filename.split('.')[-1] !='csv'):
        print("Input must be a csv file. Please input a csv file with file extension .csv included in the end of the input file name.")
        sys.exit()
    # open the file
    header = []
    data = []
    date_times = []
    with open(filename, 'r',encoding='utf-8-sig') as f:
        count = 0
        for line in f:
            stripline = line.strip();
            commaline = stripline.split(',')
            if has_headers and count == 0:
                header = commaline
            else:
                data.append(commaline)
                
                sample_date = DateTime()
                date = commaline[0].split(" ")
                [month,day,year] = date[0].split("/")
                [hour,minute] = date[1].split(":")
                sample_date.year = int(year)
                sample_date.month = int(month)
                sample_date.day = int(day)
                sample_date.hour = int(hour)
                sample_date.minute = int(minute)
                sample_date.no_time = False
                date_times.append(sample_date)
                
            count += 1
            
    return data, date_times, header
        
# Convert DateTime to Minutes
def DateTimeToMinutes(date_time):
    return date_time.minute + 60*date_time.hour

# Plot Data against daily temperature information
def PlotData(data, date_times, column):
    vals = [float(data[i][column]) for i in range(0,len(data))]
    times = [DateTimeToMinutes(date_time) for date_time in date_times]
    plt.plot(times,vals)
    
# Get average of quantity of interest
def GetAverageValue(data, column):
    avg = 0
    for i in range(0,len(data)):
        avg += float(data[i][column])
    return avg/len(data)
    


