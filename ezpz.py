#!/usr/bin/python
# coding: utf-8

# EZP report header:
#Login Date;Logout Date;Username;EZproxy Session;IP address;Geography
#column widths: 11,9,11,9,31,16,17,40
# See: parsing notes
#to create the source data:
#head -n $(grep -n Login\ summary ccl201512_report.log |cut -d: -f1) ccl201512_report.log |grep cgu > ezp201512CGU.txt

import sys
import ConfigParser
import base64
import uuid
from hashlib import sha256
doc=""" 
%prog [file] [output] 
file is the name of the ezproxy report we want to process. 
Outputfile should include path, will be created if not existing and clobbered if existing
"""


def hash_uid(uname, salt=None):
    if salt is None:
        salt = uuid.uuid4().hex
    hashed_uid = sha256(uname + salt).hexdigest()
    return (hashed_uid)

def verify_password(uid, hashed_uid, salt):
    re_hashed, salt = hash_uid(uid, salt)
    return re_hashed == hashed_uid

def getUserID(loginCred):
	#from idAtSource, return the userID (to be encrypted)
	try:
		#parse apart the username into uname (hashed) and campus
		uname = loginCred.split('@')[0]
		if uname not in ['-','Username']: #hash it
			uname = hash_uid(uname, UNAMESALT) 
	except IndexError:
		uname = 'ERROR'
	return uname
	
def getCampus(loginCred):
	#from idAtSource, return campus initials (CGU, KGI, CMC, HMC, PIT, POM, SCR)
	campus = '-' #default value for invalid data errors
	try:
		#parse apart the username into uname (hashed) and campus
		campus = loginCred.split('@')[1].lower()[0:3] #campus depends on uname
	except IndexError:
		campus = 'ERROR'
	return campus

def getDateList(dateBlob):
	#from a string with year-month-day return a list with [year,month,day]
	return dateBlob.strip().split('-')

def getTimeList(timeBlob):
	#from a string with hour:minute:second return a list with [hour, minute, second]
	return timeBlob.strip().split(':')
	
def getGeographyList(geogBlob):
	#from a string with countryabbrev;countryName;state;city return a list with [countryabbrev,countryName,state,city]
	return geogBlob.strip().split(';')
	
config = ConfigParser.RawConfigParser()
config.read('ezpz.cfg')
UNAMESALT = config.get('Auth', 'salt')

if __name__ == '__main__':
	ezpInFileName = sys.argv[1]
	ezpOutFileName = sys.argv[2]
	with open (ezpOutFileName,'w') as ezpOutFile, open(ezpInFileName, 'r') as ezpInFile:
		for line in ezpInFile:
			#parse out the individual output values (including campus), encrypt the user id, write output
			#Login Date; Login Time; Logout Date; Logout Time; Username;EZproxy Session;IP address;Geography
			#column widths: [0:11],[11:20],[20:31],[31:40],[40:71],[71:86], [86:103], [103:]
			loginDateList = getDateList(line[0:11])
			loginTimeList = getTimeList(line[11:20])
			logoutDateList = getDateList(line[20:31])
			logoutTimeList = getTimeList(line[31:40])			
			uid = getUserID(line[40:71])
			campus = getCampus(line[40:71])
			session = line[71:86].strip()
			ip = line[86:103].strip()
			geography = line[103:].strip()
			print line[40:71], campus, uid, session

			
		
