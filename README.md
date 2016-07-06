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
