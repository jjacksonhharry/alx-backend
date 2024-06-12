// 6-job_creator.js
import kue from 'kue';

// Create a Kue queue
const queue = kue.createQueue();

// Job data
const jobData = {
  phoneNumber: '1234567890',
  message: 'This is a test notification',
};

// Create a job in the push_notification_code queue
const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    }
  });

// Listen for the 'complete' event
job.on('complete', () => {
  console.log('Notification job completed');
});

// Listen for the 'failed' event
job.on('failed', () => {
  console.log('Notification job failed');
});
