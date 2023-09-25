#!/usr/bin/node

// Get the first argument from the command line
const arg1 = process.argv[2];

// Use the parseInt function to convert the argument to an integer
const x = parseInt(arg1, 10);

// Check if the conversion resulted in a valid integer
if (!isNaN(x)) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
