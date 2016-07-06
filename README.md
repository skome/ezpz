# ezpz
EZPZ is a collection of tools to support OCLC EZProxy log and report file analyses.  
They are designed around currently manual steps to collate files.   
The files include the EZProxy Report files and the EZProxy Log files.

##Processing goals include:
###Process EZProxy Report files:
* Extract campus per user		
* Anonymize userids
* Extract Date and time into fields
* Extract session id
* Store as csv

###Process EZProxy log files:
* Extract session id
* Extract URLs
* Break URLS into components: service, server, resource
* Store as CSV
* Other stuff, TBD

##Summary of Analysis:
Combine the monthly reports and the daily log files into a set of monthly reports about users, resources, campuses, and time.  
To do this create monthly logs from the daily logs(1), join them to the monthly report via the session id(2,3). 
In that process create a campus id, add a user status (student, faculty, etc), and anonymize userids.  Then generate reports.

##Processing Steps:
1. Append the daily log files into a monthly file
  1. `ls ezp*.log > 201601.lst`
  2. `cat $(cat 201601.lst) > 201601.log`
  3. Delete the daily files
2. Cut the top of the report file into a new file(s)
  1. All campuses: `head -n $(grep -n Login\ summary ccl201511_report.log |cut -d: -f1) ccl201511_report.log`
  2. Optional: Only CGU (for example): `head -n $(grep -n Login\ summary ccl201512_report.log |cut -d: -f1) ccl201512_report.log |grep cgu > ezp201512CGU.txt`

  OR: use bash script `ezpPullCampusReport [monthly report] [campus report] [campus]`
  * e.g.  `~/ezpPullCampusReport ccl201602_report.log ccl201602_report_PIT.log pit`
  * ...will read ccl201602_report.log, create ccl201602_report_PIT.log

c. ezpCountUIDS.py will count in the report the unique user ids per campus.

3. (optional) Create a campus log file with xtrctCampusezp.py using the above campus report and the full log file, e.g.  `~/ezpz/xtrctCampusEzp.py 201604.log ezp201604KGI.log ccl201604_report_KGI.log` ...will extract a campus's log lines into a new file like ezp201601KGI.log
####Todo: 
  1. Generalize xtrctKGIezp.py to work for any campus, any month
  2. Speed improvements needed!
4. Extract URLs from the new file and split them into component parts for analysis: `findezpURLS logfile output`


