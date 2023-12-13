/*

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". 
Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. 
DNA strand is never empty or there is no DNA at all (again, except for Haskell).

Example: (input --> output)

"ATTGC" --> "TAACG"
"GTAT" --> "CATA"

*/

// My solution:
function DNAStrand(dna){
    let dnaArr = dna.split(''); // split the string into an array
    let newArr = []; // create an empty array
    dnaArr.forEach(char => { // loop through the array
      if (char === 'A') { // if the char is 'A'
        newArr.push('T'); // push 'T' to the new array
      } else if (char === 'T') { // if the char is 'T'
        newArr.push('A'); // push 'A' to the new array
      } else if (char === 'G') { // if the char is 'G'
        newArr.push('C'); // push 'C' to the new array
      } else if (char === 'C') { // if the char is 'C'
        newArr.push('G'); // push 'G' to the new array
      }
    })
    return newArr.join(''); // join the array into a string
}

// Other solutions:
// Solution 1: By warriors
function DNAStrand(dna){
    return dna.replace(/./g, function(c) {
      return DNAStrand.pairs[c]
    })
  }
  
  DNAStrand.pairs = {
    A:'T',
    T:'A',
    C:'G',
    G:'C',
  }