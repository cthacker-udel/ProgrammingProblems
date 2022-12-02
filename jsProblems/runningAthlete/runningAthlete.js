/**
 *
 * @param {string[]} act
 * @param {string} txt
 */
function runningAthlete(act, txt) {
  let resultStr = "";
  for (let i = 0; i < act.length; i++) {
    // O(n)
    switch (act[i]) {
      case "run": {
        switch (txt[i]) {
          case "_": {
            resultStr += "_";
            break;
          }
          case "|": {
            resultStr += "/";
          }
        }
        break;
      }
      case "jump": {
        switch (txt[i]) {
          case "_": {
            resultStr += "x";
            break;
          }
          case "|": {
            resultStr += "|";
            break;
          }
        }
        break;
      }
    }
  }
  return resultStr;
}
