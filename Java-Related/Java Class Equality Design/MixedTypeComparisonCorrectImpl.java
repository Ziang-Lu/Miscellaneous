class MySuperClass {
    /**
     * Protected helper method to check whether this object is considered equal
     * to the given object.
     * Note that to handle case 4, we must introduce the otherBranch flag to
     * avoid falling into an infinite loop
     * @param o object to compare to
     * @param otherBranch whether to traverse in reversed order
     * @return whether this object is considered equal to o
     */
    protected boolean navigateClassHierarchyAndCheckEquality(Object o, boolean otherBranch) {
        return true;
    }

    @Override
    public boolean equals(Object o) {
        // Preliminary checks
        // Reflexive
        if (o == this) {
            return true;
        }
        // Check whether this and o are in the same class hierarchy
        if (!(o instanceof MySuperClass)) {
            return false;
        }

        // Delegate to navigateClassHierarchyAndCheckEquality() method
        return navigateClassHierarchyAndCheckEquality(o, false);
    }
}

class MyClass extends MySuperClass {
    /**
     * Default value for field1.
     */
    private static final int FIELD_1_DEFAULT = 0;
    /**
     * Default value for field2.
     */
    private static final int FIELD_2_DEFAULT = 0;

    /**
     * Dummy first field.
     */
    private final int field1;
    /**
     * Dummy second field.
     */
    private final int field2;

    /**
     * Default constructor.
     */
    MyClass() {
        this(FIELD_1_DEFAULT, FIELD_2_DEFAULT);
    }

    /**
     * Constructor with parameter.
     * @param field1 first field
     * @param field2 second field
     */
    MyClass(int field1, int field2) {
        this.field1 = field1;
        this.field2 = field2;
    }

    @Override
    protected boolean navigateClassHierarchyAndCheckEquality(Object o, boolean otherBranch) {
        if (getClass() == o.getClass()) { // Case 1
            // Check this object's own fields
            if (!checkOwnFields(o)) {
                return false;
            }
            // Delegate to superclass
            return super.navigateClassHierarchyAndCheckEquality(o, otherBranch);
        }
        if ((getClass().isAssignableFrom(o.getClass())) && (!otherBranch)) { // Case 3
            // The reason we discard the 'instanceof' test is because it will lead to this method being overwritten in
            // each subclass for testing against the corresponding type.
            // Switch the roles of this and o
            return ((MyClass) o).navigateClassHierarchyAndCheckEquality(this, true);
        } else { // Case 2 & 4
            // Check this object's own fields
            if (!checkOwnFields(o)) {
                return false;
            }
            // Delegate to the superclass of this
            return super.navigateClassHierarchyAndCheckEquality(o, otherBranch);
        }
    }

    /**
     * Private helper method to check whether this object's own fields are
     * considered equal to the given object.
     * @param o object to compare to
     * @return whether this object's own fields are considered equal to o
     */
    private boolean checkOwnFields(Object o) {
        if (o instanceof MyClass) {
            // this and o are of the same type
            // or
            // this -> superclass
            // o -> subclass
            // Only check the common fields, which are exactly the fields in this
            MyClass another = (MyClass) o;
            return (field1 == another.field1) && (field2 == another.field2);
        } else {
            // o -> superclass
            // this -> subclass
            // Only check the subclass-specific parts against default values
            return (field1 == FIELD_1_DEFAULT) && (field2 == FIELD_2_DEFAULT);
        }
    }
}

class MySubClass1 extends MyClass {}

class MySubClass2 extends MyClass {}

class MySubSubClass extends MySubClass2 {}

public class MixedTypeComparisonCorrectImpl {

    /**
     * Main driver.
     * @param args arguments from command line
     */
    public static void main(String[] args) {
        MyClass thisObj = new MyClass();
        MyClass other = null;

        // Case 1: this and other are of exact the same type
        other = new MyClass();
        System.out.println(thisObj.equals(other));

        // Case 2: this is a subclass of other
        MySuperClass otherSuper = new MySuperClass();
        System.out.println(thisObj.equals(otherSuper));

        // Case 3: this is a superclass of other
        MySubClass1 otherSub = new MySubClass1();
        System.out.println(thisObj.equals(otherSub));

        // Case 4: this and other are of different branches in the class hierarchy
        MySubClass1 thisSub = new MySubClass1();
        MySubSubClass otherSubSub = new MySubSubClass();
        System.out.println(thisSub.equals(otherSubSub));
    }

}
