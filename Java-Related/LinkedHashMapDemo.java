import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map;

/**
 * LinkedHashMap demo.
 * Unlike HashMap, the insertion order is maintained: while iterating the
 * LinkedHashMap, elements are displayed in the order they were inserted.
 *
 * @author Ziang Lu
 */
public class LinkedHashMapDemo {
    public static void main(String[] args) {
        System.out.println("===== HashMap elements: =====");
        Map<Integer, String> hm = new HashMap<>();
        hm.put(1, "a");
        hm.put(4, "d");
        hm.put(2, "b");
        hm.put(4, "new d");
        System.out.println(hm);

        System.out.println();

        System.out.println("===== LinkedHashMap elements: =====");
        Map<Integer, String> lhm = new LinkedHashMap<>();
        lhm.put(1, "a");
        lhm.put(4, "d");
        lhm.put(2, "b");
        lhm.put(4, "new d");
        System.out.println(lhm);

        // Output:
        // ===== HashMap elements: =====
        // {1=a, 2=b, 4=new d}
        //
        // ===== LinkedHashMap elements: =====
        // {1=a, 4=new d, 2=b}
    }
}
