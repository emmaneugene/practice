import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Set;
import java.util.stream.Collectors;

// Dijkstra's algo
public class Solution {

    public static void main(String[] args) throws IOException {
        if (args.length < 1) {
            System.out.println("Please provide a file path");
            return;
        }

        List<List<Character>> grid = new ArrayList<>();
        Coords start = new Coords(-1, -1, 0);
        int rowIdx = 0;

        List<String> lines = Files.readAllLines(Path.of(args[0]));
        for (String line : lines) {
            grid.add(line.chars().mapToObj(ch -> (char) ch).collect(Collectors.toList()));

            if (line.contains("S")) {
                start = new Coords(rowIdx, line.indexOf('S'), 0);
            }

            rowIdx++;
        }

        System.out.println("Part 1: " + shortestPath(start, grid));

        List<Coords> coords = new LinkedList<>();

        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid.get(0).size(); j++) {
                if (grid.get(i).get(j) == 'a') {
                    coords.add(new Coords(i, j, 0));
                }
            }
        }

        int p2 =
                coords.stream()
                        .map(c -> shortestPath(c, grid))
                        .filter(i -> i > 0)
                        .min(Integer::compare)
                        .get();
        System.out.println("Part 2: " + p2);
    }

    private static int shortestPath(Coords c, List<List<Character>> grid) {
        Set<String> visited = new HashSet<>();
        Queue<Coords> toExplore = new LinkedList<>();
        visited.add(c.toString());
        toExplore.add(c);

        while (!toExplore.isEmpty()) {
            c = toExplore.remove();
            if (grid.get(c.row()).get(c.col()) == 'E') {
                return c.steps();
            }
            explore(c, visited, toExplore, grid);
        }

        return -1;
    }

    private static void explore(
            Coords curr, Set<String> visited, Queue<Coords> toExplore, List<List<Character>> grid) {
        List.of(
                        new Coords(curr.row(), curr.col() - 1, curr.steps() + 1),
                        new Coords(curr.row(), curr.col() + 1, curr.steps() + 1),
                        new Coords(curr.row() - 1, curr.col(), curr.steps() + 1),
                        new Coords(curr.row() + 1, curr.col(), curr.steps() + 1))
                .forEach(
                        c -> {
                            if (!visited.contains(c.toString())
                                    && c.row() >= 0
                                    && c.row() < grid.size()
                                    && c.col() >= 0
                                    && c.col() < grid.get(0).size()
                                    && climbable(curr, c, grid)) {
                                visited.add(c.toString());
                                toExplore.add(c);
                            }
                        });
    }

    private static boolean climbable(Coords src, Coords dst, List<List<Character>> grid) {
        Character s = grid.get(src.row()).get(src.col());
        Character d = grid.get(dst.row()).get(dst.col());

        if (s == 'S') {
            return Character.isLowerCase(d) && d <= 'b';
        } else if (d == 'E') {
            return s >= 'y';
        } else {
            return d - s <= 1;
        }
    }
}

record Coords(int row, int col, int steps) {

    @Override
    public String toString() {
        return row + "," + col;
    }
}
