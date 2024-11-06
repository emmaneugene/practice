import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

abstract class Node {
    String name;

    abstract int getSize();
}

class Directory extends Node {
    Node parent = null;
    Map<String, Node> children = new HashMap<>();

    Directory(String name) {
        this.name = name;
    }

    void addChild(Node n) {
        if (n instanceof Directory) {
            Directory d = (Directory) n;
            d.parent = this;
        }

        children.put(n.name, n);
    }

    int getSize() {
        return children.values()
                .stream()
                .mapToInt(Node::getSize)
                .sum();
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(String.format("- %s (dir)\n", name));

        for (Node n : children.values()) {
            if (n instanceof Directory) {
                String[] lines = n.toString().split("\\n");
                for (String l: lines) {
                    sb.append("  " + l + "\n");
                }
            }
            else {
                sb.append("  " + n);
            }
        }
        return sb.toString();
    }
}

class File extends Node {
    int size;

    File(String name, int size) {
        this.name = name;
        this.size = size;
    }

    int getSize() {
        return size;
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

        String line;

        try (BufferedReader reader = new BufferedReader(new FileReader(args[0]))) {
            while ((line = reader.readLine()) != null) {

            }
        } catch (IOException e) {
            System.err.println(e.getMessage());
        }
    }

    public static void test() {
        System.out.println("Creating empty root node");
        Directory root = new Directory("/");
        System.out.println("Size of empty node: " + root.getSize());

        root.addChild(new File("File1", 123));
        System.out.println("Size of node with 1 file: " + root.getSize());

        Directory d = new Directory("Dir1");
        d.addChild(new File("Test1", 1000));
        root.addChild(d);
        System.out.println("Size of node with 1 file and 1 directory: " + root.getSize());

        System.out.println(root);
        System.out.println();
        System.out.println(d.parent);
    }
}
