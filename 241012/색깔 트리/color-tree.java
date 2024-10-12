import java.util.*;

public class Main {
    private static Map<Integer, Node> map;
    private static Set<Integer> leaves;

    public static void main(String[] args) {
        map = new HashMap<>();
        leaves = new HashSet<>();

        Scanner scanner = new Scanner(System.in);
        int Q = Integer.parseInt(scanner.nextLine());

        for (int i = 0; i < Q; i++) {
            String[] instruction = scanner.nextLine().split(" ");
            int ins = Integer.parseInt(instruction[0]);

            if (ins == 100) {
                int m_id = Integer.parseInt(instruction[1]);
                int p_id = Integer.parseInt(instruction[2]);
                int color = Integer.parseInt(instruction[3]);
                int max_depth = Integer.parseInt(instruction[4]);

                if (p_id == -1) {
                    Node node = new Node(m_id, color, max_depth, null);
                    map.put(m_id, node);
                    leaves.add(m_id);
                } else {
                    Node parent = map.get(p_id);
                    Node node = new Node(m_id, color, max_depth, parent);

                    if (checkNode(node, 1)) {
                        map.put(m_id, node);
                        Node.addChild(parent, m_id);
                        leaves.add(m_id);
                        leaves.remove(p_id);
                    }
                }
            }

            if (ins == 200) {
                int m_id = Integer.parseInt(instruction[1]);
                int color = Integer.parseInt(instruction[2]);

                changeColor(map.get(m_id), color);
            }

            if (ins == 300) {
                int m_id = Integer.parseInt(instruction[1]);
                System.out.println(map.get(m_id).color);
            }

            if (ins == 400) {
                for (int k : map.keySet()) {
                    Node node = map.get(k);
                    node.colors = new boolean[5];
                }

                for (int k : leaves) {
                    settingValue(map.get(k), new boolean[5]);
                }
                long answer = 0L;
                for (int k : map.keySet()) {
                    Node node = map.get(k);
                    int v = countValue(node);
                    answer += (long) (v * v);
                }
                System.out.println(answer);
            }
        }

        // for (int k : map.keySet()) {
        //     System.out.println(k);
        // }
    }

    static class Node {
        final int m_id;
        int color;
        final int max_depth;
        int current_depth;
        Node p_node;
        List<Integer> c_nodes;
        boolean[] colors;

        public Node(int m_id, int color, int max_depth, Node p_node) {
            this.m_id = m_id;
            this.color = color;
            this.max_depth = max_depth;
            this.p_node = p_node;
            this.c_nodes = new ArrayList<>();
        }

        public static void addChild(Node node, int c_id) {
            node.c_nodes.add(c_id);
        }
    }

    private static boolean checkNode(Node node, int depth) {
        if (depth > node.max_depth) return false;
        if (node.p_node == null) return true;

        return checkNode(node.p_node, depth + 1);
    }

    private static void changeColor(Node node, int color) {
        node.color = color;

        if (node.c_nodes.isEmpty()) return;

        for (int c_id : node.c_nodes) {
            changeColor(map.get(c_id), color);
        }
    }


    private static void settingValue(Node node, boolean[] subColors) {
        boolean[] myColors = node.colors;
        myColors[node.color - 1] = true;
        for (int i = 0; i < 5; i++) {
            myColors[i] = myColors[i] || subColors[i];
        }

        if (node.p_node == null) return;

        settingValue(node.p_node, myColors);
    }

    private static int countValue(Node node) {
        int n = 0;
        boolean[] colors = node.colors;
        for (int i = 0; i < 5; i++) {
            if (colors[i]) n++;
        }
        return n;
    }
}