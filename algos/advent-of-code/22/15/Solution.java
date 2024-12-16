import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashSet;
import java.util.Set;


record Sensor(int x, int y, int range) {
    public Set<Integer> getExclusions(int yRow) {
        Set<Integer> excluded = new HashSet<>();
        int rem = range - Math.abs(y - yRow);
        for (int i = x-rem; i <= x+rem; i++) {
            excluded.add(i);
        }
        return excluded;
    }

    @Override
    public String toString() {
        return String.format("%d,%d", x, y);
    }
}

record Coords(int x, int y) {
    @Override
    public String toString() {
        return String.format("%d,%d", x, y);
    }
}

/**
 * Start inclusive, end inclusive
 */
class Range implements Comparable<Range> {
    int start;
    int end;

    public Range(int start, int end) {
        this.start = start;
        this.end = end;
    }

    public boolean overlaps(Range r) {
        return (r.start <= start && r.end >= start) || (r.end >= end && r.start <= end);
    }

    public void insert(Range r) {
        if (r.end >= start) {
            start = r.start;
        }

        if (r.start <= end) {
            end = r.end;
        }
    }

    @Override
    public int compareTo(Range r) {
        return start != r.start ? this.start - r.start : this.end - r.end;
    }
}

public class Solution {

    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("Please provide a file path");
            return;
        }

        Set<Coords> beacons = new HashSet<>();
        Set<Sensor> sensors = new HashSet<>();

        try (BufferedReader reader = new BufferedReader(new FileReader(args[0]))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String s = line.substring(
                    line.indexOf("x"),
                    line.indexOf(":")
                );
                String b = line.substring(
                    line.lastIndexOf("x")
                );
                Coords beacon = createBeacon(b);
                beacons.add(beacon);
                sensors.add(createSensor(s, beacon));
            }

        } catch (IOException e) {
            System.err.println(e.getMessage());
        }

        System.out.println("Part 1 test (y=10): " + excludedCount(sensors, beacons, 10));
        System.out.println("Part 1 input (y=2,000,000): " + excludedCount(sensors, beacons, 2_000_000));
        Coords c = locateBeacon(sensors, beacons, 4_000_000);
        System.out.println("Part 2 input: " +  (c.x() * 4_000_000 + c.y()));
    }

    static Sensor createSensor(String s, Coords b) {
        String[] sToks = s.split(", ");
        int sX = Integer.parseInt(sToks[0].substring(2));
        int sY = Integer.parseInt(sToks[1].substring(2));
        return new Sensor (sX, sY, Math.abs(sX - b.x()) + Math.abs(sY - b.y()));
    }

    static Coords createBeacon(String b) {
        String[] toks = b.split(", ");
        return new Coords(
            Integer.parseInt(toks[0].substring(2)),
            Integer.parseInt(toks[1].substring(2))
        );
    }

    /*
     * Part 1: Get number of excluded beacon positions for a given y coordinate
     */
    static int excludedCount(Set<Sensor> sensors, Set<Coords> beacons, int y) {
        Set<Integer> excludedX = new HashSet<>();

        sensors.stream()
            .filter(s -> s.y() - s.range() <= y && s.y() + s.range() >= y)
            .forEach(s -> excludedX.addAll(s.getExclusions(y)));

        int beaconCnt = (int) beacons.stream().filter(b -> b.y() == y).count();

        return excludedX.size() - beaconCnt;
    }

    /*
     * Part 2: Locate distress beacon
     */
    static Coords locateBeacon(Set<Sensor> sensors, Set<Coords> beacons, int limit) {
        for (int y = 0; y < limit; y++) {

            // Filter sensors include y

            // Iterate over sensors to create sorted list of ranges

            // Check if output range is in [0, limit]

            // Return otherwise

        }

        return new Coords(0, 0);
    }
}
