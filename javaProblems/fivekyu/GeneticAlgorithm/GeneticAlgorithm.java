package javaProblems.fivekyu.GeneticAlgorithm;

import java.util.stream.IntStream;
import java.util.List;
import java.util.function.ToDoubleFunction;

public class GeneticAlgorithm {

    private String generate(int length) {

    }

    private String[] select(List<String> population, List<Double> fitnesses) {
        double[] sums = population.stream()
                .map(e -> IntStream.range(0, e.length()).map(f -> e.charAt(f) == '0' ? f + 1 : 0).sum())
                .mapToDouble(e -> e).toArray();
        double[] multiples = population.stream()
                .map(e -> IntStream.range(0, e.length()).map(f -> e.charAt(f) == '1' ? f + 1 : 1).mapToDouble(e -> e)
                        .reduce((e1, e2) -> e1 * 1.0 * e2).getAsDouble())
                .mapToDouble(e -> e).toArray();

        return new String[] {};
    }

    private String mutate(String chromosome, double p) {

    }

    private String[] crossover(String chromosome1, String chromosome2) {

    }

    private String run(ToDoubleFunction<String> fitness, int length, double p_c, double p_m) {

    }

    public String run(ToDoubleFunction<String> fitness, int length, double p_c, double p_m, int iterations) {

    }

}
