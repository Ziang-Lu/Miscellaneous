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

class Point3D extends Point2D {
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

public class GetClassCorrect {

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
// false
// false
// Comparing origin and p2 ...
// false
// false
// Comparing p1 and p2 ...
// false
// false