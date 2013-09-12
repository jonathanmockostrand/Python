################################################################################
#
#Jonathan Strand
#Dept. of Geology & Geophysics, TAMU. 2013-09-11
#Python for Geoscientists
#
################################################################################
#
#This script contains a python class that will read date, sea-level pressure,
#wind speed, and wind direction from a NOAA bouy data file. Wind speed and
#direction has been converted to northward and eastward wind vectors.
#
#http://www.ndbc.noaa.gov/download_data.php?filename=burl1h2011.txt.gz&dir=data/historical/stdmet/
#
################################################################################

import numpy as np
import datetime as dt

class burl1_2011():
    '''
    Function:
        noaa_convert(file)

    Input:
        file.dat
        
    Output:
        Date as datetime
        Pressure as sea-level pressure
        wU and wV as Components U and V of wind vector 
        (converted from wind speed and direction)
    '''
    
    def __init__(self, datafile):
        
        self.datafile = datafile
        f = open(self.datafile)

        date = []
        pressure = []
        wspeed = []
        wdirection = []

        for line in f.readlines()[2:]:
            data = line.split()
            YYYY = int(data[0])
            MM = int(data[1])
            DD = int(data[2])
            hh = int(data[3])
            mm = int(data[4])
    
            date.append( dt.datetime(YYYY, MM, DD, hh, mm) )
            pressure.append( float(data[12]) )
            wspeed.append ( float(data[6]) )
            wdirection.append ( float(data[5]) )

        date = np.array(date)
        pressure = np.array(pressure)
        wspeed = np.array(wspeed)
        wdirection = np.array(wdirection) 
        U = np.array( -wspeed * np.sin(wdirection * np.pi/180) )
        V = np.array( -wspeed * np.cos(wdirection * np.pi/180) )

        self.date = date
        self.pressure = pressure
        self.U = U
        self.V = V
        
d11 = burl1_2011('burl1_2011.dat')
