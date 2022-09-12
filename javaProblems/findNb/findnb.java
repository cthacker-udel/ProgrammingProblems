package javaProblems.findNb;

import java.util.stream.IntStream;

public class findnb {

    public static long findNb(long m) {

        long accumulator = 0;
        long digit = 1;
        while (accumulator < m) {
            accumulator += digit * digit * digit;
            digit++;
        }
        return accumulator == m ? accumulator : -1;
    }

}
