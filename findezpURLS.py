#!/usr/bin/python
# coding: utf-8
import sys
import csv
import re
doc=""" 
%prog [logfile] [output] 
logfile is the name of the ezproxy log file we want to process. 
outputfile should include path, will be created if not existing and clobbered if existing
Resulting file will contain URLs parsed into fields
"""
YUCK = ["css","dll","f4v","gif","ico","jpg","jpeg","js","json","png","swf","ttf","woff"]
count = 0
def printStatus(curr, total):
	sys.stdout.write('Processing line {} / {}\r'.format(curr,total))
	sys.stdout.flush()
	
if __name__ == '__main__':
	InFileName = sys.argv[1] #main log file
	OutFileName = sys.argv[2] #new logfile to write
	kgiResFile = open(OutFileName,'w')
	ezpwriter = csv.writer(kgiResFile, delimiter='|')
	with open(InFileName,'r') as ezpKGI:
		print "Retrieving log data..."
		lines = [l.strip('\n') for l in ezpKGI.readlines()]
		for i, line in enumerate(lines):
			if i%100 == 0:
				printStatus(i, len(lines))
			#get the session ID
			try:
				foo = re.search(" - ([^ ]+) ", line)
				if foo:
					sess = foo.group(1) #line.split(" - ")[1].split(" ")[0]
			except AttributeError:
				sess = '-'
				pass
			#get the URL, break into pipe-delimited fields
			try:
				resource = re.search("(?P<url>https?://[^\s]+)", line).group("url").split('.')
				if resource:
					if (resource[-1].lower() not in YUCK):#filter out unwanted file formats	
						resource[0]=resource[0].split('//')[1]#get rid of 'http://'
						resource.insert(0,sess)
						ezpwriter.writerow(resource)
			except AttributeError:
				resource = "-"
				pass
			except TypeError:
				result = []
				pass
	print "Processing complete for",OutFileName


