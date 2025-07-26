import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class Solution {

    public static void main(String[] args) throws IOException {
        if (args.length < 1) {
            System.out.println("Please provide a file path");
            return;
        }

        int score1 = 0;
        int score2 = 0;

        List<String> lines = Files.readAllLines(Path.of(args[0]));
        for (String line : lines) {
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
    }
}
