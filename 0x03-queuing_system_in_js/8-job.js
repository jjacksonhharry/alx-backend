import kue from 'kue';

// Function to create push notification jobs
const createPushNotificationsJobs = (jobs, queue) => {
  // Check if jobs is an array
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  // Process each job in the array
  for (const [index, jobData] of jobs.entries()) {
    // Create a new job in the push_notification_code_3 queue
    const notificationJob = queue.create('push_notification_code_3', jobData);

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
};

export default createPushNotificationsJobs;
