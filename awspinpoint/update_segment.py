import json
import boto3


def lambda_handler(event, context):
    
    client = boto3.client('pinpoint')
    response = client.create_import_job(
    ApplicationId='a37c567f873b41d69a97a7ff488333c7',
    ImportJobRequest={
        'DefineSegment': True,
        'Format': 'CSV',
        'RegisterEndpoints': True,
        'RoleArn': 'arn:aws:iam::583980982166:role/For_Labda_Pinpoint',
        'S3Url': 's3://pinpoint-contact-list/pinpoint_example_import.csv',
        'SegmentId': '29419c6025514d95be565b24d12e8dac',
    }
)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
