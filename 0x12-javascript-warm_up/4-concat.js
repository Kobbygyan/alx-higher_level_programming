#!/usr/bin/node

// Get the two arguments using array destructuring
const [argv1, argv2] = process.argv.slice(2);

// Check if both arguments are defined
if (typeof argv1 !== 'undefined' && typeof argv2 !== 'undefined') {
  // Use console.log(...) to print the formatted output
  console.log(argv1 + ' is ' + argv2);
} else {
  console.log('Please provide two arguments.');
}
