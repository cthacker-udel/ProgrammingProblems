const MillisecondConstants = {
  DAY: 86_400_000,
  WEEK: 604_800_000,
};

const Dates = {
  SUNDAY: 0,
  MONDAY: 1,
  TUESDAY: 2,
  WEDNESDAY: 3,
  THURSDAY: 4,
  FRIDAY: 5,
  SATURDAY: 6,
};

const Direction = {
  ASC: 0,
  DESC: 1,
};

/**
 *
 * @param date - The date to span it's surrounding dates for
 * @returns The day that is found from searching around the current date
 */
const findDay = (date, day, direction) => {
  let foundDate = date.getDay() === day;
  let movingDate = new Date(date);
  while (!foundDate) {
    movingDate = new Date(
      movingDate.getTime() +
        (direction === Direction.ASC
          ? MillisecondConstants.DAY
          : -MillisecondConstants.DAY)
    );
    foundDate = movingDate.getDay() === day;
  }
  return movingDate;
};

/**
 * Generates the date range from the date supplied to it
 *
 * @param date - The date we are analyzing
 */
const generateDateRange = (date) => {
  const lowerDate = findDay(
    new Date(date.getTime() - MillisecondConstants.WEEK),
    Dates.SATURDAY,
    Direction.ASC
  );
  const upperDate = findDay(new Date(date), Dates.SUNDAY, Direction.DESC);
  return [lowerDate, upperDate];
};

generateDateRange(new Date());
