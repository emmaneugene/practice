import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;
import java.util.stream.Collectors;

/**
 * For part 2, use modulo logic to keep values from exploding. The modulo value should be divisible
 * by all test divisors
 */
record Pass(int target, long value) {}

class Monkey {

    List<Long> items;
    String op;
    long testDiv;
    int passTrue;
    int passFalse;
    long inspectCnt = 0;

    public Monkey(List<Long> items, String op, long testDiv, int passTrue, int passFalse) {
        this.items = items;
        this.op = op;
        this.testDiv = testDiv;
        this.passTrue = passTrue;
        this.passFalse = passFalse;
    }

    public long inspect(long item) {
        inspectCnt++;
        String[] toks = op.split(" ");
        String operator = toks[0];
        long operand = toks[1].equals("old") ? item : Long.valueOf(toks[1]);

        switch (operator) {
            case "+":
                return item + operand;
            case "*":
                return item * operand;
        }

        return item;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Monkey with items " + items);
        sb.append("\nOp: {" + op + "}");
        sb.append("\nDivide by " + testDiv);
        sb.append("\nThow to monkey " + passTrue + " if divisible, else " + passFalse);
        return sb.toString();
    }
}

public class Solution {

    public static void main(String[] args) throws IOException {
        if (args.length < 1) {
            System.out.println("Please provide a file path");
            return;
        }

        List<Monkey> monkeys1 = new ArrayList<>();
        List<Monkey> monkeys2 = new ArrayList<>();

        List<String> lines = Files.readAllLines(Path.of(args[0]));
        Iterator<String> iter = lines.iterator();
        String line;
        while (iter.hasNext()) {
            line = iter.next();
            if (line.startsWith("Monkey")) {
                String[] itemStrs =
                        iter.next().strip().substring("Starting items: ".length()).split(", ");
                List<Long> items =
                        Arrays.stream(itemStrs)
                                .map(x -> Long.valueOf(x))
                                .collect(Collectors.toList());
                line = iter.next().strip();
                String op = line.substring(line.lastIndexOf(" ") - 1);
                line = iter.next();
                long testDiv = Long.valueOf(line.substring(line.lastIndexOf(" ") + 1));
                line = iter.next().strip();
                int passTrue = Integer.valueOf(line.substring(line.lastIndexOf(" ") + 1));
                line = iter.next().strip();
                int passFalse = Integer.valueOf(line.substring(line.lastIndexOf(" ") + 1));

                monkeys1.add(new Monkey(items, op, testDiv, passTrue, passFalse));
                monkeys2.add(new Monkey(new ArrayList<>(items), op, testDiv, passTrue, passFalse));
            }
        }

        // Part 1: Play 20 rounds, divide worry level by 3
        for (int i = 0; i < 20; i++) {
            for (Monkey m : monkeys1) {
                List<Pass> passes = new ArrayList<>();

                for (long it : m.items) {
                    long val = m.inspect(it) / 3;
                    int targ = val % m.testDiv == 0 ? m.passTrue : m.passFalse;
                    passes.add(new Pass(targ, val));
                }

                for (Pass p : passes) {
                    monkeys1.get(p.target()).items.add(p.value());
                }

                m.items.clear();
            }
        }

        List<Long> inspectCnts =
                monkeys1.stream().map(m -> m.inspectCnt).sorted().collect(Collectors.toList());
        long p1 = inspectCnts.removeLast() * inspectCnts.removeLast();

        // Part 2: Play 10,000 rounds, modulo worry level to keep it reasonable
        long bigModulo = 1;
        for (Monkey m : monkeys2) {
            if (bigModulo % m.testDiv != 0) {
                bigModulo *= m.testDiv / hcf(bigModulo, m.testDiv);
            }
        }

        for (int i = 0; i < 10000; i++) {
            for (Monkey m : monkeys2) {
                List<Pass> passes = new ArrayList<>();

                for (long it : m.items) {
                    long val = m.inspect(it) % bigModulo;
                    int targ = val % m.testDiv == 0 ? m.passTrue : m.passFalse;
                    passes.add(new Pass(targ, val));
                }

                for (Pass p : passes) {
                    monkeys2.get(p.target()).items.add(p.value());
                }

                m.items.clear();
            }
        }

        List<Long> inspectCnts2 =
                monkeys2.stream().map(m -> m.inspectCnt).sorted().collect(Collectors.toList());
        long p2 = inspectCnts2.removeLast() * inspectCnts2.removeLast();

        System.out.println("Part 1: " + p1);
        System.out.println("Part 2: " + p2);
    }

    // Euclidean algo for finding highest common factor
    public static long hcf(long a, long b) {
        a = Math.abs(a);
        b = Math.abs(b);

        if (a == 0) return b;
        if (b == 0) return a;

        while (b != 0) {
            long tmp = b;
            b = a % b;
            a = tmp;
        }

        return a;
    }
}
