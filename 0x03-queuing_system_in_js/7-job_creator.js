import kue from 'kue';

// Create an array of jobs
const jobs = [
  { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
  { phoneNumber: '4153518781', message: 'This is the code 4562 to verify your account' },
  { phoneNumber: '4153518743', message: 'This is the code 4321 to verify your account' },
  { phoneNumber: '4153538781', message: 'This is the code 4562 to verify your account' },
  { phoneNumber: '4153118782', message: 'This is the code 4321 to verify your account' },
  { phoneNumber: '4153718781', message: 'This is the code 4562 to verify your account' },
  { phoneNumber: '4159518782', message: 'This is the code 4321 to verify your account' },
  { phoneNumber: '4158718781', message: 'This is the code 4562 to verify your account' },
  { phoneNumber: '4153818782', message: 'This is the code 4321 to verify your account' },
  { phoneNumber: '4154318781', message: 'This is the code 4562 to verify your account' },
  { phoneNumber: '4151218782', message: 'This is the code 4321 to verify your account' },
];

// Create a Kue queue
const queue = kue.createQueue();

// Process each job in the jobs array
for (const [index, jobData] of jobs.entries()) {
  // Create a new job in the push_notification_code_2 queue
  const notificationJob = queue.create('push_notification_code_2', jobData);

  // Log when the job is created
  notificationJob.save((err) => {
    if (!err) {
      console.log(`Notification job created: ${notificationJob.id}`);
    } else {
      console.error(`Error creating notification job: ${err}`);
    }
  });

  // Event handler for completed jobs
  notificationJob.on('complete', () => {
    console.log(`Notification job ${notificationJob.id} completed`);
  });

  // Event handler for failed jobs
  notificationJob.on('failed', (err) => {
    console.error(`Notification job ${notificationJob.id} failed: ${err}`);
  });

  // Event handler for job progress
  notificationJob.on('progress', (progress) => {
    console.log(`Notification job ${notificationJob.id} ${progress}% complete`);
  });
}

// Close the Kue queue when the script exits
process.on('SIGINT', () => {
  kue.shutdown(500, () => {
    process.exit(0);
  });
});
