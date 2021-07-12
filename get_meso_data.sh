#!/usr/bin/env bash
##########################################################################
# Program:    get_meso.sh
# Purpose:    script for presenting menu options for a user
# Version:    0.0.1
# Created:    18 May 2021
#
# Author:     Mark Laufersweiler
# Email:      laufers@ou.edu
#
# Modified:   
#			
##########################################################################


# mesonet site where data resides
base_url="http://www.mesonet.org/data/public/mesonet"
# echo $base_url
# set logfile
logfile=wget.log

	clear
echo ""
echo ""
echo "This script will retreive Oklahoma Mesonet data for a"
echo "particular day or month for data01 Mar 1994 - present"
echo ""
read -rp "Choose d for a day(d) or m for a month(m) data: " q1
if [ "$q1" = 'd' ] || [ "$q1" = 'D' ]; then 
	echo ""
	echo "Enter date for the day you wish to download."
	echo ""
	read -rp "Enter year (yyyy): " year;
	#echo "$year"
	read -rp "Enter month (mm): " month;
	#echo "$month"
	read -rp "Enter day (dd): " day;
	#echo "$day"

	url_mdf="$base_url/mdf/$year/$month/$day/"
	url_mts="$base_url/mts/$year/$month/$day/"
	echo ""
	echo "Base urls: "
	echo $url_mdf
	echo $url_mts

elif [ "$q1" = 'm' ] || [ "$q1" = 'M' ] || [ "$q1" = '' ]; then 
	echo ""
	echo "Enter date for the month you wish to download."
	echo ""
	read -rp "Enter year (yyyy): " year;
	echo "$year"
	read -rp "Enter month (mm): " month;
	echo "$month"
	url_mdf="$base_url/mdf/$year/$month/"
	url_mts="$base_url/mts/$year/$month/"
	echo ""
	echo "Base urls: "
	echo $url_mdf
	echo $url_mts
else
	echo "Incorect entry, try again"
fi

# wget -r --no-parent -N -A '*.mts' $url_mts
wget -r --no-parent -N -A '*.mdf' $url_mdf -o 'mdf_'$logfile
echo ""
echo "Completed download of mdf files."
wget -r --no-parent -N -A '*.mts' $url_mts -o 'mts_'$logfile
echo ""
echo "Completed download of mts files."
echo ""
