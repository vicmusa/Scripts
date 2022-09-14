import json
import boto3
import time

def lambda_handler(event, context):
    video = event['object']
    id_meeting = event['id_meeting']
    job_name = event['id_meeting']+'-transcribe_job'
    client = boto3.client('transcribe')
    response = client.start_transcription_job(
    TranscriptionJobName=job_name,
    LanguageCode='es-ES',
    MediaFormat='mp4',
    Media={
        'MediaFileUri': video,
    },
    OutputBucketName='transcribe-siscotel-infraestructura',
    OutputKey=id_meeting+'trancription.json',
    Settings={
        'ShowSpeakerLabels': True,
        'MaxSpeakerLabels': 2,
        'ShowAlternatives': True,
        'MaxAlternatives': 2,
        },
    )
    
    max_tries = 60
    while max_tries > 0:
        max_tries -= 1
        job = client.get_transcription_job(TranscriptionJobName=job_name)
        job_status = job['TranscriptionJob']['TranscriptionJobStatus']
        if job_status in ['COMPLETED', 'FAILED']:
            print(f"Job {job_name} is {job_status}.")
            if job_status == 'COMPLETED':
                print('Job Completed')
            break
        else:
            print(f"Waiting for {job_name}. Current status is {job_status}.")
        time.sleep(10)
        
    output = {
        
       
        
        
    }
    return {
        'statusCode': 200,
        "job_status": "COMPLETED",
        "id_meeting": event['id_meeting'],
        "key":id_meeting+'trancription.json',
    }
