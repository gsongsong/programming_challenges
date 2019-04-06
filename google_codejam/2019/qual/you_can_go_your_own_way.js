// https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881da

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let [numCases, currCase, len] = [null, 0, null];
rl.on('line', (input) => {
  if (numCases ===  null) {
    numCases = +input;
    return;
  }
  if (currCase < numCases) {
    if (len === null) {
      len = +input;
      return;
    }
    console.log(`Case #${++currCase}: ${solve(input)}`);
    len = null;
  }
});

function solve(input) {
  const path = input.split('');
  return path.map((char) => char === 'E' ? 'S' : 'E').join('');
}
