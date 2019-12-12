import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;

/**
 * TCP client demo.
 *
 * @author Ziang Lu
 */
public class TCPClient {

    /**
     * Main driver.
     * @param args arguments from command line
     */
    public static void main(String[] args) {
        try {
            // Create an IPv4, TCP socket, and connect the socket to the server
            Socket s = new Socket("127.0.0.1", 9999);
            System.out.println("[CLIENT] Connecting to 127.0.0.1:9999...");

            DataInputStream in = new DataInputStream(s.getInputStream());
            DataOutputStream out = new DataOutputStream(s.getOutputStream());

            System.out.println(in.readUTF());
            String[] names = new String[]{"Michael", "Tracy", "Sarah"};
            for (String name : names) {
                out.writeUTF(name);
                out.flush();
                System.out.println(in.readUTF());
            }
            out.writeUTF("exit");

            // Close the socket
            s.close();
            System.out.println("[CLIENT] Client socket closed");
        } catch (IOException e) {
            e.printStackTrace();
        }

        /*
         * Output:
         * [CLIENT] Connecting to 127.0.0.1:9999...
         * Welcome!
         * Hello, Michael
         * Hello, Tracy
         * Hello, Sarah
         * [CLIENT] Client socket closed
         */
    }

}
