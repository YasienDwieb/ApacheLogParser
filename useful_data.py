from pymongo import MongoClient
import time

class LogOps():
	client = MongoClient('mongodb://localhost:27017/')
	
	def findWhereFileExists(self,file):
		db=self.client.testdb
		file_occurences = db.logs.find({'path': file})
		return file_occurences

	def findHostRequests(self,host):
		db=self.client.testdb
		file_occurences = db.logs.find({'host': host})
		return file_occurences 

	def findByUserAgent(self,useragent):
		db=self.client.testdb
		file_occurences = db.logs.find({"$text":{"$search":useragent}})
		return file_occurences 

	def orderByHitsPerPath(self):
		db=self.client.testdb
		file_occurences = db.logs.aggregate([{"$group":{"_id":"$path","num_rows":{"$sum":1}}},{"$sort":{"num_rows":1}}])
		return file_occurences 

apachelog=LogOps()
# logs=apachelog.findWhereFileExists('/cgi-sys/defaultwebpage.cgi')
# logs=apachelog.findHostRequests('180.76.15.19')
# logs=apachelog.findByUserAgent('Mozilla')
# start = time.time()
logs=apachelog.orderByHitsPerPath()
# end = time.time()
# print 'Time elasped: '+str(end - start)
for i in logs:
	print i