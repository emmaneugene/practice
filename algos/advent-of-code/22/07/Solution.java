import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.OptionalInt;

abstract class Node {

    String name;
    int size;
}

class Directory extends Node {

    Directory parent = null;
    Map<String, Node> children = new HashMap<>();

    Directory(String name) {
        this.name = name;
        this.size = 0;
    }

    void addChild(Node n) {
        if (n instanceof Directory) {
            Directory d = (Directory) n;
            d.parent = this;
        }

        children.put(n.name, n);
        updateSize(n.size);
    }

    void deleteChild(String nodeName) {
        Node toDelete = children.get(nodeName);
        children.remove(nodeName);
        updateSize(-toDelete.size);
    }

    void updateSize(int size) {
        this.size += size;
        if (parent != null) {
            parent.updateSize(size);
        }
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(String.format("- %s (dir)\n", name));

        for (Node n : children.values()) {
            if (n instanceof Directory) {
                String[] lines = n.toString().split("\\n");
                for (String l : lines) {
                    sb.append("  " + l + "\n");
                }
            } else {
                sb.append("  " + n);
            }
        }
        return sb.toString();
    }
}

class File extends Node {

    File(String name, int size) {
        this.name = name;
        this.size = size;
    }

    public String toString() {
        return String.format("- %s (file, size=%d)\n", name, size);
    }
}

public class Solution {

    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("Running test case:");
            test();
            System.out.println("Please provide a file path");
            return;
        }

        try (BufferedReader reader = new BufferedReader(new FileReader(args[0]))) {
            String line;
            Directory root = new Directory("/");
            Directory currDir = root;

            // Remove first command
            reader.readLine();

            while ((line = reader.readLine()) != null) {
                if (line.startsWith("$ ")) {
                    // Process command
                    String cmd = line.substring("$ ".length());
                    if (cmd.startsWith("cd ")) {
                        String dirName = cmd.split(" ")[1];
                        if (dirName.equals("..")) {
                            currDir = currDir.parent;
                        } else {
                            currDir = (Directory) currDir.children.get(dirName);
                        }
                    }
                } else {
                    // Process `ls` output
                    String[] tokens = line.split(" ");
                    if (tokens[0].equals("dir")) {
                        currDir.addChild(new Directory(tokens[1]));
                    } else {
                        currDir.addChild(new File(tokens[1], Integer.parseInt(tokens[0])));
                    }
                }
            }

            System.out.println("Final directory tree:");
            System.out.println(root);

            System.out.println("Part 1: " + solution1(root));
            System.out.println("Part 2: " + solution2(root));
        } catch (IOException e) {
            System.err.println(e.getMessage());
        }
    }

    private static int solution1(Directory d) {
        int result = 0;

        if (d.size <= 100_000) {
            result += d.size;
        }

        result += d.children.values()
                .stream()
                .filter(obj -> obj instanceof Directory)
                .mapToInt(x -> solution1((Directory) x))
                .sum();

        return result;
    }

    private static int solution2(Directory d) {
        int minToFree = d.size - 40_000_000;

        if (minToFree < 0) {
            return -1;
        }

        return getSmallest(minToFree, d, d.size);
    }

    private static int getSmallest(int min, Directory d, int curr) {
        if (d.size >= min && d.size < curr) {
            curr = d.size;
        }
        OptionalInt smallestChild = d.children.values()
                .stream()
                .filter(obj -> obj instanceof Directory)
                .mapToInt(x -> getSmallest(min, (Directory) x, d.size))
                .min();

        if (smallestChild.isPresent() && smallestChild.getAsInt() >= min) {
            curr = smallestChild.getAsInt();
        }

        return curr;
    }

    public static void test() {
        System.out.println("Creating empty root node");
        Directory root = new Directory("/");
        System.out.println("Size of empty node: " + root.size);

        root.addChild(new File("File1", 123));
        System.out.println("Size of node with 1 file: " + root.size);

        Directory d = new Directory("Dir1");
        d.addChild(new File("Test1", 1000));
        root.addChild(d);
        System.out.println("Size of node with 1 file and 1 directory: " + root.size);

        System.out.println(root);
        System.out.println();
        System.out.println(d.parent);
    }
}
