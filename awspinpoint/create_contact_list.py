import json
import boto3
import csv 
import io

bucket = 'pinpoint-contact-list'
key = 'filtered_contact_list.json'
s3 = boto3.client('s3')
def lambda_handler(event, context):
    # TODO implement
    
    # Get Object S3
    result = s3.get_object(Bucket=bucket, Key=key)
    text = result["Body"].read().decode()
    jsonlist = json.loads(text)
    listofuser = jsonlist['listofusers']
    
    with open("/tmp/output.csv","w",newline="") as f:  
        title = "ChannelType,Address,Location.Country,User.UserId,Attributes.Name,Attributes.State,Attributes.UserableId,Attributes.UserableType,Attributes.Username,Attributes.Celularotp,Attributes.LastActionTime".split(",") # quick hack
        cw = csv.DictWriter(f,title,delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        cw.writeheader()
        cw.writerows(listofuser)
        
    s3.upload_file('/tmp/output.csv', 'pinpoint-contact-list', 'final_contact_list.csv')
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
