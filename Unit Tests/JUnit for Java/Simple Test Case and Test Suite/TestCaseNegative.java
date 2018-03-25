import junit.framework.TestCase;
import org.junit.Test;

public class TestCaseNegative extends TestCase {

    private String msg = "Robert";
    MessageUtil msgUtil = new MessageUtil(msg);

    @Test
    public void testGreetingMsg() {
        System.out.println("Inside " + getName());
        msg = "Hi! Robert";
        assertEquals(msgUtil.printMessage(), msg);
    }

}
