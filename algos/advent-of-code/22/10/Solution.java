import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

class P1 {

    int reg = 1;
    int cycles = 0;
    int sum = 0;

    private void cycle() {
        cycles++;

        if (cycles % 40 == 20) {
            sum += cycles * reg;
        }
    }

    public void exec(String instr) {
        String[] toks = instr.split(" ");
        cycle();

        switch (toks[0]) {
            case "addx":
                cycle();
                reg += Integer.valueOf(toks[1]);
        }
    }
}

class P2 {

    int reg = 1;
    int cycles = 0;
    StringBuilder sb = new StringBuilder();

    private void cycle() {
        if (cycles % 40 >= reg - 1 && cycles % 40 <= reg + 1) {
            sb.append("#");
        } else {
            sb.append(".");
        }

        cycles++;
    }

    public void exec(String instr) {
        String[] toks = instr.split(" ");
        cycle();

        switch (toks[0]) {
            case "addx":
                cycle();
                reg += Integer.valueOf(toks[1]);
        }
    }

    public void display() {
        for (int i = 0; i < 6; i++) {
            System.out.println(sb.substring(40 * i, 40 * (i + 1)));
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
                p1.exec(line);
                p2.exec(line);
            }

            System.out.println("Part 1: " + p1.sum);
            System.out.println("Part 2:");
            p2.display();
        } catch (IOException e) {
            System.err.println(e.getMessage());
        }
    }
}
