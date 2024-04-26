console.log(__filename);
console.log(__dirname);

var url = 'http://mylogger.io/log';

function log(message) {
	// Send HTTP reuqests
	console.log(message)
}

// Export the log function
module.exports = log
