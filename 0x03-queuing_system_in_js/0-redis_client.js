// connect to the Redis server running on your machine

import redis from 'redis';

// Create a Redis client
const client = redis.createClient();

// Event handler for successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event handler for connection errors
client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

// Close the Redis connection when the script exits
process.on('SIGINT', () => {
  client.quit();
  process.exit();
});
