import psycopg2
import json
from datetime import datetime
import boto3 

#DB_HOST = "ec2-52-5-117-166.compute-1.amazonaws.com"
#DB_NAME = "dd1t8rsmuatdac"
#DB_USER = "uamcv7g7kcstt0"
#DB_PASS = "p98352151affa0a25606298ec69add2c17083eb25e60fe095e21c4ceeff50470f"

DB_HOST = "ec2-52-73-249-239.compute-1.amazonaws.com"
DB_NAME = "de6f8accmpl7s4"
DB_USER = "nnpeyxpboczbnd"
DB_PASS = "7076ca152cad0d3feabb38d2f7ef1d0c7f564ca24b33cb461ee86952077b3e45"

def lambda_handler(event, context):
    
    contact_list = []
    
    #Obtener datos de la tabla 
    
    try:
        conn = psycopg2.connect (dbname=DB_NAME, host=DB_HOST, user=DB_USER, password=DB_PASS)
        cursor = conn.cursor()
        cursor.execute("SELECT usr.id, usr.name, usr.email, usr.state, usr.userable_id, usr.userable_type, usr.username, usr.celularotp, usr.last_action_time, count(req.id) cant_reqs FROM public.users usr left join public.requests req on req.user_id = usr.id where usr.userable_type='NaturalPerson' and usr.state = 'active' and req.id is null group by usr.id, usr.name, usr.email, usr.state, usr.userable_id, usr.userable_type, usr.username, usr.celularotp, usr.last_action_time") # FECHA
        query = cursor.fetchall()
    except Exception as e:
        print(e) 
    finally:
        conn.close()
    
    #Formatear datos
    for data in query:
        if "gmail.com" in data[2] or "hotmail.com" in data[2] or "siscotelcloud.com" in data[2]:
            print(data[2])
            user = {} 
            user['ChannelType'] = 'EMAIL'
            user['Address'] = data[2]
            user['Location.Country'] = 'VEN'
            user['User.UserId'] = data[0]
            user['Attributes.Name'] = data[1]
            user['Attributes.State'] = data[3]
            user['Attributes.UserableId'] = data[4]
            user['Attributes.UserableType'] = data[5]
            user['Attributes.Username'] = data[6]
            user['Attributes.Celularotp']  = data[7]
            user['Attributes.LastActionTime'] = data[8].strftime('%d/%m/%y %H:%M')
            contact_list.append(user)
            
    #Insertar en S3.
    listofusers = {
        'listofusers': contact_list
    }
    with open('/tmp/sample.txt', 'w') as f:
         json.dump(listofusers, f)
    s3_client = boto3.client('s3')
    response = s3_client.upload_file('/tmp/sample.txt', 'pinpoint-contact-list', 'contact_list.json')
            

    # TODO implement
    return {
        'statusCode': 200
    }
