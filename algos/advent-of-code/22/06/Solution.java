import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.HashSet;
import java.util.Set;

/** Sliding window with increment counter */
public class Solution {

    public static void main(String[] args) throws IOException {
        if (args.length < 1) {
            System.out.println("Please provide a file path");
            return;
        }

        String input = Files.readString(Path.of(args[0]));

        System.out.println("Part 1: " + solution(input, 5));
        System.out.println("Part 2: " + (solution(input, 14) + 1));
    }

    private static int solution(String s, int uniqueCount) {
        Set<Character> chars = new HashSet<>();
        chars.add(s.charAt(0));
        int start = 0;

        for (int i = 1; i < s.length(); i++) {
            if (chars.contains(s.charAt(i))) {
                while (s.charAt(start) != s.charAt(i)) {
                    chars.remove(s.charAt(start++));
                }
                start++;
            } else {
                chars.add(s.charAt(i));

                if (chars.size() == uniqueCount) {
                    return i;
                }
            }
        }

        return -1;
    }
}
