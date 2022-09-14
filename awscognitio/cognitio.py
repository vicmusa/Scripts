import json
import boto3
from botocore.exceptions import ClientError

# Read

def lambda_handler(event, context):
    email = event['email']
    password = event['password']
    user_pool_id = 'us-east-1_o9mvpKP2X'
    app_client_id = '3t7sg6ce25889g42s8djqqhm7e'
    client = boto3.client('cognito-idp')
    try:
        resp = client.initiate_auth(
        ClientId=app_client_id,
        AuthFlow='USER_PASSWORD_AUTH',
        AuthParameters={
            "USERNAME": email,
            "PASSWORD": password
        }
        )  
        token=resp['AuthenticationResult']['AccessToken']
        print("Log in success")
        print("Access token:", token)
        print("ID token:", resp['AuthenticationResult']['IdToken'])
        response = client.get_user(
        AccessToken=resp['AuthenticationResult']['AccessToken']
        )
        print(response)
    except ClientError as e:
        token = 'Unexpected error: %s' % e
    return {
        'statusCode': 200,
        'body': token
    }
