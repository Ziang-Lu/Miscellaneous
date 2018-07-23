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
        if (!(o instanceof PhoneNumber)) {
            // This will allow mixed-type comparison, which means comparing subclass and superclass objects.
            // However, since this class is final, there wil be no extension to this class and thus there will be no
            // mixed-type comparison.
            // Therefore, there will be no symmetry and transitivity problem, and this kind of implementation is perfect.
            return false;
        }
        PhoneNumber another = (PhoneNumber) o;
        return (areaCode == another.areaCode) && (exchange == another.exchange) && (extension == another.extension);
    }
}