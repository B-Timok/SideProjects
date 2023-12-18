// Date: 02/18/21

/**
 * Sorts the digits of a given number in descending order.
 * 
 * @param {number} n - The number to sort the digits of.
 * @returns {number} The number with its digits sorted in descending order.
 */
function descendingOrder1(n) {
    const digits = Array.from(String(n), Number); // Convert number to an array of digits
    const sortedDigits = digits.sort((a, b) => b - a); // Sort the digits in descending order
    const result = parseInt(sortedDigits.join('')); // Convert the sorted digits back to a number
    return result;
}

// more easy to understand solution
function descendingOrder2(n) {
    return parseInt(String(n).split('').sort().reverse().join(''));
}

// tests
console.log(descendingOrder2(0)); // 0
console.log(descendingOrder2(1)); // 1
console.log(descendingOrder2(123456789)); // 987654321
console.log(descendingOrder2(1021)); // 2110