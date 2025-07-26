import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.List;

public class Solution {

    public static void main(String[] args) throws IOException {
        if (args.length < 1) {
            System.out.println("Please provide a file path");
            return;
        }

        List<String> lines = Files.readAllLines(Path.of(args[0]));

        int[] top3 = {0, 0, 0};
        int max = 0;
        int curr = 0;

        for (String line : lines) {
            try {
                curr += Integer.parseInt(line);
            } catch (NumberFormatException e) {
                max = Integer.max(curr, max);
                insert(top3, curr);
                curr = 0;
            }
        }

        max = Integer.max(curr, max);
        insert(top3, curr);

        System.out.println("Part 1: " + max);
        System.out.println("Part 2: " + Arrays.stream(top3).sum());
    }

    public static void insert(int[] vals, int val) {
        for (int i = 0; i < vals.length; i++) {
            if (val > vals[i]) {
                int tmp;
                for (int j = i; j < vals.length; j++) {
                    tmp = vals[j];
                    vals[j] = val;
                    val = tmp;
                }
                break;
            }
        }
    }
}
