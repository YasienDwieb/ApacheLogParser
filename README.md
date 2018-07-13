# ApacheLogParser
Parser for Apache log file that stores data and extracts useful insights out of it.

### Place your acess log file in log directory instead of the empty one

### Then, run ($python processlog.py) in your terminal which will populate mongo db with log records. 

### Requirements:
   * Python
   * Mongo 
	 * Mongo Client (to connect to mongo from python)
			installation: pip install pymongo

### Useful info extraction functions are available in useful_data.py script
### which are:
   * findWhereFileExists: Gets requests to a specific path
	 * findHostRequests: Get request from a specific host to any file/path on your server
	 * findByUserAgent: Get requests made using a specific user agent
	 * orderByHitsPerPath: Orders your files/pathes based on hits