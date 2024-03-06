import kue from 'kue';

// Create a Kue queue
const queue = kue.createQueue();

// Object containing the Job data
const jobData = {
  phoneNumber: '123456789',
  message: 'Hello, this is a notification!',
};

// Create a job in the push_notification_code queue
const notificationJob = queue
  .create('push_notification_code', jobData)
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${notificationJob.id}`);
    } else {
      console.error(`Error creating notification job: ${err}`);
    }
  });

// Event handler for completed jobs
notificationJob.on('complete', () => {
  console.log('Notification job completed');
});

// Event handler for failed jobs
notificationJob.on('failed', (err) => {
  console.error(`Notification job failed: ${err}`);
});

// Close the Kue queue when the script exits
process.on('SIGINT', () => {
  kue.shutdown(500, () => {
    process.exit(0);
  });
});
