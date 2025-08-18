import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Collections;
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
 * <p>P2: Find all (visitedSet, pressure) pairs, then find two disjoint sets with max combined
 * pressure
 */
public class Solution {

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
        Map<String, Set<String>> valveAdj = new HashMap<>();
        Map<String, Integer> valveRates = new HashMap<>();

        for (String line : lines) {
            Matcher matcher = PATTERN.matcher(line);
            if (!matcher.matches()) continue;
            String valve = matcher.group("valve");
            int rate = Integer.parseInt(matcher.group("rate"));
            String connected = matcher.group("valves");

            valveAdj.put(valve, Set.of(connected.split(", ")));
            valveRates.put(valve, rate);
        }

        Map<String, Map<String, Integer>> valveToValveShortestTimes = bfsTime(valveAdj);

        Map<String, Integer> posValveRates =
                valveRates.entrySet().stream()
                        .filter(e -> e.getValue() > 0)
                        .collect(Collectors.toMap(Entry::getKey, Entry::getValue));

        // Part 1: Find max pressure for single agent in 30 minutes
        Map<Set<String>, Integer> p1Paths = new HashMap<>();
        collectAllPaths(
                valveToValveShortestTimes, posValveRates, new HashSet<>(), "AA", 30, 0, p1Paths);
        int p1 = p1Paths.values().stream().mapToInt(Integer::intValue).max().orElse(0);
        System.out.println("Part 1: " + p1);

        // Part 2: Collect all (visitedSet, pressure) pairs in 26 minutes, find best disjoint pair
        Map<Set<String>, Integer> allPaths = new HashMap<>();
        collectAllPaths(
                valveToValveShortestTimes, posValveRates, new HashSet<>(), "AA", 26, 0, allPaths);

        int p2 = 0;
        for (var entry1 : allPaths.entrySet()) {
            for (var entry2 : allPaths.entrySet()) {
                if (Collections.disjoint(entry1.getKey(), entry2.getKey())) {
                    p2 = Math.max(p2, entry1.getValue() + entry2.getValue());
                }
            }
        }
        System.out.println("Part 2: " + p2);
    }

    /** Use BFS to compute the minimum time it takes to reach all other valves from a given valve */
    static Map<String, Map<String, Integer>> bfsTime(Map<String, Set<String>> valveAdj) {

        Map<String, Map<String, Integer>> valveToValveShortestTimes = new HashMap<>();
        for (String valve : valveAdj.keySet()) {
            Set<String> explore = Set.of(valve);
            Map<String, Integer> tracker = new HashMap<>();
            int t = 0;

            while (!explore.isEmpty()) {
                Set<String> tmp = new HashSet<>();

                for (String v : explore) {
                    tracker.put(v, t);
                    for (String vAdj : valveAdj.get(v)) {
                        if (!tracker.containsKey(vAdj)) {
                            tmp.add(vAdj);
                        }
                    }
                }

                t++;
                explore = tmp;
            }

            valveToValveShortestTimes.put(valve, tracker);
        }

        return valveToValveShortestTimes;
    }

    /**
     * Recursively explores all reachable valve combinations and records the maximum pressure
     * achievable for each visited set. Used for Part 2 to find optimal disjoint paths.
     *
     * @param valveToValveShortestTimes shortest travel times between all valve pairs
     * @param rates flow rates for non-zero valves
     * @param visited set of valves opened so far
     * @param curr current valve position
     * @param time remaining time
     * @param pressure accumulated pressure from opened valves
     * @param allPaths output map storing best pressure for each visited set
     */
    static void collectAllPaths(
            Map<String, Map<String, Integer>> valveToValveShortestTimes,
            Map<String, Integer> rates,
            Set<String> visited,
            String curr,
            int time,
            int pressure,
            Map<Set<String>, Integer> allPaths) {

        allPaths.merge(visited, pressure, Math::max);

        for (String valve : rates.keySet()) {
            Integer dist = valveToValveShortestTimes.get(curr).get(valve);
            if (visited.contains(valve) || dist == null || dist + 1 >= time) continue;

            int newTime = time - dist - 1;
            Set<String> newVisited = new HashSet<>(visited);
            newVisited.add(valve);
            int newPressure = pressure + rates.get(valve) * newTime;

            collectAllPaths(
                    valveToValveShortestTimes,
                    rates,
                    newVisited,
                    valve,
                    newTime,
                    newPressure,
                    allPaths);
        }
    }
}
