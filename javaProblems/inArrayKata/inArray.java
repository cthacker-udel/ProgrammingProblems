import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashSet;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class WhichAreIn {

    public static String[] inArray(String[] array1, String[] array2) {
        ArrayList<String> strList2 = (ArrayList<String>) Stream.of(array2).collect(Collectors.toList());
        System.out.println(Arrays.toString(array1));
        strList2.forEach(System.out::println);
        HashSet<String> strList3 = new HashSet<>();
        for (String eachWord : array1) {
            for (int i = 0; i < strList2.size(); i++) {
                String theWord = strList2.get(i);
                if (theWord.contains(eachWord)) {
                    strList3.add(eachWord);
                }
            }
        }
        System.out.println("sorted hashset");
        ArrayList<String> strList = (ArrayList<String>) strList3.stream().sorted(new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return o1.compareTo(o2);
            }
        }).collect(Collectors.toList());
        System.out.println("------");
        strList.forEach(System.out::println);
        return strList3.toArray(String[]::new);
    }
}
