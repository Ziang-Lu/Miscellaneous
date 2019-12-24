import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetSocketAddress;

/**
 * UDP client demo.
 *
 * @author Ziang Lu
 */
public class UDPClient {

    /**
     * Main driver.
     * @param args arguments from command line
     */
    public static void main(String[] args) {
        try {
            DatagramSocket s = new DatagramSocket();

            // No need to connect the socket to the server

            String[] names = new String[]{"Michael", "Tracy", "Sarah"};
            for (String name : names) {
                DatagramPacket sentPacket = new DatagramPacket(name.getBytes(), name.length());
                sentPacket.setSocketAddress(new InetSocketAddress("127.0.0.1", 9999));
                s.send(sentPacket);

                // Although by default "DatagramSocket.receive()" is blocking, since the server immediately dumps back the new data
                // when it receives some data, we won't notice this blocking time.

                DatagramPacket receivedPacket = new DatagramPacket(new byte[1024], 1024);
                s.receive(receivedPacket);
                System.out.println(new String(receivedPacket.getData()).trim());
            }
            // Close the socket
            s.close();
        } catch (IOException e) {
            e.printStackTrace();
        }

        /*
         * Output:
         * Hello, Michael
         * Hello, Tracy
         * Hello, Sarah
         */
    }

}
