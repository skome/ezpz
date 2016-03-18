#!/usr/bin/python
with open('ezp201602.log','r') as ezpf, open('ezp201602KGI.log','w') as ezpKGIf:
	sessions = []
	with open('ccl201602_report_KGI.log','r') as ezpKGISessf:
		for line in ezpKGISessf.readlines():                                                                                                                
			sessions.append(line[71:86])
	for line in ezpf:
		for session in sessions:                                                                                                                            
			if session in line:
				print line
				ezpKGIf.writelines(line)
				break
