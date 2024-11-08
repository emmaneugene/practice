import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;

public class Solution {

    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("Please provide a file path");
            return;
        }

        try (BufferedReader reader = new BufferedReader(new FileReader(args[0]))) {
            String line;
            int[] top3Cals = { 0, 0, 0 };
            int maxCals = 0;
            int currCals = 0;

            while ((line = reader.readLine()) != null) {
                try {
                    currCals += Integer.parseInt(line);
                } catch (NumberFormatException e) {
                    maxCals = Integer.max(currCals, maxCals);

                    for (int i = 0; i < top3Cals.length; i++) {
                        if (currCals > top3Cals[i]) {
                            int tmp;
                            for (int j = i; j < top3Cals.length; j++) {
                                tmp = top3Cals[j];
                                top3Cals[j] = currCals;
                                currCals = tmp;
                            }
                            break;
                        }
                    }

                    currCals = 0;
                }
            }

            maxCals = Integer.max(currCals, maxCals);

            for (int i = 0; i < top3Cals.length; i++) {
                if (currCals > top3Cals[i]) {
                    int tmp;
                    for (int j = i; j < top3Cals.length; j++) {
                        tmp = top3Cals[j];
                        top3Cals[j] = currCals;
                        currCals = tmp;
                    }
                    break;
                }
            }

            System.out.println("Part 1: " + maxCals);
            System.out.println("Part 2: " + Arrays.stream(top3Cals).sum());
        } catch (IOException e) {
            System.err.println(e.getMessage());
        }
    }
}
