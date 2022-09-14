import json
import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    client = boto3.client('cognito-idp')
    a= "Texto"
    pool_id = 'us-east-1_o9mvpKP2X'
    email = event['email']
    password = event['password']
    client_id= '3t7sg6ce25889g42s8djqqhm7e'
    try:
        response = client.sign_up(
        ClientId=client_id,
        Username=email,
        Password=password,
        )
    
        response = client.admin_confirm_sign_up(
        UserPoolId=pool_id,
        Username=email,
        )
        
        
        response = client.admin_update_user_attributes(
        UserPoolId=pool_id,
        Username=email,
        UserAttributes=[
        {
            'Name': 'email_verified',
            'Value': 'true'
        },
        ],
    )
        a="User Created! and Confirmed"
    except ClientError as e:
        if e.response['Error']['Code']=='UsernameExistsException':
            a = 'user is already created'
        else:
            a = 'Unexpected error: %s' % e
          
          

    return {
            'statusCode': 200,
            'body': json.dumps(a)
            }
   
   
