// Import the event module used to raise and listen to events
// events are basically signals that something has happened
// Event usually returns a class
const EventEmitter = require('events');
// Create an object from the event class
const emmiter = new EventEmitter();

// Listen for an event
emmiter.on('messageLogged', function() {
	// Log a message to the console
	console.log('Listener called');
});

// Raise an event
emmiter.emit('messageLogged');

