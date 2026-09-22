from opensky_api import OpenSkyApi
import requests
import matplotlib
matplotlib.use('Agg')  
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

def GatherData():
    api = OpenSkyApi()
    s = api.get_states()
    print(s)

def CalculateAverage(df):
    tempVelocityList = []
    for flights in df.iloc:
        if flights['velocity'] != ' None':
            tempVelocityList.append((float(flights['velocity'])))
    tempVelocityList.pop()
    averageVelocity = sum(tempVelocityList)/len(tempVelocityList)
    return averageVelocity

def CalculateTotalFlightsOverTime(df):
    flightsInAir = 0
    for flights in df.iloc:
        if flights['on_ground'] == " False":
            flightsInAir += 1
    return flightsInAir

def GeneratePlot(x,y):
    plt.plot(x, y)
    plt.title("Flights in Air Between 11:25AM - 12:45 PM")
    plt.xlabel("Every 10 minutes after 11:25AM")
    plt.ylabel("Amount of Flights")
    plt.savefig('FlightInAir.png', dpi=150)

def main():
    datafileLoc = "datafiles/"

    ##### CALCULATING AVERAGE VELOCITY ####
    NUM_OF_FILES = 9
    allAverageVelocity = []
    FlightsList = []
    for i in range(1,NUM_OF_FILES+1,1):
        csvFile = datafileLoc+str(i)+".csv"
        df = pd.read_csv(csvFile)
        allAverageVelocity.append(CalculateAverage(df))
        FlightsList.append(CalculateTotalFlightsOverTime(df))

    ################
    finalAverageVelocity = sum(allAverageVelocity)/NUM_OF_FILES
    print("The average velocity amongst the 9 files is:", finalAverageVelocity)
    #################
    print(FlightsList)
    TimeList = [0, 10, 20, 30, 40, 50, 60, 70, 80]
    GeneratePlot(TimeList, FlightsList)

main()     
