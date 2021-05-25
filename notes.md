# Notes

## Pulling in data
### wget

```
wget -r --no-parent -A '*.mts' http://www.mesonet.org/data/public/mesonet/mts/2020/02/

```

Change mts (station data) to mdf (state hourly data) 

## Cleaning data

* Data files are a fixed width format for the columns of data. 
* The data is structured to cover a 24 hour period based on UTC but is reported as time from midnight. 
* missing or not reporting data uses the -99x format for reporting
