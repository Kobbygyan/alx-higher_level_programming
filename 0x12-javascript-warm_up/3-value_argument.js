#!/usr/bin/node

// Get the first argument using array destructuring
const [firstArgument] = process.argv.slice(2);

// Use a conditional statement to print the appropriate message
if (typeof firstArgument === 'undefined') {
  console.log('No argument');
} else {
  console.log(firstArgument);
}
