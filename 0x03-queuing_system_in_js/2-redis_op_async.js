// Node Redis client and async operations

import redis from 'redis';
import { promisify } from 'util';

// Create a Redis client
const client = redis.createClient();

// Promisify the get and set methods of the Redis client
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Event handler for successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event handler for connection errors
client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

// Function to set a new school value in Redis
const setNewSchool = async (schoolName, value) => {
  await setAsync(schoolName, value);
};

// Async function to display the value for a given school name
const displaySchoolValue = async (schoolName) => {
  try {
    const reply = await getAsync(schoolName);
    console.log(reply);
  } catch (err) {
    console.error(`Error retrieving value for ${schoolName}: ${err}`);
  }
};

// Close the Redis connection when the script exits
process.on('SIGINT', () => {
  client.quit();
  process.exit();
});

// Call the functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
