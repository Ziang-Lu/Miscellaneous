# Strong Reference (强引用)

### Explanation

```java
Object o = new Object();
```

如果一个object具有strong reference, 那么GC绝不会回收它

=> 当内存空间不足, JVM宁愿抛出OutOfMemoryError使程序异常终止, 也不会靠随意回收具有strong reference的object来解决内存不足的问题.

如希望GC回收该object, 需要显式地将其置为`null`:

```java
o = null;
```

或当超出该object的scope时

### Example

`ArrayList`源码片段:

```java
private transient Object[] elementData;

public void clear() {
    modCount++;
    // Let GC do its work
    for (int i = 0; i < size; i++) {
        elementData[i] = null;
    }
}
```

显式地将每个`Object`置为`null` => 让GC回收该`Object`

<br>

# Soft Reference (软引用)

### Explanation

```java
String s = "abc"; // strong reference
SoftReference<String> softRef = new SoftReference<>(s); // soft reference
```

如果一个object具有soft reference, 那么GC在内存足够时不会回收该object, 但在内存空间紧张时就会回收该object

```java
// 若"abc"仍然有strong reference, 则GC绝不会回收它(如上)
// 因此, 需要先显式地清除掉对"abc"的strong reference
s = null;
// 此时, "abc"仅有一个soft reference
if (JVM内存紧张) {
    System.gc(); // 由于内存紧张, GC会回收仅有一个soft refernece的"abc"
}
```

=> Soft reference最常被用来实现内存敏感的高速缓存

### Example

当点击浏览器的后退按钮时:

* 重新请求页面？

  => 耗时

* 缓存全部浏览过的页面, 此时就取出缓存的页面

  => 内存消耗巨大, 甚至可能造成内存溢出

此时就可使用soft reference实现不会内存溢出的缓存

```java
Page prev = new Page();
SoftReference<Page> softPrev = new SoftReference<>(prev);
// ...浏览下一页面
// 点击后退按钮
if (softPrev.get() != null) { // 内存还足够, 前一个页面还未被GC回收
    prev = softPrev.get() // 使用soft reference取出缓存的页面
} else { // 由于内存紧张, 前一个页面已经被GC回收
    prev = new Page(); // 重新请求页面
}
prev.render();
```

<br>

# Weak Reference (弱引用)

### Explanation

```java
String s = "abc";
WeakReference<String> weakRef = new WeakReference<>(s);
```

当GC线程扫描其所管辖的内存区域时, 一旦发现只具有weak reference的object, 则不管内存是否紧张, 都会回收该object

```java
// 若"abc"仍然有strong reference, 则GC绝不会回收它(如上)
// 因此, 需要先显式地清除掉对"abc"的strong reference
s = null;
// 此时, "abc"仅有一个weak reference
System.gc(); // 一旦GC发现该仅有一个weak reference的"abc", 不管内存是否紧张, GC都会回收它
```

=> 当想引用一个object, 又不想通过strong reference而介入该object的生命周期时, 就可以使用weak reference



