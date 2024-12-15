import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashSet;
import java.util.Set;

class Grid {

    Set<String> occupied = new HashSet<>();
    int xMin = 500;
    int xMax = 500;
    int yMax = 0;
    int p1Cnt = 0;
    int p2Cnt = 0;

    public void traceRocks(String s) {
        String[] toks = s.split("\\s*->\\s*");

        int xSrc = 0;
        int ySrc = 0;
        int xDst = 0;
        int yDst = 0;

        for (int i = 0; i + 1 < toks.length; i++) {
            String[] srcCoords = toks[i].split(",");
            String[] dstCoords = toks[i+1].split(",");
            xSrc = Integer.parseInt(srcCoords[0]);
            ySrc = Integer.parseInt(srcCoords[1]);
            xDst = Integer.parseInt(dstCoords[0]);
            yDst = Integer.parseInt(dstCoords[1]);

            xMin = Math.min(xMin, Math.min(xSrc, xDst));
            xMax = Math.max(xMax, Math.max(xSrc, xDst));
            yMax = Math.max(yMax, Math.max(ySrc, yDst));

            for (int y = Math.min(ySrc, yDst); y <= Math.max(ySrc, yDst); y++) {
                occupied.add(toCoords(xSrc, y));
            }

            for (int x = Math.min(xSrc, xDst); x <= Math.max(xSrc, xDst); x++) {
                occupied.add(toCoords(x, ySrc));
            }
        }
    }

    public void simulate1() {
        Set<String> occupiedCpy = new HashSet<>(occupied);
        int xPos = 500;
        int yPos = 0;

        while (true) {
            if (!occupiedCpy.contains(toCoords(xPos, yPos+1))) {
                yPos++;
            } else if (!occupiedCpy.contains(toCoords(xPos-1, yPos+1))) {
                xPos--;
                yPos++;
                if (xPos < xMin) break;
            } else if (!occupiedCpy.contains(toCoords(xPos+1, yPos+1))) {
                xPos++;
                yPos++;
                if (xPos > xMax) break;
            } else {
                occupiedCpy.add(toCoords(xPos, yPos));
                xPos = 500;
                yPos = 0;
                p1Cnt++;
            }
        }
    }

    public void simulate2() {
        Set<String> occupiedCpy = new HashSet<>(occupied);
        int floor = yMax + 2;
        int xPos = 500;
        int yPos = 0;

        while (true) {
            if (yPos+1 < floor) {
                if (!occupiedCpy.contains(toCoords(xPos, yPos+1))) {
                    yPos++;
                } else if (!occupiedCpy.contains(toCoords(xPos-1, yPos+1))) {
                    xPos--;
                    yPos++;
                } else if (!occupiedCpy.contains(toCoords(xPos+1, yPos+1))) {
                    xPos++;
                    yPos++;
                } else {
                    if (occupiedCpy.contains(toCoords(xPos, yPos))) break;
                    occupiedCpy.add(toCoords(xPos, yPos));
                    p2Cnt++;
                    xPos = 500;
                    yPos = 0;
                }
            } else {
                if (occupiedCpy.contains(toCoords(xPos, yPos))) break;
                occupiedCpy.add(toCoords(xPos, yPos));
                p2Cnt++;
                xPos = 500;
                yPos = 0;
            }
        }
    }

    public static String toCoords(int x, int y) {
        return String.format("%d,%d", x, y);
    }
}

public class Solution {

    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("Please provide a file path");
            return;
        }

        Grid g = new Grid();

        try (BufferedReader reader = new BufferedReader(new FileReader(args[0]))) {
            String line;
            while ((line = reader.readLine()) != null) {
                g.traceRocks(line);
            }
        } catch (IOException e) {
            System.err.println(e.getMessage());
        }

        g.simulate1();
        System.out.println("Part 1: " + g.p1Cnt);
        g.simulate2();
        System.out.println("Part 2: " + g.p2Cnt);
    }
}
