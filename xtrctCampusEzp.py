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
        outputFiles = {}
        with open(ezpReportFileName, 'r') as ezpCampusSessf:
            print('Reading report: {}, writing to {}').format(
                ezpReportFileName,ezpOutFileName)
            ezpOutFile = open (ezpOutFileName,'w')
            for line in ezpCampusSessf.readlines():
                session = line[71:86]
                outputFiles[session] = ezpOutFile
    with open(ezpInFileName, 'r') as ezpInFile:
        print('Reading log {}').format(ezpInFileName)
        for count, line in enumerate(ezpInFile):
            printStatus(count)
            session = line.split(' ')[2]
            outfile = outputFiles.get(session)
            if outfile is not None:
                ezpOutFile.writelines(line)
    print("Completed.")
