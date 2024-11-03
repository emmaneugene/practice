import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("Please provide a file path");
            return;
        }

        String line;
        StringBuilder msg1 = new StringBuilder();
        StringBuilder msg2 = new StringBuilder();

        try (BufferedReader reader = new BufferedReader(new FileReader(args[0]))) {
            // Process stacks
            List<String> stacksStr = new ArrayList<>();
            while ((line = reader.readLine()).length() != 0) {
                stacksStr.add(line);
            }

            List<List<Character>> stacks1 = new ArrayList<>();
            int stackCount = stacksStr.removeLast().strip().split("\\s+").length;
            for (int i = 0; i < stackCount; i++) {
                stacks1.add(new ArrayList<>());
            }

            for (int i = stacksStr.size() - 1; i >= 0; i--) {
                for (int j = 0; j < stackCount; j++) {
                    try {
                        char c = stacksStr.get(i).charAt(getCrateIdx(j));
                        if (c != ' ') {
                            stacks1.get(j).add(c);
                        }
                    } catch (StringIndexOutOfBoundsException e) {
                        break;
                    }
                }
            }

            List<List<Character>> stacks2 = new ArrayList<>();
            for (List<Character> l : stacks1) {
                stacks2.add(new ArrayList<>(l));
            }

            // Process instructions
            while ((line = reader.readLine()) != null) {
                processInstr1(line, stacks1);
                processInstr2(line, stacks2);
            }
            for (int i = 0; i < stackCount; i++) {
                msg1.append(stacks1.get(i).getLast());
                msg2.append(stacks2.get(i).getLast());
            }

            System.out.println(msg1);
            System.out.println(msg2);
        } catch (IOException e) {
            System.err.println(e.getMessage());
        }
    }

    private static int getCrateIdx(int n) {
        return 1 + (n) * 4;
    }

    private static void processInstr1(String instr, List<List<Character>> stacks) {
        String[] toks = instr.split("\\s+");
        int moveCount = Integer.parseInt(toks[1]);
        int src = Integer.parseInt(toks[3]);
        int dst = Integer.parseInt(toks[5]);

        for (int i = 0; i < moveCount; i++) {
            stacks.get(dst - 1).add(stacks.get(src - 1).removeLast());
        }
    }

    private static void processInstr2(String instr, List<List<Character>> stacks) {
        String[] toks = instr.split("\\s+");
        int moveCount = Integer.parseInt(toks[1]);
        int src = Integer.parseInt(toks[3]);
        int dst = Integer.parseInt(toks[5]);

        List<Character> srcStack = stacks.get(src - 1);
        List<Character> dstStack = stacks.get(dst - 1);
        List<Character> subl = srcStack.subList(srcStack.size() - moveCount, srcStack.size());

        subl.forEach(c -> dstStack.add(c));
        subl.clear();
    }
}
