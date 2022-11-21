export const checkCoupon = (
  enteredCode: string,
  correctCode: string,
  currentDate: string,
  expirationDate: string
): boolean =>
  new Date(currentDate).getTime() <= new Date(expirationDate).getTime() &&
  enteredCode === correctCode;
