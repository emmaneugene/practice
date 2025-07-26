import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;

public class Solution {
    public static void main(String[] args) throws IOException {
        if (args.length < 1) {
            System.out.println("Please provide a file path");
            return;
        }

        List<String> lines = Files.readAllLines(Path.of(args[0]));

        int idx = 0;
        while (lines.get(idx).length() != 0) idx++;
        List<String> stacksStr = new ArrayList<>(lines.subList(0, idx));
        List<String> instrsStr = new ArrayList<>(lines.subList(idx + 1, lines.size()));

        StringBuilder msg1 = new StringBuilder();
        StringBuilder msg2 = new StringBuilder();

        // Process stacks
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
        for (String instr : instrsStr) {
            processInstr1(instr, stacks1);
            processInstr2(instr, stacks2);
        }
        for (int i = 0; i < stackCount; i++) {
            msg1.append(stacks1.get(i).getLast());
            msg2.append(stacks2.get(i).getLast());
        }

        System.out.println(msg1);
        System.out.println(msg2);
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
