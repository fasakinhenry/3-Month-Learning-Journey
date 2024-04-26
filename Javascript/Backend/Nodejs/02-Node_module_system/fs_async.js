// Import the fs module to interact with the file system
const fs = require('fs');

// Use the fs module to read all the files in a directory asynchronously
fs.readdir('./', function(err, files) {
	if (err) console.log('Error', err);
	else console.log('Files in this directory includes: ', files);
});
