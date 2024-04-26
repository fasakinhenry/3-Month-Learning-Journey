// Import the OS module from Node
const os = require('os');

// Use the OS module to get the total memory of the computer
const totalMemory = os.totalmem();
// Use the OS module to get the free memmory of the computer
const freeMemory = os.freemem();

// Log the total and free memory of the system to the console
console.log(`Total Memory: ${totalMemory} \nFree Memory: ${freeMemory}`);
// console.log('Total Memory: ' + totalMemory, '\n' + 'Free Memory: ' + freeMemory);
