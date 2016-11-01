#!/usr/bin/python
# coding: utf-8
import sys
doc=""" 
%prog [file] [output] [report] 
file is the name of the ezproxy report we want to process. 
Outputfile should include path, will be created if not existing and clobbered if existing
Report is the {campus} EZProxy _report file

"""
count = 0
campuses=['cgu','cmc','hmc','kecksci','kgi','pit','pom','scr']
cf_prefix = 'ccl'
cf_post = '_report_'
cf_type = '.rpt'
def printStatus(curr):
	if curr%1000 == 0:
		sys.stdout.write('Processing line {} / low millions\r'.format(curr))
		sys.stdout.flush()
		
if __name__ == '__main__':
    ezpInFileName = sys.argv[1] #main log file
    ezpFilePrefix = ezpInFileName.split('.')[0]
    for campus in campuses:
        ezpOutFileName = ezpFilePrefix+"_"+campus+'.log'
        ezpReportFileName = cf_prefix+ezpFilePrefix+cf_post+campus+cf_type
        print('Reading report: {}, searching {}').format(ezpReportFileName,ezpInFileName)
        with open (ezpOutFileName,'w') as ezpOutFile, open(ezpInFileName, 'r') as ezpInFile, open(ezpReportFileName, 'r') as ezpCampusSessf:
            sessions = []
            for line in ezpCampusSessf.readlines():                                                                                                                
                sessions.append(line[71:86])
            print('Writing {}').format(ezpOutFileName)
            for count, line in enumerate(ezpInFile):
                printStatus(count)                                                                                                                            			
                for session in sessions:
                    #print session, line.split(' ')[2]
                    if session in line.split(' ')[2]:
                        ezpOutFile.writelines(line)
                        break
    print("Completed.")
