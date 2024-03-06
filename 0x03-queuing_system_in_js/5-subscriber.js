import redis from 'redis';

// Create a Redis client
const client = redis.createClient();

// Event handler for successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
  // Subscribe to the channel
  client.subscribe('holberton school channel');
});

// Event handler for connection errors
client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

// Event handler for received messages
client.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    // Unsubscribe and quit when receiving 'KILL_SERVER'
    client.unsubscribe('holberton school channel');
    client.quit();
  }
});

// Close the Redis connection when the script exits
process.on('SIGINT', () => {
  client.quit();
  process.exit();
});
