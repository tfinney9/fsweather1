# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 15:26:06 2017

@author: tanner
"""

import mwlatest#Grabber
import datetime#Writer
import Tweeter#Tweeter
import sys


station=open('stationName.txt')
sName=station.read()
simTime=str(datetime.datetime.now())


def parse(dta):
    keys=dta['STATION'][0]['OBSERVATIONS'].keys()
    hr=simTime[11:16]
    name=dta['STATION'][0]['STID']
    
    fT=float
    fM=float
    tempC=float
    windDir=float
    humid=float
    windSpd=float
    windDir=float
    voltage=float
    
    for i in range(len(keys)):
        if str(keys[i])=='air_temp_value_1':
            tempC=dta['STATION'][0]['OBSERVATIONS']['air_temp_value_1']['value']#C
    #        continue
        if str(keys[i])=='wind_speed_value_1':
            windSpd=dta['STATION'][0]['OBSERVATIONS']['wind_speed_value_1']['value']#m/s
        if str(keys[i])=='wind_direction_value_1':
            windDir=dta['STATION'][0]['OBSERVATIONS']['wind_direction_value_1']['value']#degFromNorth    
        if str(keys[i])=='relative_humidity_value_1':
            humid=dta['STATION'][0]['OBSERVATIONS']['relative_humidity_value_1']['value']#%
        if str(keys[i])=='volt_value_1':
            voltage=dta['STATION'][0]['OBSERVATIONS']['volt_value_1']['value']#Volts
        if str(keys[i])=='volt_value_1':
            fM=dta['STATION'][0]['OBSERVATIONS']['fuel_moisture_value_1']['value']
        if str(keys[i])=='volt_value_1':
            fT=dta['STATION'][0]['OBSERVATIONS']['fuel_temp_value_1']['value']
    
    tempF=tempC*9./5.+32.
    mpsTompH=2.23694
    windSpdM=windSpd*mpsTompH
    datList=[str(name),hr,tempF,tempC,humid,windSpdM,windDir]
    exList=[voltage,fM,fT]
    return datList
    
    
#data=parse(dta)



testList=['stat','18:55', '32.432', '.24', '47.81', '2.544', '125.8']
# time tempF tempC humidity speed direction    

def writeFile(dataList):
    fout=open("weather.txt",'w')
    fout.write(dataList[0])
    fout.write(" weather at ")
    fout.write(dataList[1])
    fout.write(": ")
    fout.write(str(round(dataList[2],2)))
    fout.write("F/")
    fout.write(str(round(dataList[3],2)))
    fout.write("C ")
    fout.write("Relative Humidity: ")
    fout.write(str(round(dataList[4],2)))
    fout.write("% Wind Speed: ")
    fout.write(str(round(dataList[5],2)))
    fout.write(" mph at ")
    fout.write(str(round(dataList[6],2)))
    fout.write(" degrees from north.")
    fout.close()
    
    
wxUrl=mwlatest.stationUrlBuilder(mwlatest.dtoken,sName,"","")
dta=mwlatest.readData(wxUrl)
data=parse(dta)
writeFile(data)
Tweeter.Tweet('weather.txt')

