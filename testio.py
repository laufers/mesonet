import sys
import datetime

now = datetime.datetime.now()

today = datetime.datetime.now().strftime("%Y%m%d")

station = 'nrmn'
date = today

if len(sys.argv) >= 2 :
	station = sys.argv[1]

if len(sys.argv) >=3 : 	
	date = sys.argv[2]
	

filename = date+station+'.mts'	

url = 'http://www.mesonet.org/data/public/mesonet/mts/' + date[0:4] +  '/' + date[4:6] + '/' + date[6:] + '/' + filename
 
print (filename)

print (url)

print (station, date)