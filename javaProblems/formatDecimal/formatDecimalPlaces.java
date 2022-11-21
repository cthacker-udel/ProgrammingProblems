import java.text.DecimalFormat;

public class Numbers {

    public static double TwoDecimalPlaces(double number) {
        return Double.parseDouble(new DecimalFormat(".##").format(number).toString());
    }
}