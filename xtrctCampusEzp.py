#!/usr/bin/python
# coding: utf-8
import sys
doc=""" 
%prog [file] [output] [report] 
file is the name of the ezproxy report we want to process. 
Outputfile should include path, will be created if not existing and clobbered if existing
Report is the {campus} EZProxy _report file

"""
if __name__ == '__main__':
	ezpInFileName = sys.argv[1] #main log file
	ezpOutFileName = sys.argv[2] #new campus logfile
	ezpReportFileName = sys.argv[3]# campus session report
	with open (ezpOutFileName,'w') as ezpOutFile, open(ezpInFileName, 'r') as ezpInFile, open(ezpReportFileName, 'r') as ezpCampusSessf:
		sessions = []
		for line in ezpCampusSessf.readlines():                                                                                                                
			sessions.append(line[71:86])
		for line in ezpInFile.readlines():
			for session in sessions:                                                                                                                            
				if session in line:
					print line
					ezpOutFile.writelines(line)
					break
