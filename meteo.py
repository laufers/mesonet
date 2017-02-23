import numpy as np
from numpy.lib.recfunctions import append_fields
import matplotlib.pyplot as plt
import datetime
import urllib.request
import sys


# my first funtion
def tmp2f(arg):
    ntmp = (9. / 5. * arg) + 32.
    return ntmp


def dewpoint(rh, tmpc):
    H = (np.log10(rh) - 2) / 0.4343 + (17.62 * tmpc) / (243.12 + tmpc)
    dptc = 243.12 * H / (17.62 - H)
    return dptc


# default station is Norman and date is current
# syntax is meteo.py [station] [date yyyymmdd]

now = datetime.datetime.now()

today = datetime.datetime.now().strftime("%Y%m%d")

station = 'nrmn'
date = today

if len(sys.argv) >= 2:
    station = sys.argv[1]

if len(sys.argv) >= 3:
    date = sys.argv[2]

# Read in data from url www.mesonet.org
filename = date + station + '.mts'
url = 'http://www.mesonet.org/data/public/mesonet/mts/' + \
    date[0:4] + '/' + date[4:6] + '/' + date[6:] + '/' + filename

print(filename, url)
data_get = urllib.request.urlopen(url)

# New line here

#x = np.loadtxt('20120229nrmn.mts', skiprows = 3, usecols = [3,12], unpack = True)
# second method allowing for headers to be read in as data
#x = np.genfromtxt('20120229nrmn.mts',dtype = None, names = True, skip_header = 2)

# time,relh,tmpc,wspd,pres = np.loadtxt('20120302nrmn.mts', skiprows = 3, usecols = [2,3,4,5,12], unpack = True)
# data read now includes test for missing data (-996,-995) as used by the OklaMesonet
# data = np.genfromtxt('data/20120317nrmn.mts', skip_header = 2 , dtype =
# None, names = True,
data = np.genfromtxt(data_get, skip_header=2, dtype=None, names=True,
                     missing_values={None: ["-995", "-996", "-999"]}, usemask=True)


# post processing of data to facilitate plotting, this ignores missing data and uses the standard NaN(not a number)
# relh[relh==-996] = np.nan

# second method to mask(remove, ignore) data in preperation for display or
# analytics.

DPTF = tmp2f(dewpoint(data["RELH"], data["TAIR"]))
data["TAIR"] = tmp2f(data["TAIR"])

# coombined function call result to original data array to keep varable
# data in one structure
data = append_fields(data, "DPTF", DPTF)


#fig = plt.figure(figsize=(12,10))
fig = plt.figure()
fig.set_size_inches(6, 8)

# Set up of dictionary for use of strings and variable names
# Strings first owing to non hashing of arrays
# tuple added to include color
# varname = {'Rel. Humidity' : (relh,'green'),
# 		   'Dewpoint F'	   : (dptf, 'green'),
# 		   'Pressure mb' : (pres,'black'),
# 		   'Temperature C' : (tmpc,'red'),
# 		   'Windspeed knots' : (wspd, 'blue'),
# 		   'Temperature F' : (tmpf,'red'),}
varPlotColor = dict(TAIR='red',
                    RELH='green',
                    WSPD='blue',
                    WDIR='blue',
                    RAIN='blue',
                    DPTF='green',
                    PRES='black',
                    SRAD='dark yellow',
                    TIME='black')

varPlotLabel = dict(TAIR='Temperature F',
                    RELH='Rel Humidity %',
                    WSPD='Wind Speed m/s',
                    WDIR='Wind Direction',
                    RAIN='Rain 24 hour Accum ins',
                    DPTF='Dewpoint F',
                    PRES='Pressure mb',
                    SRAD='Solar Insolation W/m2',
                    TIME='Minutes after midnight GMT (UTC)')


# Needed prior to the creation of the dictionary
pltlist = ["TAIR", "DPTF", "PRES", "WSPD", "WDIR"]

# careful when calling dictionary that tuple is split out and in the case of the y axis
# remember to keep the dictionary aray
for panel, metvar in enumerate(pltlist, start=1):
    plt.subplot(len(pltlist), 1, panel)
    plt.plot(data['TIME'], data[metvar], varPlotColor[metvar])
    plt.xlabel(varPlotLabel["TIME"])
    plt.ylabel(varPlotLabel[metvar])
    plt.axis('tight')

# plt.show()

plt.savefig('./plots/meteogram_' + station + '_' + date + '.png')
