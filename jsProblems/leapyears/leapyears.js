/**
 * Returns whether or not the given year is a leap year
 *
 * @param {number} year - the year to evaluate if it is a leap year
 */
const isLeapYear = (year) => {
  return year % 4 == 0 && !year % 100 == 0 && year % 400 == 0;
};

isLeapYear(1000);
