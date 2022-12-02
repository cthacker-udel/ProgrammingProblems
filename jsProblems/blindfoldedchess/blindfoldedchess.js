const fs = require("fs");

/**
 *
 * @param {number[][]} moves - The list of available moves
 * @param {number[]} curr_pattern - The current pattern we have
 * @param {number} curr_x - The current x
 * @param {number} curr_y - The current y
 * @param {number[][]} guesses - The array of guesses we have made, cannot exceed 500
 */
function blindfoldChess(moves) {
  let moves = {}; // hashmap consisting of the initial moves, and their chains
  let visited_spots = {}; // hashmap consisting of the initial moves, and all spots we visited along that path
  let curr_x = 0;
  let curr_y = 0;
  for (let i = 0; i < moves.length; i++) {
    moves[moves[i]] = [moves[i]];
    curr_x += moves[i][0];
    curr_y += moves[i][1];
    visited_spots[moves[i]];
  }
}

// So what we need to do, is to pick a starting move, and then simulate the subsequent moves while removing duplicate moves from the equation
// Then we map out each move, at each point, and what that resulting move places the piece at, as we are adding moves to the current chain, we check has that location already been
// visited, if so, we don't add it to the chain, and move on to another move. Repeating this process for each initial move.

const kingMoves = [
  [-1, 1],
  [1, 0],
  [0, -1],
  [0, 1],
  [-1, 0],
  [1, -1],
  [-1, -1],
  [1, 1],
];

fs.writeFileSync("output.txt", JSON.stringify(blindfoldChess(kingMoves)));
console.log(blindfoldChess(kingMoves));
