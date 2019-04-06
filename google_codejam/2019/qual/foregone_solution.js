// https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/0000000000088231

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let [numCases, currCase] = [null, 0];
rl.on('line', (input) => {
  if (numCases ===  null) {
    numCases = +input;
    return;
  }
  if (currCase < numCases) {
    console.log(`Case #${++currCase}: ${solve(input)}`);
  }
});

function solve(input) {
  const aArr = [];
  for (let i = 0; i < input.length; i++) {
    const num = +input[i];
    aArr.push(num !== 4 ? num : 2);
  }
  const a = +aArr.join('');
  return `${a} ${+input - a}`;
}
