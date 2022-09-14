import json
import boto3
from boto3.dynamodb.conditions import Key, Attr


def lambda_handler(event, context):
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('pinpoint_info')
    finalList = []
    listofemail=[]
    resp = table.scan(FilterExpression=Attr('status actual').eq('clickeado'),)
    listofusers= event["listofusers"] 
    listofuserDynamoDb = resp['Items']
    
    for user in listofuserDynamoDb:
        listofemail.append(user['destino'])
    
    
    print('--------------------event users--------------------------------')
    print(listofusers)
    print('--------------------------Dynamo Users-------------------------')
    print(listofemail)
    print("-------------------------final users-----------------------------------------------")
    
    for user in listofusers:
        if not user['Address'] in listofemail:
            finalList.append(user)
    print(finalList)
    
    # TODO implement
    
    return {
        'statusCode': 200,
        'listofusers': finalList
    
    }
