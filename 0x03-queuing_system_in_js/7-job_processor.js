import kue from 'kue';

// Array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Create a Kue queue
const queue = kue.createQueue({
  jobEvents: false, // Disable Kue job events for better control
});

// Function to send notifications
const sendNotification = (phoneNumber, message, job, done) => {
  // Track progress from 0 to 100%
  let progress = 0;

  // Function to update job progress
  const updateProgress = () => {
    job.progress(progress, 100);
    progress += 50;
  };

  // Fail the job if the phoneNumber is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    job.log(`Phone number ${phoneNumber} is blacklisted`);
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  } else {
    // Update progress to 50%
    updateProgress();

    // Log and update progress to 100%
    job.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    updateProgress();

    // Complete the job
    done();
  }
};

// Process jobs in the push_notification_code_2 queue with two jobs at a time
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});

// Close the Kue queue when the script exits
process.on('SIGINT', () => {
  kue.shutdown(500, () => {
    process.exit(0);
  });
});
