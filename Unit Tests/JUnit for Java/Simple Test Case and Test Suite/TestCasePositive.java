import junit.framework.TestCase;
import org.junit.Test;

public class TestCasePositive extends TestCase {

    private String msg = "Robert";
    MessageUtil msgUtil = new MessageUtil(msg);

    @Test
    public void testPrintMsg() {
        System.out.println("Inside " + getName());
        assertEquals(msgUtil.printMessage(), msg);
    }

}
