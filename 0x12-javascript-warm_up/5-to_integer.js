#!/usr/bin/node

// Get the first argument from the command line
const arg1 = process.argv[2];

// Use the parseInt function to convert the argument to an integer
const number = parseInt(arg1, 10);

// Check if the conversion resulted in a valid integer
if (!isNaN(number)) {
  console.log(`My number: ${number}`);
} else {
  console.log('Not a number');
}
