package javaProblems.countTheDays;

import java.time.ZoneId;
import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;
import java.util.TimeZone;

public class countTheDays {

    long MS_IN_DAY = 86400000;

    public boolean incrementDays(Calendar d1, Calendar d2) {
        return (d1.get(Calendar.YEAR) != d2.get(Calendar.YEAR) || d1.get(Calendar.MONTH) != d2.get(Calendar.MONTH))
                || (d1.get(Calendar.DAY_OF_MONTH) != d2.get(Calendar.DAY_OF_MONTH)
                        && Math.abs(d1.getTime().getTime() - d2.getTime().getTime()) > MS_IN_DAY);
    }

    public String countDays(Date d) {
        int days = 0;
        TimeZone est = TimeZone.getTimeZone("EST");
        GregorianCalendar targetCalendar = new GregorianCalendar();
        GregorianCalendar sourceCalendar = new GregorianCalendar();
        targetCalendar.setTime(d);
        sourceCalendar.setTime(new Date());

        targetCalendar.setTimeZone(est);
        sourceCalendar.setTimeZone(est);

        System.out.println(String.format("Calendar1 = %s and Calendar2 = %s", targetCalendar.getTime().toString(),
                sourceCalendar.getTime().toString()));

        if (sourceCalendar.after(targetCalendar)
                && sourceCalendar.get(Calendar.DAY_OF_YEAR) != targetCalendar.get(Calendar.DAY_OF_YEAR)) {
            return "The day is in the past!";
        } else if (sourceCalendar.get(Calendar.YEAR) == targetCalendar.get(Calendar.YEAR)
                && sourceCalendar.get(Calendar.MONTH) == targetCalendar.get(Calendar.MONTH)
                && sourceCalendar.get(Calendar.DAY_OF_YEAR) == targetCalendar.get(Calendar.DAY_OF_YEAR)) {
            return "Today is the day!";
        }

        do {
            sourceCalendar.add(Calendar.DAY_OF_MONTH, 1);
            if (incrementDays(sourceCalendar, targetCalendar)) {
                days++;
            }
        } while (sourceCalendar.get(Calendar.YEAR) != targetCalendar.get(Calendar.YEAR)
                || sourceCalendar.get(Calendar.MONTH) != targetCalendar.get(Calendar.MONTH)
                || sourceCalendar.get(Calendar.DAY_OF_YEAR) != targetCalendar.get(Calendar.DAY_OF_YEAR));

        System.out.println(String.format("Calendar1 = %s and Calendar2 = %s", targetCalendar.getTime().toString(),
                sourceCalendar.getTime().toString()));
        return String.format("%d days", days);
    }

    public static void main(String[] args) {
        countTheDays days = new countTheDays();
        days.countDays(new Date(2022 - 1900, 8, 21));
    }

}
