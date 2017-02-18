# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 15:26:06 2017

@author: tanner
"""

import mwlatest
import datetime

simTime=str(datetime.datetime.now())
hr=simTime[11:16]

wxUrl=mwlatest.stationUrlBuilder(mwlatest.dtoken,"TR266","","")
dta=mwlatest.readData(wxUrl)

name=dta['STATION'][0]['STID']
temp=dta['STATION'][0]['OBSERVATIONS']['air_temp_value_1']['value']#C
windSpd=dta['STATION'][0]['OBSERVATIONS']['wind_speed_value_1']#m/s
windDir=dta['STATION'][0]['OBSERVATIONS']['wind_direction_value_1']#degFromNorth
humid=dta['STATION'][0]['OBSERVATIONS']['relative_humidity_value_1']['value']#%
voltage=dta['STATION'][0]['OBSERVATIONS']['volt_value_1']['value']#Volts
fM=dta['STATION'][0]['OBSERVATIONS']['fuel_moisture_value_1']['value']
fT=dta['STATION'][0]['OBSERVATIONS']['fuel_temp_value_1']['value']

testList=['18:55', '32.432', '.24', '47.81', '2.544', '125.8']
    

def writeFile(dataList):
    fout=open("test.txt",'w')
    fout.write("weather at ")
    fout.write(dataList[0])
    fout.write(": ")
    fout.write(dataList[1])
    fout.write("F/")
    fout.write(dataList[2])
    fout.write("C ")
    fout.write("Relative Humidity: ")
    fout.write(dataList[3])
    fout.write("% Wind Speed: ")
    fout.write(dataList[4])
    fout.write(" mps at ")
    fout.write(dataList[5])
    fout.write(" degrees from north.")
    fout.close()

