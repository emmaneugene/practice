import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.Map;

public class Solution {

    public static void main(String[] args) throws IOException {
        if (args.length < 1) {
            System.out.println("Please provide a file path");
            return;
        }

        Map<String, Integer> shapeVals =
                Map.ofEntries(
                        Map.entry("rock", 1), Map.entry("paper", 2), Map.entry("scissors", 3));

        Map<String, String> shapeCodes =
                Map.ofEntries(
                        Map.entry("X", "rock"),
                        Map.entry("Y", "paper"),
                        Map.entry("Z", "scissors"));

        Map<String, Integer> matchupVals =
                Map.ofEntries(
                        Map.entry("AX", 3), // rock - rock
                        Map.entry("AY", 6), // rock - paper
                        Map.entry("AZ", 0), // rock - scissors
                        Map.entry("BX", 0), // paper - rock
                        Map.entry("BY", 3), // paper - paper
                        Map.entry("BZ", 6), // paper - scissors
                        Map.entry("CX", 6), // scissors - rock
                        Map.entry("CY", 0), // scissors - paper
                        Map.entry("CZ", 3) // scissors - scissors
                        );

        Map<String, Integer> endingVals =
                Map.ofEntries(
                        Map.entry("X", 0), // lose
                        Map.entry("Y", 3), // draw
                        Map.entry("Z", 6) // win
                        );

        Map<String, String> outcomes2 =
                Map.ofEntries(
                        Map.entry("AX", "scissors"), // lose(rock) = scissors
                        Map.entry("AY", "rock"), // draw(rock) = rock
                        Map.entry("AZ", "paper"), // win(rock) = paper
                        Map.entry("BX", "rock"), // lose(paper) = rock
                        Map.entry("BY", "paper"), // draw(paper) = paper
                        Map.entry("BZ", "scissors"), // win(paper) = scissors
                        Map.entry("CX", "paper"), // lose(scissors) = paper
                        Map.entry("CY", "scissors"), // draw(scissors) = scissors
                        Map.entry("CZ", "rock") // win(scissors) = rock
                        );

        int score1 = 0;
        int score2 = 0;

        List<String> lines = Files.readAllLines(Path.of(args[0]));
        for (String line : lines) {
            String[] vals = line.split(" ");
            score1 += shapeVals.get(shapeCodes.get(vals[1])) + matchupVals.get(vals[0] + vals[1]);
            score2 += shapeVals.get(outcomes2.get(vals[0] + vals[1])) + endingVals.get(vals[1]);
        }

        System.out.println("Part 1: " + score1);
        System.out.println("Part 2: " + score2);
    }
}
