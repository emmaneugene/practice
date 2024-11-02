import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

public class Solution {
    public static void main(String[] args) {

        if (args.length < 1) {
            System.out.println("Please provide a file path");
            return;
        }

        int score1 = 0;
        int score2 = 0;
        List<String> lines = new ArrayList<>();
        String line;

        try (BufferedReader reader = new BufferedReader(new FileReader(args[0]))) {

            while ((line = reader.readLine()) != null) {
                // Part 1
                int strLen = line.length();
                Set<Character> s1 = line.substring(0, strLen / 2)
                        .chars()
                        .mapToObj(ch -> (char) ch)
                        .collect(Collectors.toSet());
                Set<Character> s2 = line.substring(strLen / 2, strLen)
                        .chars()
                        .mapToObj(ch -> (char) ch)
                        .collect(Collectors.toSet());

                s1.retainAll(s2);
                score1 += s1.stream()
                        .map(c -> getPriority(c))
                        .reduce(0, (a, b) -> a + b);

                // Part 2
                lines.add(line);
                if (lines.size() == 3) {
                    Set<Character> g1 = lines.get(0).chars().mapToObj(ch -> (char) ch).collect(Collectors.toSet());
                    Set<Character> g2 = lines.get(1).chars().mapToObj(ch -> (char) ch).collect(Collectors.toSet());
                    Set<Character> g3 = lines.get(2).chars().mapToObj(ch -> (char) ch).collect(Collectors.toSet());

                    g1.retainAll(g2);
                    g1.retainAll(g3);

                    score2 += g1.stream().map(c -> getPriority(c)).reduce(0, (a, b) -> a + b);

                    lines.clear();
                }

            }

        } catch (IOException e) {
            System.out.println("Error processing part 1");
            System.err.println(e.getMessage());
        }

        System.out.println("Part 1: " + score1);
        System.out.println("Part 2: " + score2);
    }

    private static int getPriority(char c) {
        if (Character.isUpperCase(c)) {
            return c - 'A' + 27;
        }
        return c - 'a' + 1;
    }
}
