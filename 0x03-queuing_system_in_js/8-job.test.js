import chai from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job';

const { expect } = chai;

describe('createPushNotificationsJobs', () => {
  let queue;

  beforeEach(() => {
    // Create a Kue queue in test mode
    queue = kue.createQueue({ redis: { createClientFactory: () => kue.redis.createClient() }, testMode: true });
  });

  afterEach((done) => {
    // Clear the queue and exit test mode
    queue.testMode.clear();
    queue.shutdown(500, done);
  });

  it('should display an error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('invalid', queue)).to.throw('Jobs is not an array');
  });

  it('should create two new jobs to the queue', () => {
    const jobs = [
      { phoneNumber: '4153518780', message: 'Test message 1' },
      { phoneNumber: '4153518781', message: 'Test message 2' },
    ];

    createPushNotificationsJobs(jobs, queue);

    // Check the number of jobs in the queue
    expect(queue.testMode.jobs.length).to.equal(2);

    // Check if the job creation events were logged
    expect(queue.testMode.jobs[0].log[0]).to.equal('Notification job created: 1');
    expect(queue.testMode.jobs[1].log[0]).to.equal('Notification job created: 2');
  });

describe('createPushNotificationsJobs', () => {
  let queue;

  // Before each test, create a new Kue queue and enter test mode
  beforeEach(() => {
    queue = kue.createQueue();
    queue.testMode.enter();
  });

  // After each test, clear the queue and exit test mode
  afterEach(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should display an error message if jobs is not an array', () => {
    // Call the function with a non-array argument
    expect(() => createPushNotificationsJobs({}, queue)).to.throw('Jobs is not an array');

    // Ensure that no jobs were added to the queue
    expect(queue.testMode.jobs.length).to.equal(0);
  });

  it('should create two new jobs to the queue', () => {
    const jobs = [
      { phoneNumber: '4153518780', message: 'Test message 1' },
      { phoneNumber: '4153518781', message: 'Test message 2' },
    ];

    // Call the function with the array of jobs
    createPushNotificationsJobs(jobs, queue);

    // Ensure that two jobs were added to the queue
    expect(queue.testMode.jobs.length).to.equal(2);

    // Check the properties of the first job
    const job1 = queue.testMode.jobs[0];
    expect(job1.type).to.equal('push_notification_code_3');
    expect(job1.data.phoneNumber).to.equal('4153518780');
    expect(job1.data.message).to.equal('Test message 1');

    // Check the properties of the second job
    const job2 = queue.testMode.jobs[1];
    expect(job2.type).to.equal('push_notification_code_3');
    expect(job2.data.phoneNumber).to.equal('4153518781');
    expect(job2.data.message).to.equal('Test message 2');
  });
  
});
