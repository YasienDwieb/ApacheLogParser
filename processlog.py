from pymongo import MongoClient
import apachelog, sys
from dateutil.parser import parse

# Format copied and pasted from Apache conf - use raw string + single quotes
format = r'%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"'
p = apachelog.parser(format)

client = MongoClient('mongodb://localhost:27017/')
db=client.testdb

for line in open('log/access_log'):
	data = p.parse(line)     	
	if data['%r']:
		accessed_file=data['%r'].split()
		if(len(accessed_file)>2):
			accessed_file_name=accessed_file[1]
		else:
			accessed_file_name=accessed_file[0]
	else:
			accessed_file_name=''
	apache_date=data['%t'].replace("[","").replace("]","")
	time=parse(apache_date[:11] + " " + apache_date[12:])
	log_entry={"host":data['%h'],"time":time,"path":accessed_file_name,"referer":data["%{Referer}i"],"useragent":data['%{User-Agent}i']}
	db.logs.insert_one(log_entry)
