// Import the ecents module as a class
const EventEmitter = require('events');
// Import the log function from logger.js (class)
const Logger = require('./logger.js');
// Create a new object from the Logger class
const logger = new Logger();
logger.log('Message');
