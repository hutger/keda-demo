import boto3
import sys
import time


# Create SQS client
sqs = boto3.client('sqs')

message_count = int(sys.argv[1])

queue_url = 'https://sqs.us-east-2.amazonaws.com/579607414664/test_queue'

# Send message to SQS queue
for i in range(message_count):
    response = sqs.send_message(
        QueueUrl=queue_url,
        DelaySeconds=10,
        MessageAttributes={
            'Title': {
                'DataType': 'String',
                'StringValue': 'The Whistler'
            },
            'Author': {
                'DataType': 'String',
                'StringValue': 'John Grisham'
            },
            'WeeksOn': {
                'DataType': 'Number',
                'StringValue': '6'
            }
        },
        MessageBody=(
            'time.time()'
        )
    )

    print(response['MessageId'])
