/**
 * Phone number class.
 *
 * @author Ziang Lu
 */
public final class PhoneNumber {

    /**
     * Area code of this phone number.
     */
    private final short areaCode;
    /**
     * Exchange of this phone number.
     */
    private final short exchange;
    /**
     * Extension of this phone number.
     */
    private final short extension;

    /**
     * Constructor with parameters.
     * @param areaCode area code of the phone number
     * @param exchange exchange of the phone number
     * @param extension extension of the phone number
     */
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
