import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;

public class Solution {
  public static void main(String[] args) {
    if (args.length < 1) {
      System.out.println("Please provide a file path");
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
          if (currCals > maxCals) {
            maxCals = currCals;
          }

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

      if (currCals > maxCals) {
        maxCals = currCals;
      }

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

      System.out.println("Most calories: " + maxCals);
      System.out.print("Top 3 calories: ");
      for (int c : top3Cals) {
        System.out.print(c + " ");
      }
      System.out.println("\nTotal of top 3 calories: " + Arrays.stream(top3Cals).reduce(0, (a, b) -> a + b));
    } catch (IOException e) {
      System.err.println(e.getMessage());
    }
  }
}
