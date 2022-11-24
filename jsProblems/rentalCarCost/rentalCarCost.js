/**
 *
 * @param {number} d - the # of days the car is rented for
 */
function rentalCarCost(d) {
  return d * 40 - ((d >= 3 && d < 7 ? 20 : 0) + (d >= 7 ? 50 : 0));
}

console.log(rentalCarCost(3));
