#!/usr/bin/python
# coding: utf-8
import sys
import csv
from collections import defaultdict
from collections import Counter
doc=""" 
%prog [report] [output]  
report is the name of the ezproxy report we want to process. 
Outputfile should include path, will be created if not existing and clobbered if existing
"""

if __name__ == '__main__':
	InFileName = sys.argv[1] #main report file
	OutFileName = sys.argv[2] #new report file to write
	ResFile = open(OutFileName,'w')
	ezpwriter = csv.writer(ResFile, delimiter=',')
	with open(InFileName,'r') as ezp:
		uidd = {} # unique user id dictionary: key is uid, value is campus
		sidd = {} # session id dictionary: key is session, value is uid (hashed evenutually)
		errors = defaultdict(int) # holds values that cause parsing errors as keys and count of them as value
		for line in ezp:
			idatsrc = line[41:70].split('@') # parse out the user id from the log line
			uid = idatsrc[0].strip()
			sessid = line[71:86]# count sessions per user
			try: # assign campus (prefix) value to uid key
				uidd[uid] = idatsrc[1].split('.')[0].strip()# note though that the uid prefix may not be unique across campuses
			except IndexError:
				errors[idatsrc[0]]+=1
			try: # assign uid value to session key
				sidd[sessid] = uid
			except:
				  e = sys.exc_info()[0]
				  print "Error: {}".format(e)
		campuses = uidd.values() 
		campuses.sort()	
		cfreq = Counter(campuses) # a list of tuples: campus, count
		for k,v in cfreq.iteritems(): 
			print '{0:15}{1:6d}'.format(k,v)
		users = sidd.values()
		users.sort()
		ufreq = Counter(users) # a list of tuples: user, count of sessions
		for k,v in ufreq.iteritems():
			print '{}, {}'.format(k,v)
		for k,v in errors.iteritems():
			print 'Error Value: "{}" occurred {} times'.format(k.strip(),v)
