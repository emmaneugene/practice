import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Coords {
    int X = 0;
    int Y = 0;

    public String toString() {
        return String.join(",", String.valueOf(X), String.valueOf(Y));
    }
}

class P1 {

    // Let starting position be X = 0, Y = 0
    Coords head = new Coords();
    Coords tail = new Coords();
    Set<String> visited = new HashSet<>();

    void moveHead(String dir) {
        switch (dir) {
            case "U":
                head.Y -= 1;
                break;
            case "D":
                head.Y += 1;
                break;
            case "L":
                head.X -= 1;
                break;
            case "R":
                head.X += 1;
                break;
        }

        // 3 cases:
        // - Same X, diff Y -> move Y by one
        // - Same Y, diff X -> move X by one
        // - Diagonal ->  move X and Y
        if (head.X == tail.X && Math.abs(head.Y - tail.Y) > 1) {
            tail.Y += head.Y > tail.Y ? 1 : -1;
        } else if (head.Y == tail.Y && Math.abs(head.X - tail.X) > 1) {
            tail.X += head.X > tail.X ? 1 : -1;
        } else if (Math.abs(head.Y - tail.Y) > 1 || Math.abs(head.X - tail.X) > 1) {
            tail.Y += head.Y > tail.Y ? 1 : -1;
            tail.X += head.X > tail.X ? 1 : -1;
        }

        visited.add(tail.toString());
    }
}

class P2 {

    List<Coords> knots;
    Set<String> visited = new HashSet<>();

    public P2() {
        this(10);
    }

    public P2(int size) {
        knots = new ArrayList<>();
        for (int i = 0; i < size; i++) {
            knots.add(new Coords());
        }
    }

    void moveHead(String dir) {
        switch (dir) {
            case "U":
                knots.get(0).Y -= 1;
                break;
            case "D":
                knots.get(0).Y += 1;
                break;
            case "L":
                knots.get(0).X -= 1;
                break;
            case "R":
                knots.get(0).X += 1;
                break;
        }

        for (int i = 1; i < knots.size(); i++) {
            moveKnots(knots.get(i-1), knots.get(i));
        }

        visited.add(knots.getLast().toString());
    }

    private static void moveKnots(Coords front, Coords back) {
        if (front.X == back.X && Math.abs(front.Y - back.Y) > 1) {
            back.Y += front.Y > back.Y ? 1 : -1;
        } else if (front.Y == back.Y && Math.abs(front.X - back.X) > 1) {
            back.X += front.X > back.X ? 1 : -1;
        } else if (Math.abs(front.Y - back.Y) > 1 || Math.abs(front.X - back.X) > 1) {
            back.Y += front.Y > back.Y ? 1 : -1;
            back.X += front.X > back.X ? 1 : -1;
        }
    }
}

public class Solution {

    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("Please provide a file path");
            return;
        }

        try (BufferedReader reader = new BufferedReader(new FileReader(args[0]))) {

            String line;
            P1 p1 = new P1();
            P2 p2 = new P2();

            while ((line = reader.readLine()) != null) {
                String[] toks = line.split(" ");
                String dir = toks[0];
                int cnt = Integer.valueOf(toks[1]);

                for (int i = 0; i < cnt; i++) {
                    p1.moveHead(dir);
                    p2.moveHead(dir);
                }
            }

            System.out.println("Part 1: " + p1.visited.size());
            System.out.println("Part 2: " + p2.visited.size());
        } catch (IOException e) {
            System.err.println(e.getMessage());
        }
    }
}
