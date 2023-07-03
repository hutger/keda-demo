import boto3
import sys

# Create SQS client
sqs = boto3.client('sqs')

message_count = int(sys.argv[1])

queue_url = 'https://sqs.us-east-2.amazonaws.com/579607414664/test_queue'

# Receive message from SQS queue
for i in range(message_count):
    response = sqs.receive_message(
        QueueUrl=queue_url,
        AttributeNames=[
            'SentTimestamp'
        ],
        MaxNumberOfMessages=1,
        MessageAttributeNames=[
            'All'
        ],
        VisibilityTimeout=0,
        WaitTimeSeconds=0
    )

    message = response['Messages'][0]
    receipt_handle = message['ReceiptHandle']

    # Delete received message from queue
    sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=receipt_handle
    )
    print('Received and deleted message: %s' % message)