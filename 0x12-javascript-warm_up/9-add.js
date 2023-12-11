#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const args = process.argv.slice(2);

const num1 = parseInt(args[0]);
const num2 = parseInt(args[1]);

if (!isNaN(num1) && !isNaN(num2)) {
  const result = add(num1, num2);
  console.log(`The addition of ${num1} and ${num2} is: ${result}`);
} else {
  console.log('Invalid input. Please provide two integers.');
}