#!/usr/bin/node

// Get the first argument from the command line
const arg1 = process.argv[2];

// Use the parseInt function to convert the argument to an integer
const size = parseInt(arg1, 10);

// Check if the conversion resulted in a valid integer
if (!isNaN(size)) {
  // Use a nested for loop to print the square
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
