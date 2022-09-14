import psycopg2
import json


DB_HOST = "ec2-3-231-112-124.compute-1.amazonaws.com"
DB_NAME = "d89q7434bhifcb"
DB_USER = "vsyhinnleuqmdn"
DB_PASS = "9186134652f5c9f2204748a4d6a19190b5bde145cf3cec0e98eda6ac71282dcf"

contact_list = []
def lambda_handler(event, context):
    
    #Obtener datos de la tabla 
    
    try:
        conn = psycopg2.connect (dbname=DB_NAME, host=DB_HOST, user=DB_USER, password=DB_PASS)
        cursor = conn.cursor()
        cursor.execute("SELECT email,name FROM users")
        json_string = json.dumps(dict(cursor.fetchall()))
        json_final = json.loads(json_string)
        print(type(json_string))
        print(type(json_final))
        print(json_string)
    except Exception as e:
        print(e) 
    finally:
        conn.close()
    
    #Formatear datos
    i = 1
    for key in json_final.keys():
        print(key)
        data = {
            'ChannelType': 'EMAIL',
            'Address': key,
            'Location.Country': 'VEN',
            'User.UserId' : i,
            'Attributes.Name': json_final[key]
        }
        contact_list.append(data)
        i += 1
    print(contact_list)        

    
    
    #
    
    # Formatear
    
    
    # Json
    
    

    # TODO implement
    return {
        'statusCode': 200,
        'listofusers': contact_list
    }
