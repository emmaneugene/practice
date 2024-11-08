import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

class Tree {
    int lView = 0;
    int rView = 0;
    int tView = 0;
    int bView = 0;

    int getScore() {
        return lView * rView * tView * bView;
    }
}

public class Solution {

    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("Please provide a file path");
            return;
        }

        List<List<Integer>> grid = new ArrayList<>();

        try (BufferedReader reader = new BufferedReader(new FileReader(args[0]))) {
            String line;
            while ((line = reader.readLine()) != null) {
                List<Integer> row = new ArrayList<>();
                for (char c : line.toCharArray()) {
                    row.add(c - '0');
                }
                grid.add(row);
            }

        } catch (IOException e) {
            System.err.println(e.getMessage());
        }

        System.out.println("Part 1: " + solution1(grid));
        System.out.println("Part 2: " + solution2(grid));
    }

    private static String coords(int row, int col) {
        return String.join(",", String.valueOf(row), String.valueOf(col));
    }

    private static int solution1(List<List<Integer>> grid) {
        Set<String> visible = new HashSet<>();

        int rowCnt = grid.size();
        int colCnt = grid.get(0).size();

        for (int row = 0; row < rowCnt; row++) {
            // Left
            visible.add(coords(row, 0));
            int tallestL = grid.get(row).get(0);

            for (int col = 1; col < colCnt; col++) {
                if (grid.get(row).get(col) > tallestL) {
                    visible.add(coords(row, col));
                    tallestL = grid.get(row).get(col);
                }
            }
            // Right
            visible.add(coords(row, colCnt - 1));
            int tallestR = grid.get(row).get(colCnt - 1);

            for (int col = colCnt - 2; col >= 0; col--) {
                if (grid.get(row).get(col) > tallestR) {
                    visible.add(coords(row, col));
                    tallestR = grid.get(row).get(col);
                }
            }
        }

        for (int col = 0; col < colCnt; col++) {
            // Top
            visible.add(coords(0, col));
            int tallestT = grid.get(0).get(col);

            for (int row = 1; row < rowCnt; row++) {
                if (grid.get(row).get(col) > tallestT) {
                    visible.add(coords(row, col));
                    tallestT = grid.get(row).get(col);
                }
            }
            // Bottom
            visible.add(coords(rowCnt - 1, col));
            int tallestB = grid.get(rowCnt - 1).get(col);

            for (int row = rowCnt - 2; row >= 0; row--) {
                if (grid.get(row).get(col) > tallestB) {
                    visible.add(coords(row, col));
                    tallestB = grid.get(row).get(col);
                }
            }
        }
        return visible.size();
    }

    private static int solution2(List<List<Integer>> grid) {
        Map<String, Tree> trees = new HashMap<>();
        int rowCnt = grid.size();
        int colCnt = grid.get(0).size();

        for (int row = 0; row < rowCnt; row++) {
            for (int col = 0; col < colCnt; col++) {
                trees.put(coords(row, col), new Tree());
            }
        }

        for (int row = 0; row < rowCnt; row++) {
            // Left views
            for (int col = 0; col < colCnt; col++) {
                trees.get(coords(row, col)).lView = getLView(grid, row, col);
            }
            // Right views
            for (int col = colCnt - 1; col >= 0; col--) {
                trees.get(coords(row, col)).rView = getRView(grid, row, col);
            }
        }

        for (int col = 0; col < colCnt; col++) {
            // Top views
            for (int row = 0; row < rowCnt; row++) {
                trees.get(coords(row, col)).tView = getTView(grid, row, col);
            }
            // Bottom views
            for (int row = rowCnt - 1; row >= 0; row--) {
                trees.get(coords(row, col)).bView = getBView(grid, row, col);
            }
        }

        return trees.values()
                .stream()
                .map(Tree::getScore)
                .reduce(0, Integer::max);
    }

    private static int getLView(List<List<Integer>> grid, int row, int col) {
        if (col == 0)
            return 0;

        int curr = grid.get(row).get(col);
        int view = 1;
        while (grid.get(row).get(col - view) < curr && col - view > 0) {
            view++;
        }

        return view;
    }

    private static int getRView(List<List<Integer>> grid, int row, int col) {
        int colCnt = grid.get(0).size();
        if (col == colCnt - 1)
            return 0;

        int curr = grid.get(row).get(col);
        int view = 1;
        while (grid.get(row).get(col + view) < curr && col + view < colCnt - 1) {
            view++;
        }

        return view;
    }

    private static int getTView(List<List<Integer>> grid, int row, int col) {
        if (row == 0)
            return 0;

        int curr = grid.get(row).get(col);
        int view = 1;
        while (grid.get(row - view).get(col) < curr && row - view > 0) {
            view++;
        }

        return view;
    }

    private static int getBView(List<List<Integer>> grid, int row, int col) {
        int rowCnt = grid.size();
        if (row == rowCnt - 1)
            return 0;

        int curr = grid.get(row).get(col);
        int view = 1;
        while (grid.get(row + view).get(col) < curr && row + view < rowCnt - 1) {
            view++;
        }

        return view;
    }
}
