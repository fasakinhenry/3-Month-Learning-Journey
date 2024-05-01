// console.log(__filename);
// console.log(__dirname);
// import the events module as a class
const EventEmitter = require('events');

var url = 'http://mylogger.io/log';
class Logger extends EventEmitter {
	log(message) {
		// Send HTTP requests
		console.log(message);
		
		// Raise events
		this.emit('logging', {data: 'message'});
		this.emit('messageLogged', {id: 1, url: 'http://'});
	}
}
function log(message) {
	// Send HTTP reuqests
	console.log(message)
}

// Export the log function
module.exports = Logger
