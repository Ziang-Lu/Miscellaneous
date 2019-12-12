import java.io.IOException;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.net.InetSocketAddress;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

/**
 * TCP server demo.
 *
 * @author Ziang Lu
 */
public class TCPServer {

    /**
     * Thread function to handle TCP connection.
     */
    private static class TCPWorker implements Runnable {
        /**
         * TCP socket connection.
         */
        private Socket sock;

        /**
         * Constructor with parameter.
         * @param sock TCP socket connection
         */
        TCPWorker(Socket sock) {
            this.sock = sock;
        }

        @Override
        public void run() {
            System.out.println(String.format("[SERVER] Connection accepted from %s", sock.getRemoteSocketAddress()));
            try {
                DataOutputStream out = new DataOutputStream(sock.getOutputStream());
                DataInputStream in = new DataInputStream(sock.getInputStream());

                out.writeUTF("Welcome!");
                out.flush();
                while (true) {
                    String data = in.readUTF();
                    Thread.sleep(1000);
                    if (data.equals("") || data.equals("exit")) {
                        break;
                    }
                    out.writeUTF("Hello, " + data);
                    out.flush();
                }
                sock.close();
            } catch (IOException | InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println(
                    String.format("[SERVER] Connection accepted from %s CLOSED", sock.getRemoteSocketAddress()));
        }
    }

    /**
     * Main driver.
     * @param args arguments from command line
     */
    public static void main(String[] args) {
        try {
            // Create an IPv4, TCP server socket
            ServerSocket serverSocket = new ServerSocket();
            // Bind the server socket to server address "127.0.0.1:9999", and let the server start listening for
            // connections requests
            serverSocket.bind(new InetSocketAddress("127.0.0.1", 9999));
            System.out.println("[Server] Server bound to 127.0.0.1:9999");
            System.out.println("[SERVER] Listening for connection...");

            // => Use a thread pool to reuse the thread, and thus improve performance
            ExecutorService pool = Executors.newFixedThreadPool(50);
            while (true) {
                Socket sock = serverSocket.accept(); // Accepted a connection
                // We want to fire up a thread to handle the connection, so that the server is not blocked away from
                // other connections.
                // => Use a thread pool to reuse the thread, and thus improve performance
                pool.submit(new TCPWorker(sock));
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        /*
         * Output:
         * [SERVER] Server bound to 127.0.0.1:9999
         * [SERVER] Listening for connection...
         * [SERVER] Connection accepted from /127.0.0.1:59808
         * [SERVER] Connection accepted from /127.0.0.1:59808 CLOSED
         */
    }

}
