import json
import boto3
import operator

def lambda_handler(event, context):
    # TODO implement
    sentimentsClient = []
    sentimentsAgent = []
    promSentimentAgent = {'Positive': 0.00, 'Negative': 0.00, 'Neutral': 0.00, 'Mixed': 00}
    promSentimentClient = {'Positive': 0.00, 'Negative': 0.00, 'Neutral': 0.00, 'Mixed': 00}
    key = {
        'id_meeting': {
           'S':event['id_meeting']
          }
          }
    table = "Transcribe_Test"
    db_client = boto3.client("dynamodb")
    item = db_client.get_item(TableName = table, Key = key)
    agenttext = item["Item"]["agent_text"]['S']
    clienttext = item["Item"]["client_text"]['S']
    clienttext = clienttext.split("\n")
    agenttext = agenttext.split("\n")
    comprehend_client = boto3.client('comprehend')
    
    for  text in clienttext:
        responseClient = comprehend_client.detect_sentiment(
            Text = text,
            LanguageCode='es')
        sentimentsClient.append(responseClient)
        promSentimentClient['Positive']+=responseClient['SentimentScore']['Positive']
        promSentimentClient['Negative']+=responseClient['SentimentScore']['Negative']
        promSentimentClient['Neutral']+=responseClient['SentimentScore']['Neutral']
        promSentimentClient['Mixed']+=responseClient['SentimentScore']['Mixed']
    for text in agenttext:
        responseAgent = comprehend_client.detect_sentiment(
            Text = text,
            LanguageCode='es')
        sentimentsAgent.append(responseAgent)
        promSentimentAgent['Positive']+=responseAgent['SentimentScore']['Positive']
        promSentimentAgent['Negative']+=responseAgent['SentimentScore']['Negative']
        promSentimentAgent['Neutral']+=responseAgent['SentimentScore']['Neutral']
        promSentimentAgent['Mixed']+=responseAgent['SentimentScore']['Mixed']
    print(sentimentsClient)
    
    
    #Darle sentido a los datos
    #Calculo del Promedio
    
    promA = len(agenttext)
  
    promSentimentAgent['Positive']=promSentimentAgent['Positive']/promA
    promSentimentAgent['Negative']=promSentimentAgent['Negative']/promA
    promSentimentAgent['Neutral']=promSentimentAgent['Neutral']/promA
    promSentimentAgent['Mixed']=promSentimentAgent['Mixed']/promA
    
    promC = len(clienttext)
    promSentimentClient['Positive']=promSentimentClient['Positive']/promC
    promSentimentClient['Negative']=promSentimentClient['Negative']/promC
    promSentimentClient['Neutral']=promSentimentClient['Neutral']/promC
    promSentimentClient['Mixed']=promSentimentClient['Mixed']/promC
    
    # Sacar Emocion dominante
    
    maxEmotionAgent = max(promSentimentAgent,key=promSentimentAgent.get)
    print(maxEmotionAgent)
    maxEmotionClient = max(promSentimentClient, key=promSentimentClient.get)
    print(maxEmotionClient)
    
    print(promSentimentAgent)
    
    
    #Insertarlos en Dynamodb
    
    updete_db = db_client.update_item(
        TableName = table,
        Key = {
            'id_meeting': {
                'S': event['id_meeting']
            }
            },
        UpdateExpression="set #prom_sentiments_A=:psA, #prom_sentiments_C=:psC, #domintant_A=:domi_a, #domintant_C=:domi_c",
        ExpressionAttributeNames={
        '#prom_sentiments_A': 'prom_sentiments_A',
        '#prom_sentiments_C': 'prom_sentiments_C',
        '#domintant_A': 'dominante_agente',
        '#domintant_C': 'dominante_cliente',
        },
        ExpressionAttributeValues={
        ':psA': {
            'S' : str(promSentimentAgent)  
        },
        ':psC':{
           'S': str(promSentimentClient)  
        },
        ':domi_a': {
            'S':maxEmotionAgent
        },
        ':domi_c':{
            'S':maxEmotionClient  
        },
        },
            )
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
