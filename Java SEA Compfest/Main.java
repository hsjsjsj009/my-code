import java.util.*;

public class Main {
    static int bitmask;
    static ArrayList<Character> characters;
    static ArrayList<Character> running;

    static void permutations() {
        int i;
        if (running.size() == characters.size()) {
            StringBuilder s = new StringBuilder();
            for (char c : running) {
                s.append(c);
            }
            System.out.printf("%s\n", s.toString());
        } else {
            for(i=0; i<characters.size(); i++) {
                if ( ((bitmask>>i)&1) == 0 ) {
                    bitmask |= (1<<i);
                    running.add(characters.get(i));
                    permutations();
                    running.remove(running.size()-1);
                    bitmask ^= (1<<i);
                }
            }
        }
    }

    public static void main(String[] args) {
        int i;
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        characters = new ArrayList<Character>();
        for (i=0; i<s.length(); i++) {
            characters.add(s.charAt(i));
        }
        running = new ArrayList<Character>();
        bitmask = 0;
        permutations();

    }
}