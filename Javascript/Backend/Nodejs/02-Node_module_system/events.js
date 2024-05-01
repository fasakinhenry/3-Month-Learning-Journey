// Import the event module used to raise and listen to events
// events are basically signals that something has happened
// Event usually returns a class
const EventEmitter = require('events');
// Create an object from the event class
const emmiter = new EventEmitter();

// Listen for the logging event
emmiter.addListener('logging', (eventArg) => {
	// Show progress of application and log the message to be printed to console
	console.log('logging', eventArg['data']);
});

// Listen for an event
emmiter.on('messageLogged', (arg) => {
	// Log a message to the console
	console.log('Listener called', arg);
});

// Raise an event for logging
emmiter.emit('logging', {data: 'message'})

// Raise an event for the logged message
emmiter.emit('messageLogged', {id: 1, url: 'http://'});

