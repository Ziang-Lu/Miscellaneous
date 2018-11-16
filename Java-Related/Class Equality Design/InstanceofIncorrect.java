/**
 * 2D Point class.
 *
 * @author Ziang Lu
 */
class Point2D {
    /**
     * x-coordinate of the point.
     */
    private final int x;
    /**
     * y-coordinate of the point.
     */
    private final int y;

    /**
     * Constructor with parameter.
     * @param x x-coordinate of the point
     * @param y y-coordinate of the point
     */
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

/**
 * 3D point class.
 *
 * @author Ziang Lu
 */
class Point3D extends Point2D {
    /**
     * z-coordinate of the point.
     */
    private final int z;

    /**
     * Constructor with parameter.
     * @param x x-coordinate of the point
     * @param y y-coordinate of the point
     * @param z z-coordinate of the point
     */
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

public class InstanceofIncorrect {

    /**
     * Main driver.
     * @param args arguments from command line
     */
    public static void main(String[] args) {
        Point2D origin = new Point2D(0, 0);
        Point3D p1 = new Point3D(0, 0, -1);
        Point3D p2 = new Point3D(0, 0, 1);

        System.out.println("Comparing origin and p1 ...");
        System.out.println(origin.equals(p1));
        System.out.println(p1.equals(origin));

        System.out.println("Comparing origin and p2 ...");
        System.out.println(origin.equals(p2));
        System.out.println(p2.equals(origin));

        System.out.println("Comparing p1 and p2 ...");
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
