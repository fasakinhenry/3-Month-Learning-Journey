// Import the fs Module to interact with the file system
const fs = require('fs');

// Use the fs module to read file in a directory synchronously
 const files = fs.readdirSync('./');
console.log(files);
