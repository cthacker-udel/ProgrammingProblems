package javaProblems.tortoise;

public class tortoiseRace {

    public static int[] race(int v1, int v2, int g) {

        if (v1 >= v2) {
            return null;
        }
        double v1PerHour = v1;
        double v2PerHour = v2;
        double v1PerMinute = v1 / 60.0;
        double v2PerMinute = v2 / 60.0;
        double v1PerSecond = (v1 / 60.0) / 60.0;
        double v2PerSecond = (v2 / 60.0) / 60.0;
        double totalDistanceV1 = g;
        double totalDistanceV2 = 0;
        int seconds = 0;
        int minutes = 0;
        int hours = 0;
        while (totalDistanceV2 < totalDistanceV1) {
            if (totalDistanceV1 - totalDistanceV2 + v1PerHour >= v2PerHour) {
                totalDistanceV1 += v1PerHour;
                totalDistanceV2 += v2PerHour;
                hours++;
            } else if (totalDistanceV1 - totalDistanceV2 + v1PerMinute >= v2PerMinute) {
                totalDistanceV1 += v1PerMinute;
                totalDistanceV2 += v2PerMinute;
                minutes++;
            } else {
                totalDistanceV1 += v1PerSecond;
                totalDistanceV2 += v2PerSecond;
                seconds++;
            }
            if (seconds == 60) {
                minutes++;
                if (minutes == 60) {
                    hours++;
                    minutes = 0;
                }
                seconds = 0;
            } else if (minutes == 60) {
                hours++;
                minutes = 0;
            }
        }
        return new int[] { hours, minutes, seconds > 0 ? seconds - 1 : 0 };

    }

    public static void main(String[] args) {
        race(720, 850, 70);
    }

}
