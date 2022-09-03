package javaProblems.reverseNumber;

import java.util.ArrayList;
import java.util.Collections;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class reverseNumber {
    public static int reverse(int number) {
        ArrayList<String> digits = number > 0
                ? Stream.of(String.valueOf(number).split("")).collect(ArrayList<String>::new,
                        ArrayList<String>::add, ArrayList<String>::addAll)
                : Stream.of(String.valueOf(number).substring(1).split("")).collect(ArrayList<String>::new,
                        ArrayList<String>::add, ArrayList<String>::addAll);
        Collections.reverse(digits);
        return number > 0 ? Integer.parseInt(digits.stream().collect(Collectors.joining("")))
                : -1 * Integer.parseInt(digits.stream().collect(Collectors.joining("")));
    }

    public static void main(String[] args) {
        reverse(-123);
    }
}
