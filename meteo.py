import numpy as np
# alias for numpy
import matplotlib.pyplot as plt
# imports matlab like ploting and alaised


#x = np.loadtxt('20120229nrmn.mts', skiprows = 3, usecols = [3,12], unpack = True)
# second method allowing for headers to be read in as data
#x = np.genfromtxt('20120229nrmn.mts',dtype = None, names = True, skip_header = 2)

time,relh,tmpc,wspd,pres = np.loadtxt('20120302nrmn.mts', skiprows = 3, usecols = [2,3,4,5,12], unpack = True)

# post processing of data to facilitate plotting, this ignores missing data and uses the standard NaN(not a number)
#relh[relh==-996] = np.nan

# second method to mask(remove, ignore) data in preperation for display or analytics.
relh = np.ma.array(relh, mask = (relh == -996))
pres = np.ma.array(pres, mask = (pres == -996))
tmpc = np.ma.array(tmpc, mask = (tmpc == -996))
wspd = np.ma.array(wspd, mask = (wspd == -996))


fig = plt.figure()

plt.subplot(4,1,1)
plt.plot(time,pres)

plt.subplot(4,1,2)
plt.plot(time,relh)

plt.subplot(4,1,3)
plt.plot(time,tmpc,'r')

plt.subplot(4,1,4)
plt.plot(time,wspd)
plt.show()