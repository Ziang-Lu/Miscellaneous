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

    /**
     * Main driver.
     * @param args arguments from command line
     */
    public static void main(String[] args) {
        System.out.println("===== HashMap demo =====");
        Map<Integer, String> hm = new HashMap<>();
        putEntriesToMap(hm);

        System.out.println();

        System.out.println("===== LinkedHashMap demo =====");
        Map<Integer, String> lhm = new LinkedHashMap<>();
        putEntriesToMap(lhm);

        System.out.println();

        System.out.println("===== LinkedHashMap (with access-order) demo =====");
        Map<Integer, String> lhmAccessOrder = new LinkedHashMap<>(16, 0.75f, true);
        putEntriesToMap(lhmAccessOrder);

        // Output:
        // ===== HashMap demo =====
        // {1=a, 2=b, 4=d}
        // {1=a, 2=b, 4=new d}
        //
        // ===== LinkedHashMap demo =====
        // {1=a, 4=d, 2=b}
        // {1=a, 4=new d, 2=b}
        //
        // ===== LinkedHashMap (with access-order) demo =====
        // {1=a, 4=d, 2=b}
        // {1=a, 2=b, 4=new d}
    }

    /**
     * Private helper method to put entries into the given map.
     * @param map map to put entries into
     */
    private static void putEntriesToMap(Map<Integer, String> map) {
        map.put(1, "a");
        map.put(4, "d");
        map.put(2, "b");
        System.out.println(map);
        map.put(4, "new d");
        System.out.println(map);
    }
}
