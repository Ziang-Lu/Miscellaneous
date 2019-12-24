const dgram = require('dgram');

// Create an IPv4, UDP socket
const s = dgram.createSocket('udp4', (msg, rinfo) => {
  // "message" event listener
  const host = rinfo.address;
  const port = rinfo.port;
  console.log(`[SERVER] Received from ${host}:${port}`);
  s.send(`Hello, ${msg.toString('utf8')}`, port, host);
});
// This is equivalent to:
// s.on('message', ...)

// Bind the socket to server address "127.0.0.1:9999"
// s.bind() emits a "listening" event => No need to listen for connection
s.bind(9999, 'localhost', () => {
  // "listening" event listener
  console.log('[SERVER] Server bound to 127.0.0.1:9999');
});

s.on('error', err => {
  // "error" event listener
  // Close the socket
  s.close();
});

// Output:
// [SERVER] Server bound to 127.0.0.1:9999
// [SERVER] Received from 127.0.0.1:55388
// [SERVER] Received from 127.0.0.1:55388
// [SERVER] Received from 127.0.0.1:55388
