import json
import base64
from datetime import datetime
from dateutil import tz
import boto3

dbclient = boto3.client("dynamodb")
statusDic = {
    '_email.send' : 'enviado', 
    '_email.open' : 'abierto',
    '_email.delivered' :'recibido', 
    '_email.click' : 'clickeado'
        }
statusList = [ '_email.send', '_email.open','_email.delivered','_email.click']


def lambda_handler(event, context):
    # TODO implement
    
    for record in event['Records']:
        
        #Se hace el Decode de la info de Kinesis
        
        data = record['kinesis']['data']
        base64_bytes = data.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        filteredData = message_bytes.decode('utf-8')
        log = json.loads(filteredData)
    
        # Obtengo los datos importantes
        eventStatus = log['event_type']
    
        #Verfica si es evento de interes y obtener datos
        
        if eventStatus in statusList:
            eventTime = log['arrival_timestamp']
            eventTime = datetime.fromtimestamp (eventTime/1000).strftime('%d/%m/%y %H:%M')
            eventID = log["facets"]["email_channel"]["mail_event"]["mail"]["message_id"]
            eventDestination = log["facets"]["email_channel"]["mail_event"]['mail']["destination"][0]
            print(eventStatus,eventTime,eventID,eventDestination)
            
            
            updete_db = dbclient.update_item(
                TableName = 'pinpoint_info',
                Key = {
                        'id_message': {
                            'S': eventID
                                      }
                      },
                UpdateExpression="set #dateEvent=:ed, #event=:e, #destinationevent=:eds, #actualstatus=:ae ",
            ExpressionAttributeNames={
                '#dateEvent': 'fecha de ' + statusDic[eventStatus],
                '#event': statusDic[eventStatus],
                '#destinationevent': 'destino',
                '#actualstatus': 'status actual',
            },
            ExpressionAttributeValues={
                ':ed': {
                    'S' : eventTime  
                },
                ':e':{
                    'BOOL': True  
                    
                },
                ':eds': {
                    'S':eventDestination
                },
                ':ae':{
                    'S':statusDic[eventStatus]  
                },
            },
            )
        else :
            print('no')
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
 