package javaProblems.quadraticEquation;

public class QuadraticEquation {

    /**
     * Returns the root of the quadratic formula given a, b, and c
     * 
     * @param a - a in the quadratic formula
     * @param b - b in the quadratic formula
     * @param c - c in the quadratic formula
     * @return The resultant of the quadratic formula
     */
    public static int quadraticEquation(int a, int b, int c) {
        final int upperHalf = (int) ((-1 * b) + Math.round(Math.sqrt((b * b) - 4 * a * c)));
        final int lowerHalf = 2 * a;
        return upperHalf / lowerHalf;
    }
}