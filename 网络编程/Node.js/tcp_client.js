const net = require('net');

// Create an IPv4, TCP server
const s = new net.Socket();

// Connect the socket to the server
// s.connect() emits a "connect" event.
s.connect(9999, '127.0.0.1', () => {
  // "connect" event listener
  console.log('[CLIENT] Connecting to 127.0.0.1:9999');

  s.write('Michael');

  // When this socket receives some data, it emits a "data" event.
  s.on('data', buf => {
    // "data" event listener
    console.log(buf.toString('utf8'));

    s.write('exit');
  });

  // When the other end of the socket calls "end()", this socket emits an "end"
  // event.
  s.on('end', () => {
    s.end();
    console.log('[CLIENT] Client socket closed');
  });
});

// Output:
// [CLIENT] Connecting to 127.0.0.1:9999
// Hello, Michael
// [CLIENT] Client socket closed
