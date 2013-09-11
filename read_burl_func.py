##############################################################################
#
#This file contains a function that will read in the time, pressure, wind speed, 
#and wind direction for a given bouy data .dat file
#
#The data is stored in a local dictionary (data) and passed to a global
#dictionary (data)
#
##############################################################################
#
#Created by: Taylor Sansom
#September 11, 2013
#
##############################################################################

import numpy as np
import datetime as dt

def getdata_f(file):
    
    f = open(file)
    
    pres = []
    wspd = []
    wdir = []
    date = []
    
    for line in f.readlines()[2:]:
        data = line.split()
        pres.append( float(data[12]) )
        wdir.append( int(data[5]) )
        wspd.append( float(data[6]) )
        date.append( str(data[0] + data[1] + data[2] + data[3] +  data[4]) )
        
    pres = np.array(pres)
    wdir = np.array(wdir)
    wspd = np.array(wspd)
    date = np.array(date)
    
    for x in range(len(wdir)):
        if wdir[x]<180:
            wdir[x]=wdir[x]+180
        else:
            wdir[x]=wdir[x]-180
            
    date = [ dt.datetime.strptime(date[x], "%Y%m%d%H%M") for x in range(len(date)) ]
    
    data={'date': np.array(date), 'wdir': np.array(wdir), 'wspd': np.array(wspd), 'pres': np.array(pres)}
    
    return data
    
    if __name__ == '__main__':
        print getdata_f(file)
        
data=getdata_f('burl1_2011.dat')

print data