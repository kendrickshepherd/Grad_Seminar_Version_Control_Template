#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 10:10:27 2025

@author: kendrickshepherd
"""

import Data_Extractor as de

filename = "./Data/March_4_2016.csv"
data, date_times, header = de.LoadCSVData(filename)
print("Average temperature (C): ", de.GetAverageValue(data,2))
