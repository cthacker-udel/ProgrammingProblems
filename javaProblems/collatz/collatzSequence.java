package javaProblems.collatz;

import java.util.ArrayList;
import java.util.stream.Collectors;

public class collatzSequence {

    public static String collatz(int n) {
        ArrayList<String> sequence = new ArrayList<>();
        while (n != 1) {
            sequence.add(String.format("%d", n));
            if (n % 2 == 0) {
                n /= 2;
            } else {
                n = (3 * n) + 1;
            }
        }
        sequence.add("1");
        return sequence.stream().collect(Collectors.joining("->"));
    }

}
