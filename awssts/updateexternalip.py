import json
import boto3
    
hosted_zone = 'ZKLGMO49OSPPO'
    
def lambda_handler(event, context):
    ec2 = boto3.resource('ec2')
    instance = ec2.Instance(event['detail']['instance-id'])
    public_ip = instance.public_ip_address
    public_hostname = next((tag['Value'] for tag in instance.tags if tag['Key'] == "public-hostname"))
        	
        
    client_sts = boto3.client('sts')
    connect =  client_sts.assume_role(
            RoleArn="arn:aws:iam::583980982166:role/ExternalIPRegister",
            RoleSessionName="sts_connection"
        )
    print(connect)
    key = connect['Credentials']['AccessKeyId']
    secret = connect['Credentials']['SecretAccessKey']
    token = connect['Credentials']['SessionToken']
        
        
    route53 = boto3.client(
        	  'route53',
        	  aws_access_key_id = key,
        	  aws_secret_access_key = secret,
        	  aws_session_token = token,
          )
    if public_ip != None:
        response = route53.change_resource_record_sets(
                HostedZoneId = hosted_zone,
                ChangeBatch = {
            'Changes': [
                {
                    'Action': 'UPSERT',
                    'ResourceRecordSet': {
                        'Name': 'bancoplaza-'+ public_hostname +'.siscotel.io',
                        'Type': 'A',
                        'TTL': 60,
                        'ResourceRecords': [
                            {
                                'Value': public_ip
                            }
                        ],
                    }
                }   
            ]
        }
            )
            
        
        # TODO implement
    return {
            'statusCode': 200,
            'body': json.dumps('Hello from Lambda!')
        }
