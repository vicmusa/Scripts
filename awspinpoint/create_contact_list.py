import json
import boto3
import csv 
import io

s3 = boto3.client('s3')
def lambda_handler(event, context):
    # TODO implement
    
    s3 = boto3.client('s3')
    csvio = io.StringIO()
    writer = csv.writer(csvio)
    writer.writerow([
        "ChannelType","Address","Location.Country","User.UserId","Attributes.Name"
    ])
    
    listofusers= event["listofusers"]
    
    for user in listofusers:
        writer.writerow(
            [user["ChannelType"],user["Address"], user["Location.Country"],
            user["User.UserId"],user["Attributes.Name"]]
            )
    print(csvio.getvalue())
    s3.put_object(Body=csvio.getvalue(), ContentType='application/vnd.ms-excel', Bucket='pinpoint-contact-list', Key='pinpoint_example_import.csv')
    csvio.close()
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
