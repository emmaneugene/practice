import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashSet;
import java.util.Set;

/**
 * Sliding window with increment counter
 */
public class Solution {
    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("Please provide a file path");
            return;
        }

        try (BufferedReader reader = new BufferedReader(new FileReader(args[0]))) {

            String line = reader.readLine();

            System.out.println("Part 1: " + solution(line, 5));
            System.out.println("Part 2: " + (solution(line, 14) + 1));
        } catch (IOException e) {
            System.err.println(e.getMessage());
        }

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
