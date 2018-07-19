# Class Equality Design

## Entity Types and Value Types:

* Entity Type

  Tyoes whose behavior is not strictly determined by their content.

  Some entity types are service-based types, which means that their behavior, not their state, is the most important feature.

* **Value Type**

  **Types that have content and whose behavior depeneds vitally on its content.**

The subsequent discussion of **implementing `equals()` is only relevant for value types**.

<br>

## `equals()` Contract

* Reflexivity

  An obejct must be equal to itself.

* Symmetry

  It does not make a difference whether I compare $x$ to $y$ or $y$ to $x$; the result is the same.

* Transivity

  If one object is equal to a second and the second is equal to a third, then the first and the third object must be equal, too.

* Consistency

  I can compare two objects as often as I want; the result remains the same, unless the object have been modified between subsequent comparisons.

* Comparison to `null`

  No object is equal to `null`.

<br>

## Symmetry and Transitivity Problem

Check out the following common implementation

```java
class Point2D {
    private final int x;
    private final int y;

    Point2D(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public boolean equals(Object o) {
        // Reflexive
        if (o == this) {
            return true;
        }
        if (!(o instanceof Point2D)) { // This will allow mixed-type comparison, which means comparing subclass and superclass objects.
            return false;
        }
        Point2D another = (Point2D) o;
        return (x == another.x) && (y == another.y);
    }
}

class Point3D {
    private final int z;

    Point3D(int x, int y, int z) {
        super(x, y);
        this.z = z;
    }

    @Override
    public boolean equals(Object o) {
        // Check for equality in superclass
        if (!super.equals(o)) {
            return false;
        }
        if (!(o instanceof Point3D)) {  // This will allow mixed-type comparison, which means comparing subclass and superclass objects.
            return false;
        }
        Point3D another = (Point3D) o;
        return z == another.z;
    }
}

public class PointTest {

    public static void main(String[] args) {
        Point2D origin = new Point2D(0, 0);
        Point3D p1 = new Point3D(0, 0, -1);
        Point3D p2 = new Point3D(0, 0, 1);

        System.out.println("Comparing origin and p1 ...")
        System.out.println(origin.equals(p1));
        System.out.println(p1.equals(origin));

        System.out.println("Comparing origin and p2 ...")
        System.out.println(origin.equals(p2));
        System.out.println(p2.equals(origin));

        System.out.println("Comparing p1 and p2 ...")
        System.out.println(p1.equals(p2));
        System.out.println(p2.equals(p1));
    }

}

// Comparing origin and p1 ...
// true
// false
// Comparing origin and p2 ...
// true
// false
// Comparing p1 and p2 ...
// false
// false
```

From the results, we can see that this kind of implementation **violates** the **symmetry** and **transitivity** requirements.

This is because that we used **`isntanceof`** type check and thus allowed mixed-type comparison, which means comparing subclass and superclass objects.

<br>

However, if we are designing a **final** class, which means that there will be no extension to the class and thus there will be no mixed-type comparison.

Therefore, there will be no symmetry and transitivity problem, and this kind of implementation is **perfect**.

```java
public final class PhoneNumber {

    private final short areaCode;
    private final short exchange;
    private final short extension;

    public PhoneNumber(short areaCode, short exchange, short extension) {
        this.areaCode = areaCode;
        this.exchange = exchange;
        this.extension = extension;
    }

    @Override
    public boolean equals(Object o) {
        // Reflexive
        if (o == this) {
            return true;
        }
        if (!(o instanceof PhoneNumber)) { // This will allow mixed-type comparison, which means comparing subclass and superclass objects.
            // However, since this class is final, there wil be no extension to this class and thus there will be no mixed-type comparison.
            // Therefore, there will be no symmetry and transitivity problem, and this kind of implementation is perfect.
            return false;
        }
        PhoneNumber another = (PhoneNumber) o;
        return (areaCode == another.areaCode) && (exchange == another.exchange) && (extension == another.extension);
    }
}
```

<br>

We can also perform the type check using **`getClass()`** method as follows.

