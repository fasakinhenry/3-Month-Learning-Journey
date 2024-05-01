// Import the ecents module as a class
const EventEmitter = require('events');
// Import the log function from logger.js (class)
const Logger = require('./logger.js');
// Create a new object from the Logger class
const logger = new Logger();

// Register a listener to show logging

// Register a listener to show message logged
logger.on('messageLogged', (eventArg) => {
	console.log(`Listener called with an ID: ${eventArg['id']} and used the ${eventArg['url']} url`);
});

logger.log('Message');
