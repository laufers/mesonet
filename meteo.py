import numpy as np
# alias for numpy
import matplotlib.pyplot as plt
# imports matlab like ploting and alaised

# my first funtion
def tmp2f (arg):
	ntmp = (9./5. *arg) + 32.
	return ntmp;

def dewpoint(rh, tmpc):
	H = (np.log10(rh) - 2)/0.4343 + (17.62 * tmpc)/(243.12 + tmpc)
	dptc = 243.12 * H / (17.62 - H)
	return dptc;

#x = np.loadtxt('20120229nrmn.mts', skiprows = 3, usecols = [3,12], unpack = True)
# second method allowing for headers to be read in as data
#x = np.genfromtxt('20120229nrmn.mts',dtype = None, names = True, skip_header = 2)

# time,relh,tmpc,wspd,pres = np.loadtxt('20120302nrmn.mts', skiprows = 3, usecols = [2,3,4,5,12], unpack = True)
data = np.genfromtxt('20120317nrmn.mts', skiprows = 2 , dtype= None, names = True)


# post processing of data to facilitate plotting, this ignores missing data and uses the standard NaN(not a number)
#relh[relh==-996] = np.nan

# second method to mask(remove, ignore) data in preperation for display or analytics.
relh = np.ma.array(data["RELH"], mask = (data["RELH"] == -996))
pres = np.ma.array(data["PRES"], mask = (data["PRES"] == -996))
tmpc = np.ma.array(data["TAIR"], mask = (data["TAIR"] == -996))
wspd = np.ma.array(data["WSPD"], mask = (data["WSPD"] == -996))
tmpf = tmp2f(tmpc)
dptf = tmp2f(dewpoint(relh, tmpc))

fig = plt.figure()

# Set up of dictionary for use of strings and variable names
# Strings first owing to non hashing of arrays
# tuple added to include color
varname = {'Rel. Humidity' : (relh,'green'),
		   'Dewpoint F'	   : (dptf, 'green'), 
		   'Pressure mb' : (pres,'black'),
#		   'Temperature C' : (tmpc,'red'), 
		   'Windspeed knots' : (wspd, 'blue'),
		   'Temperature F' : (tmpf,'red'),}

# Needed prior to the creation of the dictionary
# pltlist = [relh, pres, tmpc, wspd]

# careful when calling dictionary that tuple is split out and in the case of the y axis
# remember to keep the dictionary aray
for panel,metvar in enumerate(varname, start=1):
    plt.subplot(len(varname),1,panel)
    var,colr = varname[metvar]
    plt.plot(data['TIME'], var, colr)
    plt.xlabel('Mintues after 00z')
    plt.ylabel(metvar)
plt.show()