```java
class Point2D {
    private final int x;
    private final int y;

    Point2D(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public boolean equals(Object o) {
        // Reflexive
        if (o == this) {
            return true;
        }
        if (getClass() != o.getClass()) { // This will disallow mixed-type comparison.
            return false;
        }
        Point2D another = (Point2D) o;
        return (x == another.x) && (y == another.y);
    }
}

class Point3D {
    private final int z;

    Point3D(int x, int y, int z) {
        super(x, y);
        this.z = z;
    }

    @Override
    public boolean equals(Object o) {
        // Check for equality in superclass
        if (!super.equals(o)) {
            return false;
        }
        if (getClass() != o.getClass()) { // This will disallow mixed-type comparison.
            return false;
        }
        Point3D another = (Point3D) o;
        return z == another.z;
    }
}

public class PointTest {

    public static void main(String[] args) {
        Point2D origin = new Point2D(0, 0);
        Point3D p1 = new Point3D(0, 0, -1);
        Point3D p2 = new Point3D(0, 0, 1);

        System.out.println("Comparing origin and p1 ...")
        System.out.println(origin.equals(p1));
        System.out.println(p1.equals(origin));

        System.out.println("Comparing origin and p2 ...")
        System.out.println(origin.equals(p2));
        System.out.println(p2.equals(origin));

        System.out.println("Comparing p1 and p2 ...")
        System.out.println(p1.equals(p2));
        System.out.println(p2.equals(p1));
    }

}

// Comparing origin and p1 ...
// false
// false
// Comparing origin and p2 ...
// false
// false
// Comparing p1 and p2 ...
// false
// false
```

This kind of implementation perfectly complies to the `equals()` contract.

<br>

## Conclusion

Use **`instanceof`** test   =>   Allow mixed-type comparison, and there will be **symmetry and transitivity problem**

Use **`getClass()`** test.  =>.  Disallow mixed-type comparison, and thus is **perfect**

<br>

## Usage as Designer

* `final` Class

  Since there will be extension to this class, and thus there will be no mixed-type comparson.

  Thus **it will be okay to allow mixed-type comparison using `instanceof` test**.

* Non-final Class (Can be extended, and thus potentially a superclass)

  We need to follow the line of logic of the entire class hierarchy.

  In other words, if the superclass uses `isntanceof` test, we also need to use `isntanceof` test; if the superclass uses `getClass()` test, we also need to use `getClass()` test. 

  * **`instanceof`**

    **Meaning that the class hierarchy allows mixed-type comparison**

    As the designer of the current class, in order to avoid symmetry and transitivity problem, we need to make sure that subclasses only adds functionalities or fields that are not relevant to equality check by **declaring our `equals()` method as `final` to avoid it being overriden in the subclasses**.

    See below for the corresponding correct implementation.

  * **`getClass()`**

    **Meaning that the class hierarchy disallows mixed-type comparison**

```java
class Point2D {
    private final int x;
    private final int y;

    Point2D(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public final boolean equals(Object o) {
        // Reflexive
        if (o == this) {
            return true;
        }
        if (!(o instanceof Point2D)) { // This will allow mixed-type comparison, which means comparing subclass and superclass objects.
            return false;
        }
        Point2D another = (Point2D) o;
        return (x == another.x) && (y == another.y);
    }
}

class Point3D {
    private final int z;

    Point3D(int x, int y, int z) {
        super(x, y);
        this.z = z;
    }
}

public class PointTest {

    public static void main(String[] args) {
        Point2D origin = new Point2D(0, 0);
        Point3D p1 = new Point3D(0, 0, -1);
        Point3D p2 = new Point3D(0, 0, 1);

        System.out.println("Comparing origin and p1 ...")
        System.out.println(origin.equals(p1));
        System.out.println(p1.equals(origin));

        System.out.println("Comparing origin and p2 ...")
        System.out.println(origin.equals(p2));
        System.out.println(p2.equals(origin));

        System.out.println("Comparing p1 and p2 ...")
        System.out.println(p1.equals(p2));
        System.out.println(p2.equals(p1));
    }

}

// Comparing origin and p1 ...
// true
// true
// Comparing origin and p2 ...
// true
// true
// Comparing p1 and p2 ...
// true
// true
```

