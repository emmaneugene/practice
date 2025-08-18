import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

record Sensor(int x, int y, int range) {
    public Set<Integer> getExclusions(int yRow) {
        Set<Integer> excluded = new HashSet<>();
        int rem = range - Math.abs(y - yRow);
        for (int i = x - rem; i <= x + rem; i++) {
            excluded.add(i);
        }
        return excluded;
    }

    public boolean overlapsY(int y) {
        return y >= (this.y - range) && y <= (this.y + range);
    }

    public Range getXRange(int y) {
        int displace = range - Math.abs(this.y - y);
        return new Range(x - displace, x + displace);
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

/** Start inclusive, end inclusive */
class Range implements Comparable<Range> {

    int start;
    int end;

    public Range(int start, int end) {
        this.start = start;
        this.end = end;
    }

    public boolean canMerge(Range r) {
        return (r.start <= end && r.end >= start - 1) || (r.end >= start && r.start <= end + 1);
    }

    public void merge(Range r) {
        start = Math.min(start, r.start);
        end = Math.max(end, r.end);
    }

    @Override
    public int compareTo(Range r) {
        return start != r.start ? start - r.start : r.end - end;
    }

    @Override
    public String toString() {
        return String.format("[%d,%d]", start, end);
    }
}

public class Solution {

    public static void main(String[] args) throws IOException {
        if (args.length < 1) {
            System.out.println("Please provide a file path");
            return;
        }

        Set<Coords> beacons = new HashSet<>();
        Set<Sensor> sensors = new HashSet<>();

        List<String> lines = Files.readAllLines(Path.of(args[0]));
        for (String line : lines) {
            String s = line.substring(line.indexOf("x"), line.indexOf(":"));
            String b = line.substring(line.lastIndexOf("x"));
            Coords beacon = createBeacon(b);
            beacons.add(beacon);
            sensors.add(createSensor(s, beacon));
        }

        System.out.println("Part 1 exclusion count (test): " + getExclusions(sensors, beacons, 10));
        System.out.println(
                "Part 1 exclusion count (input): " + getExclusions(sensors, beacons, 2_000_000));

        System.out.println("Part 2 beacon position (test): " + locateBeacon(sensors, beacons, 20));
        System.out.println(
                "Part 2 beacon position (input): " + locateBeacon(sensors, beacons, 4_000_000));
    }

    static Sensor createSensor(String s, Coords b) {
        String[] toks = s.split(", ");
        int sX = Integer.parseInt(toks[0].substring(2));
        int sY = Integer.parseInt(toks[1].substring(2));
        return new Sensor(sX, sY, Math.abs(sX - b.x()) + Math.abs(sY - b.y()));
    }

    static Coords createBeacon(String b) {
        String[] toks = b.split(", ");
        return new Coords(
                Integer.parseInt(toks[0].substring(2)), Integer.parseInt(toks[1].substring(2)));
    }

    /*
     * Part 1: Get number of excluded beacon positions for a given y coordinate
     */
    static int getExclusions(Set<Sensor> sensors, Set<Coords> beacons, int y) {
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
            final int yTmp = y;
            // Filter sensors activated for this y value
            Set<Sensor> activated =
                    sensors.stream().filter(s -> s.overlapsY(yTmp)).collect(Collectors.toSet());

            // Iterate over sensors to create sorted list of x ranges
            List<Range> ranges = activated.stream().map(s -> s.getXRange(yTmp)).sorted().toList();
            // Merge overlapping
            Range curr = ranges.get(0);
            for (Range r : ranges.subList(1, ranges.size())) {
                if (curr.canMerge(r)) {
                    curr.merge(r);
                } else {
                    return new Coords(curr.end + 1, y);
                }
            }
        }

        return new Coords(-1, -1);
    }
}
