const net = require('net');

/**
 * TCP worker, set as the "connection" event listener of the server.
 * @param {net.Socket} sockConn connected socket
 */
function tcpWorker(sockConn) {
  // "connection" event listener
  const host = sockConn.remoteAddress;
  const port = sockConn.remotePort;
  console.log(`[SERVER] Connection accepted from ${host}:${port}`);

  // When this socket receives some data, it emits a "data" event.
  sockConn.on('data', buf => {
    // "data" event listener
    const data = buf.toString('utf8');
    if (data === 'exit') {
      sockConn.end(() =>
        console.log(`[SERVER] Connection from ${host}:${port} CLOSED`)
      );
      return;
    }
    // Deliberately sleep for 1 second before replying
    setTimeout(() => {
      sockConn.write(`Hello, ${data.toString('utf8')}`);
    }, 1000);
  });
}

// Create an IPv4, TCP server
const server = net.createServer(tcpWorker);
// When passing in "tcpServer", it is automatically set as the "connection"
// event listener of the server.
// This is equivalent to:
// server.on('connection', tcpWorker);

// Let the server start listening for connection requests
// server.listen() emits a "listening" event.
server.listen(9999, '127.0.0.1', null, () => {
  // "listening" event listener
  console.log('[SERVER] Server listening for connection...');
});

server.on('error', () => {
  // "error" event listener
  // Close the server
  server.close();
  console.log(err);
});

// Output:
// [SERVER] Server listening for connection...
// [SERVER] Connection accepted from 127.0.0.1:59647
// [SERVER] Connection from 127.0.0.1:59647 CLOSED
