# ezpz
EZPZ is a collection of tools to support OCLC EZProxy log and report file analyses.  
They are designed around currently manual steps to collate files.   
The files include the EZProxy Report files and the EZProxy Log files.

Processing goals include:
Process EZProxy Report files:
* Extract campus per user		
* Anonymize userids
* Extract Date and time into fields
* Extract session id
* Store as csv
Process EZProxy log files:
* Extract session id
* Extract URLs
* Break URLS into components: service, server, resource
* Store as CSV
* Other stuff, TBD

Summary of Analysis:
Combine the monthly reports and the daily log files into a set of monthly reports about users, resources, campuses, and time.  
To do this create monthly logs from the daily logs(1), join them to the monthly report via the session id(2,3). 
In that process create a campus id, add a user status (student, faculty, etc), and anonymize userids.  Then generate reports.
