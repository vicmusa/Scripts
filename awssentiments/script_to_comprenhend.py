import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    spk1 = []
    textspk1 = []
    textspk2 = []
    agent = ''
    client = ''
    key = event['key']
    bucket = 'transcribe-siscotel-infraestructura'
    
    s3_client = boto3.client('s3')
    
    response_s3 = s3_client.get_object(
        Key = key,
        Bucket = bucket)
        
    file = json.loads(response_s3['Body'].read())
    spk_segments = file["results"]["speaker_labels"]["segments"]
    for i,segments in enumerate(spk_segments):
        if segments['speaker_label']=='spk_0':
            spk1.append(i)

    print(spk1)
    text_segments = file['results']['segments']
    for i, segments  in enumerate(text_segments):
        if i in spk1:
            textspk1.append(segments['alternatives'][0]['transcript'])
        else:
            textspk2.append(segments['alternatives'][0]['transcript'])
            
    spk1finaltext = "\n".join(textspk1)
    spk2finaltext = "\n".join(textspk2)
    print(spk1finaltext)
    print(spk2finaltext)
    
    if "comunicarse al servicio" in spk1finaltext:
        agent =spk1finaltext
        client = spk2finaltext
    else:
        agent =spk2finaltext
        client = spk1finaltext
        
    
    table = "Transcribe_Test"
    item = {
        'id_meeting' : {
            'S': event['id_meeting']
        },
        'agent_text':{
            'S': agent
        },
         'client_text': {
             'S': client
         }
    }
    db_client = boto3.client('dynamodb')
    responsedb = db_client.put_item(TableName =table, Item= item)
        
    return {
        'statusCode': 200,
      'id_meeting' : event['id_meeting']
    }
