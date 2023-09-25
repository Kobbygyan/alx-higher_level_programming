#!/usr/bin/node

// Define the add function with the given prototype
function add (a, b) {
  return a + b;
}

// Get the two integers from the command line arguments
const arg1 = parseInt(process.argv[2], 10);
const arg2 = parseInt(process.argv[3], 10);

// Check if the conversion resulted in valid integers
if (!isNaN(arg1) && !isNaN(arg2)) {
  const result = add(arg1, arg2);
  console.log(result);
} else {
  console.log('Invalid input. Please provide two integers.');
}
