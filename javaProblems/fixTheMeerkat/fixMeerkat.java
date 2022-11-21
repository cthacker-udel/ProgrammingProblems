import java.util.stream.Stream;

public class WrongEndHead {
    public static String[] fixTheMeerkat(String[] arr) {
        return Stream.of(arr).map(e -> new String[] { e[2], e[1], e[0] }).toArray();
    }
}