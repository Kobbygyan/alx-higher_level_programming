#!/usr/bin/node

// Check the number of command-line arguments
const numArgs = process.argv.length - 2; // Subtract 2 to account for the 'node' and script name arguments

// Use a conditional statement to print the appropriate message
if (numArgs === 0) {
  console.log('No argument');
} else if (numArgs === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
