import json
import base64
from datetime import datetime
from dateutil import tz
import boto3

dbclient = boto3.client("dynamodb")
statusDic = {
    '_email.send' : "sent", 
    '_email.open' : 'opened',
    '_email.delivered' :'delivered', 
    '_email.click' : 'clicked'
        }
statusList = [ '_email.send', '_email.open','_email.delivered','_email.click']


def lambda_handler(event, context):
    # TODO implement
    print(event)
    for record in event['Records']:
        
        #Se hace el Decode de la info de Kinesis
        
        data = record['kinesis']['data']
        base64_bytes = data.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        filteredData = message_bytes.decode('utf-8')
        log = json.loads(filteredData)
    
        #Obtengo los datos importantes
        eventStatus = log['event_type']
        print(eventStatus)
        #Verfica si es evento de interes y obtener datos
        
        if eventStatus in statusList:
            eventTime = log['arrival_timestamp']
            eventTime = datetime.fromtimestamp (eventTime/1000).strftime('%d/%m/%y %H:%M')
            eventID = log["facets"]["email_channel"]["mail_event"]["mail"]["message_id"]
            eventDestination = log["facets"]["email_channel"]["mail_event"]['mail']["destination"][0]
            print(eventStatus,eventTime,eventID,eventDestination)
            
            email = eventDestination
            eventDic = { 
                "M": {
                    "date": {"S":eventTime},
                    "id_message":{"S":eventID}
                }
            }
                
            if statusDic[eventStatus] == 'clicked':
                eventDic['M']['link'] = {'S':log['attributes']['feedback']} 
           
           
            listevet = []
            listevet.append(eventDic)
            
            updete_db = dbclient.update_item(
                TableName = 'pinpoint_info',
                Key = {
                        'email': {
                            'S': email
                                      }
                      },
                UpdateExpression="SET #ri = list_append(if_not_exists(#ri, :empty_list), :vals)",
            ExpressionAttributeNames={
                '#ri': statusDic[eventStatus],
            },
            ExpressionAttributeValues={ ":vals":{"L": listevet}, ":empty_list":{"L":[]} },
            )
            
            if statusDic[eventStatus] == 'sent':
                updete_db = dbclient.update_item(
                TableName = 'pinpoint_info',
                Key = {
                        'email': {
                            'S': email
                                      }
                      },
                UpdateExpression="SET #counter = if_not_exists(#counter, :initial) + :increment",
                ExpressionAttributeNames={"#counter": "counter"},
                ExpressionAttributeValues={":increment": { "N" : "1" }, ":initial": {"N":"0"}} )
                
                
        else :
            print('no')
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
