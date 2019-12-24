const dgram = require('dgram');

// Create an IPv4, UDP socket
const s = new dgram.Socket('udp4');

// No need to connect the socket to the server

const names = ['Michael', 'Tracy', 'Sarah'];
names.forEach(name => {
  s.send(name, 9999, '127.0.0.1');
});

let msgCount = 0;
// When this socket receives some data, it emits a "message" event.
s.on('message', msg => {
  // "message" event handler
  console.log(msg.toString('utf8'));
  ++msgCount;

  if (msgCount >= names.length) {
    s.close(() => console.log('[CLIENT] Client socket closed'));
  }
});

// Output:
// Hello, Michael
// Hello, Tracy
// Hello, Sarah
// [CLIENT] Client socket closed
