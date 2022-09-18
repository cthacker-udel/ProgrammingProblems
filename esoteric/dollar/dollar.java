package esoteric.dollar;

import java.util.Calendar;
import java.util.Comparator;
import java.util.Date;
import java.util.HashMap;
import java.util.TimeZone;
import java.util.Map.Entry;

public class dollar {

    /**
     * The timestamp class, which represents each label's contents, tracking it's
     * index, it's time of creation, and it's body
     */
    public static class Timestamp {

        public Date timestamp;
        public String body;
        public int index;

        /**
         * @constructor
         *              no-arg constructor, initializes timestamp to most recent date,
         *              and body to an empty string
         */
        public Timestamp() {
            this.timestamp = new Date();
            this.body = "";
        }

        /**
         * 1-arg constructor, initializes index to the index passed in, and sets the
         * other internal members to their defaults
         * 
         * @param newIndex - The index to set the internal index value to
         */
        public Timestamp(int newIndex) {
            this.index = newIndex;
            this.timestamp = new Date();
            this.body = "";
        }

    }

    public static void interpret(String tape) {
        String output = "";
        int index = 0;
        HashMap<Integer, Timestamp> labels = new HashMap<>();
        while (tape.length() < index) {
            char command = tape.charAt(index);
            switch (command) {
                case '_': {
                    output += (char) tape.length();
                    break;
                }
                case '-': {
                    tape += (char) tape.length();
                    break;
                }
                case '$': {
                    System.out.println(output);
                    if (tape.length() % 2 != 0) {
                        output = "";
                    }
                    break;
                }
                case '&': {
                    break;
                }
                case '@': {
                    if (!labels.containsKey(tape.length())) {
                        labels.put(tape.length(), new Timestamp());
                    }
                    break;
                }
                case '!': {
                    Object[] sortedLabels = labels.entrySet().stream()
                            .sorted(new Comparator<Entry<Integer, Timestamp>>() {

                                @Override
                                public int compare(Entry<Integer, Timestamp> e1, Entry<Integer, Timestamp> e2) {
                                    Calendar c1 = Calendar.getInstance();
                                    Calendar c2 = Calendar.getInstance();
                                    TimeZone tz = TimeZone.getTimeZone("est");
                                    c1.setTimeZone(tz);
                                    c2.setTimeZone(tz);
                                    c1.setTime(e1.getValue().timestamp);
                                    c2.setTime(e2.getValue().timestamp);

                                    return c1.before(c2) ? -1 : c1.after(c2) ? 1 : 0;
                                }

                            }).toArray();
                    final Entry<Integer, Timestamp> latestTimestamp = (Entry<Integer, Timestamp>) sortedLabels[sortedLabels.length
                            - 1];

                    // acquired latest label
                    break;
                }
                case '#': {

                }

            }
        }
    }

    public static void main(String[] args) {

    }

}
