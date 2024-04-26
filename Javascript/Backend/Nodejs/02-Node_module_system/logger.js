var url = 'http://mylogger.io/log';

function log(message) {
	// Send HTTP reuqests
	console.log(message)
}

// Export the log function
module.exports.log = log
// Export the url variable as an endpoint object (not needed)
module.exports.endPoint = url;
