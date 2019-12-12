import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetSocketAddress;

/**
 * UDP Server demo.
 *
 * @author Ziang Lu
 */
public class UDPServer {

    /**
     * Main driver.
     * @param args arguments from command line
     */
    public static void main(String[] args) {
        try {
            // Create an IPv4, UDP server socket, and bind the server socket to server address "localhost:9999"
            DatagramSocket serverSocket = new DatagramSocket(null);
            // Bind the server socket to server address "127.0.0.1:9999"
            serverSocket.bind(new InetSocketAddress("127.0.0.1", 9999));
            System.out.println("[Server] Server bound to 127.0.0.1:9999");

            // No need to listen for connections

            while (true) {
                DatagramPacket receivedPacket = new DatagramPacket(new byte[1024], 1024);
                serverSocket.receive(receivedPacket);
                System.out.println("[SERVER] Received from " + receivedPacket.getSocketAddress());
                String data = new String(receivedPacket.getData()).trim();

                String reply = "Hello, " + data;
                DatagramPacket replyPacket = new DatagramPacket(reply.getBytes(), reply.length());
                replyPacket.setSocketAddress(receivedPacket.getSocketAddress());
                serverSocket.send(replyPacket);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        /*
         * Output:
         * [Server] Server bound to 127.0.0.1:9999
         * [SERVER] Received from /127.0.0.1:59471
         * [SERVER] Received from /127.0.0.1:59471
         * [SERVER] Received from /127.0.0.1:59471
         */
    }

}
