import json
import boto3
from boto3.dynamodb.conditions import Key, Attr
from datetime import date
from datetime import datetime

bucket = 'pinpoint-contact-list'
key = 'contact_list.json'
dynamoTable = 'pinpoint_info'

client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(dynamoTable)

def verifydate(user, userDb, actfecha,now):
  
    print(userDb)
    flag = False  #Flag for validations
    listsize = len(userDb['sent']) - 1
    counter = userDb['counter']
    dateLS = datetime.strptime(userDb['sent'][listsize]['date'], '%d/%m/%y %H:%M') 
    diffdays = now - dateLS                                                      #Diff Between last email sent and today 
    if counter < 4:
        if actfecha < dateLS and diffdays.days >= 2 :
            flag = True
        if actfecha > dateLS:
            diffdays1 = now - actfecha
            if diffdays1.days >= 2:
                updete_db = client.update_item(
                TableName = dynamoTable,
                Key = {
                        'email': {
                            'S': email
                                 }
                      },
                UpdateExpression="SET #counter = :vals",
                ExpressionAttributeNames={"#counter": "counter"},
                ExpressionAttributeValues={":vals": { "N" : "0" }})
                flag = True
                #Resetear contador o hacer lo que se vaya a hacer
    return flag
        
    

def lambda_handler(event, context):
    # Variables para llenar
    finalList = []
    listofemail=[]
    
    #Cliente boto3
   
    
    #Fecha de hoy
    now = datetime.now()
    today = now.strftime("%d/%m/%y %H:%H")
    
    #tabla Dynamo
    
    
    # Get Object S3
    result = client.get_object(Bucket=bucket, Key=key)
    text = result["Body"].read().decode()
    jsonlist = json.loads(text)
    listofusers= jsonlist['listofusers'] # Cambiar a este para dejar de probar con el event
    #listofusers = event['listofusers']
    
    
    
    resp = table.scan()
    listofuserDynamoDb = resp['Items']
    
 
    for user in listofuserDynamoDb:
        listofemail.append(user['email'])
    
    
    print('--------------------event users--------------------------------')
    print(listofusers)
    print('--------------------------Dynamo Users-------------------------')
    print(listofuserDynamoDb)
    print("-------------------------final users-----------------------------------------------")
    
    

    for user in listofusers:
        actfecha = datetime.strptime(user['Attributes.LastActionTime'], '%d/%m/%y %H:%M')
        diff = now - actfecha
        if not user['Address'] in listofemail:
            if diff.days >= 7:
                finalList.append(user)
        else:
            for userDb in listofuserDynamoDb:
                if userDb['email'] == user['Address']:
                    if verifydate(user,userDb,actfecha,now):
                        finalList.append(user)
                        break
    
    
    for usuario in finalList:
        if usuario['Attributes.Name'] == " ":
            usuario['Attributes.Name'] = "USUARIO"
    
    fLOU = {
        'listofusers': finalList
    }
    with open('/tmp/sample.txt', 'w') as f:
         json.dump(fLOU, f)
    s3_client = boto3.client('s3')
    response = s3_client.upload_file('/tmp/sample.txt', 'pinpoint-contact-list', 'filtered_contact_list.json')
    
    return {
        'statusCode': 200,
    }
