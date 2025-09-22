import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

/**
 * P1: Search with memoization
 *
 * <p>P2: Start with optimal path composed from P1, iteratively reassign
 */
public class Solution {

    static Map<String, Integer> memo = new HashMap<>();

    public static void main(String[] args) throws IOException {
        if (args.length < 1) {
            System.out.println("Please provide a file path");
            return;
        }

        final Pattern PATTERN =
                Pattern.compile(
                        "Valve (?<valve>\\w+) has flow rate=(?<rate>\\d+);"
                                + " tunnels? leads? to valves? (?<valves>[\\w, ]+)");

        List<String> lines = Files.readAllLines(Path.of(args[0]));
        Map<String, Set<String>> connections = new HashMap<>();
        Map<String, Integer> rates = new HashMap<>();

        for (String line : lines) {
            Matcher matcher = PATTERN.matcher(line);
            if (!matcher.matches()) continue;
            String valve = matcher.group("valve");
            int rate = Integer.parseInt(matcher.group("rate"));
            String connected = matcher.group("valves");

            connections.put(valve, Set.of(connected.split(", ")));
            rates.put(valve, rate);
        }

        // With BFS, compute minimum time it takes to reach all other valves from a given valve
        Map<String, Map<String, Integer>> minDists = new HashMap<>();
        for (String valve : connections.keySet()) {
            Set<String> explore = Set.of(valve);
            Map<String, Integer> tracker = new HashMap<>();
            int t = 0;

            while (!explore.isEmpty()) {
                Set<String> tmp = new HashSet<>();

                for (String v : explore) {
                    tracker.put(v, t);
                    for (String vAdj : connections.get(v)) {
                        if (!tracker.containsKey(vAdj)) {
                            tmp.add(vAdj);
                        }
                    }
                }

                t++;
                explore = tmp;
            }

            minDists.put(valve, tracker);
        }

        Map<String, Integer> nonZeroRates =
                rates.entrySet().stream()
                        .filter(e -> e.getValue() > 0)
                        .collect(Collectors.toMap(Entry::getKey, Entry::getValue));

        int p1 = optimal(minDists, nonZeroRates, new HashSet<>(), "AA", 30);
        System.out.println("Part 1: " + p1);
    }

    /**
     * Given:
     *
     * <ul>
     *   <li>Minimum connecting distances
     *   <li>Flow rates
     *   <li>Visited set
     *   <li>Time limit
     * </ul>
     *
     * Find the most amount of pressure that can be released, and the associated path for it
     */
    static int optimal(
            Map<String, Map<String, Integer>> minDists,
            Map<String, Integer> rates,
            Set<String> visited,
            String curr,
            int time) {

        String key = curr + "," + time + "," + visited.toString();
        if (memo.containsKey(key)) {
            return memo.get(key);
        }

        int maxPressure = 0;

        for (String valve : rates.keySet()) {
            Integer dist = minDists.get(curr).get(valve);
            if (visited.contains(valve) || dist == null || dist + 1 >= time) continue;

            int newTLeft = time - dist - 1;
            Set<String> newVisited = new HashSet<>(visited);
            newVisited.add(valve);

            int pressure = rates.get(valve) * newTLeft;
            pressure += optimal(minDists, rates, newVisited, valve, newTLeft);

            maxPressure = Math.max(maxPressure, pressure);
        }

        memo.put(key, maxPressure);
        return maxPressure;
    }
}
