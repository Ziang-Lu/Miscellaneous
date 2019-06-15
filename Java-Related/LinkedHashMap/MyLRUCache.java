import java.util.HashMap;
import java.util.Map;

/**
 * My LRU Cache.
 * The idea is decorate a HashMap with a doubly linked-list to keep track of the
 * access-order of the items.
 *
 * @param <K> key type
 * @param <V> value type
 * @author Ziang Lu
 */
public class MyLRUCache<K, V> {

    /**
     * Inner ItemNode class.
     */
    private class ItemNode {
        /**
         * Key of the item.
         */
        private final K key;
        /**
         * Value of the item.
         */
        private V val;
        /**
         * Previous item.
         */
        private ItemNode prev;
        /**
         * Next item.
         */
        private ItemNode next;

        /**
         * Constructor with parameter.
         * @param key key of the item
         * @param val value of the item
         */
        ItemNode(K key, V val) {
            this.key = key;
            this.val = val;
            prev = null;
            next = null;
        }
    }

    /**
     * Map of the items.
     */
    private final Map<K, ItemNode> map;
    /**
     * Head of the doubly linked-list, which represents the least recently used
     * item.
     */
    private ItemNode head;
    /**
     * End of the doubly linked-list, which represents the most recently used
     * item.
     */
    private ItemNode end;
    /**
     * Cache size.
     */
    private final int cacheSize;

    /**
     * Constructor with parameter.
     * @param cacheSize cache size
     */
    public MyLRUCache(int cacheSize) {
        map = new HashMap<>();
        head = null;
        end = null;
        this.cacheSize = cacheSize;
    }

    /**
     * Gets the value for the given key.
     * @param key key to check
     * @return value for the key if found, null if not found
     */
    public V get(K key) {
        if (!map.containsKey(key)) {
            return null;
        }
        ItemNode node = map.get(key);
        // Note that since we need to keep access-order, we need to move the accessed node to the end
        moveNodeToEnd(node);
        return node.val;
    }

    /**
     * Private helper method to move the given node to the end of the doubly
     * linked-list.
     * @param node node to move
     */
    private void moveNodeToEnd(ItemNode node) {
        if (node == end) { // No need to move
            return;
        }
        if (node == head) { // Simply remove and reset the head
            ItemNode headNext = head.next;
            head.next = null;
            headNext.prev = null;
            head = headNext;
        } else { // Remove the given node by reconnecting the previous and next nodes
            node.prev.next = node.next;
            node.prev = null;
            node.next.prev = node.prev;
            node.next = null;
        }
        addNodeToEnd(node);
    }

    /**
     * Helper method to add the given node to the end of the doubly linked-list.
     * @param node node to add
     */
    private void addNodeToEnd(ItemNode node) {
        if ((head == null) && (end == null)) {
            head = node;
            end = node;
            return;
        }
        // Add the given node and reset the end
        end.next = node;
        node.prev = end;
        end = node;
    }

    /**
     * Puts the given mapping for the given key and value.
     * @param key key to put
     * @param val value to put
     */
    public void put(K key, V val) {
        if (map.containsKey(key)) {
            ItemNode node = map.get(key);
            node.val = val;
            // Note that since we need to keep access-order, we need to move the accessed node to the end
            moveNodeToEnd(node);
        } else {
            if (map.size() >= cacheSize) { // Reach cache limit
                // Remove the least recently used item (head)
                map.remove(head.key);
                ItemNode headNext = head.next;
                head.next = null;
                if (headNext != null) {
                    headNext.prev = null;
                }
                head = headNext;
            }
            // Add the new node
            ItemNode newNode = new ItemNode(key, val);
            map.put(key, newNode);
            addNodeToEnd(newNode);
        }
    }

}
