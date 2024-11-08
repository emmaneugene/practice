import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Solution {

    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("Please provide a file path");
            return;
        }

        try (BufferedReader reader = new BufferedReader(new FileReader(args[0]))) {
            String line;
            int score1 = 0;
            int score2 = 0;

            while ((line = reader.readLine()) != null) {
                String[] assgns = line.split(",");
                int s1 = Integer.parseInt(assgns[0].split("-")[0]);
                int e1 = Integer.parseInt(assgns[0].split("-")[1]);
                int s2 = Integer.parseInt(assgns[1].split("-")[0]);
                int e2 = Integer.parseInt(assgns[1].split("-")[1]);

                if ((s1 >= s2 && e1 <= e2) || (s2 >= s1 && e2 <= e1)) {
                    score1 += 1;
                }

                if ((s1 >= s2 && s1 <= e2) || (s2 >= s1 && s2 <= e1)) {
                    score2 += 1;
                }
            }

            System.out.println("Part 1: " + score1);
            System.out.println("Part 2: " + score2);
        } catch (IOException e) {
            System.err.println(e.getMessage());
        }
    }
}
