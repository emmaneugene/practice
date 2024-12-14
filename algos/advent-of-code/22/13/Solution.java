import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

record Pair(List<Object> left, List<Object> right) {}

public class Solution {

    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("Please provide a file path");
            return;
        }

        List<Pair> pairs = new ArrayList<>();
        List<List<Object>> packets = new ArrayList<>();

        try (BufferedReader reader = new BufferedReader(new FileReader(args[0]))) {
            String line;
            while ((line = reader.readLine()) != null) {
                List<Object> l1 = parseValues(line);
                List<Object> l2 = parseValues(reader.readLine());
                pairs.add(new Pair(l1, l2));
                packets.add(l1);
                packets.add(l2);
                reader.readLine();
            }
        } catch (IOException e) {
            System.err.println(e.getMessage());
        }

        // Part 1
        int p1 = 0;
        for (int i = 0; i < pairs.size(); i++) {
            Pair p = pairs.get(i);
            if (comparePackets(p.left(), p.right()) < 0) {
                p1 += i+1;
            }
        }

        // Part 2
        List<Object> divider1 = List.of(List.of(2));
        List<Object> divider2 = List.of(List.of(6));
        packets.add(divider1);
        packets.add(divider2);
        packets.sort(new Comparator<Object>() {
            @Override
            public int compare(Object o1, Object o2) {
                return comparePackets(o1, o2);
            }
        });

        int divider1Idx = 0;
        int divider2Idx = 0;

        for (int i = 0; i < packets.size(); i++) {
            if (packets.get(i).hashCode() == divider1.hashCode()) {
                divider1Idx = i+1;
            }
            if (packets.get(i).hashCode() == divider2.hashCode()) {
                divider2Idx = i+1;
            }
        }

        System.out.println("Part 1: " + p1);
        System.out.println("Part 2: "+ divider1Idx * divider2Idx);
    }

    static List<Object> parseValues(String s) {
        List<Object> res = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        int scopes = 0;

        for (int i = 1; i < s.length() - 1; i++) {
            char c = s.charAt(i);

            if (c == ',' && scopes == 0) {
                String val = sb.toString();
                try {
                    res.add(Integer.parseInt(val));
                } catch (NumberFormatException e) {
                    res.add(parseValues(val));
                }
                sb.setLength(0); // Clear
                continue;
            }

            if (c == '[') scopes ++;
            else if (c == ']') scopes--;
            sb.append(c);
        }

        if (sb.length() > 0) {
            String val = sb.toString();
            try {
                res.add(Integer.parseInt(val));
            } catch (NumberFormatException e) {
                res.add(parseValues(val));
            }
        }

        return res;
    }

    @SuppressWarnings("unchecked")
    static int comparePackets(Object l, Object r) {
        if (l instanceof Integer &&  r instanceof Integer) {
            return (Integer) l - (Integer) r;
        }

        if (l instanceof Integer) l = List.of((Integer) l);
        if (r instanceof Integer) r = List.of((Integer) r);
        List<Object> lList = (List<Object>) l;
        List<Object> rList = (List<Object>) r;

        for (int i = 0; i < lList.size(); i++) {
            if (rList.size() <= i) return 1;

            int res = comparePackets(lList.get(i), rList.get(i));
            if (res != 0) return res;
        }

        return lList.size() == rList.size() ? 0 : -1;
    }
}
