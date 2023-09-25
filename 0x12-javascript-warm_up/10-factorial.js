#!/usr/bin/node

// Define the factorial function using recursion
function factorial (n) {
  // Base case: factorial of NaN is 1
  if (isNaN(n)) {
    return 1;
  }

  // Base case: factorial of 0 is 1
  if (n === 0) {
    return 1;
  }

  // Recursive case: compute the factorial using recursion
  return n * factorial(n - 1);
}

// Get the integer from the command line argument
const arg1 = parseInt(process.argv[2], 10);

// Check if the conversion resulted in a valid integer
if (!isNaN(arg1)) {
  const result = factorial(arg1);
  console.log(`Factorial of ${arg1} is ${result}`);
} else {
  console.log('Invalid input. Please provide an integer.');
}
