import java.util.LinkedHashMap;
import java.util.Map;

/**
 * LinkedHashMap with access-order to model an LRU cache.
 *
 * @author Ziang Lu
 */
public class LRUCache<K, V> extends LinkedHashMap<K, V> {
    /**
     * Cache size.
     */
    private int cacheSize;

    /**
     * Constructor with parameter.
     * @param cacheSize cache size
     */
    public LRUCache(int cacheSize) {
        // Note that we need to use access-order
        super(16, 0.75, true);
        this.cacheSize = cacheSize;
    }

    @Override
    public boolean removeEldestEntry(Map.Entry<K, V> entry) {
        return this.size() > cacheSize;
    }
}

